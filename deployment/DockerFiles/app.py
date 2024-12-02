import gradio as gr
import torch
import joblib
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import time
from prometheus_client import start_http_server, Counter, Gauge
import threading

# Initialize Prometheus metrics
REQUEST_COUNT = Counter('gradio_app_requests_total', 'Total number of requests')
GENERATE_LATENCY = Gauge('gradio_app_generate_latency', 'Latency for generating product descriptions')
FEEDBACK_COUNT = Counter('gradio_app_feedback_total', 'Total number of feedbacks')
FEEDBACK_RATING = Gauge('gradio_app_feedback_rating', 'User rating for the description')

# Start Prometheus metrics server on port 8000
def start_metrics_server():
    start_http_server(8000)  # Expose metrics on port 8000

threading.Thread(target=start_metrics_server, daemon=True).start()

# Load the trained model and processor
processor = joblib.load('./fine_tuned_processor.pkl')  # Load processor
model = joblib.load('./fine_tuned_model.pkl')  # Load trained model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()  # Set model to evaluation mode

# Function to generate caption and simulate product details
def generate_description(image):
    """
    Generate a product description based on the uploaded image.
    """
    try:
        # Preprocess the image for the model
        start_time = time.time()  # Start latency timer
        inputs = processor(images=image, return_tensors="pt").to(device)
        
        # Generate a description for the image
        with torch.no_grad():  # No need to compute gradients for inference
            output = model.generate(**inputs, max_length=50)
            generated_caption = processor.decode(output[0], skip_special_tokens=True)

        # Extract product description from the generated caption
        if "|" in generated_caption:
            parts = generated_caption.split("|")
            product_description = parts[0].strip()  # First part contains the main description
        else:
            product_description = generated_caption.strip()
        
        # Calculate latency
        latency = time.time() - start_time
        REQUEST_COUNT.inc()  # Increment request count
        GENERATE_LATENCY.set(latency)  # Track latency
        return product_description, f"{latency:.2f} seconds"
    except Exception as e:
        return f"Error generating description: {e}", "N/A"

# Collect feedback and rating
def collect_feedback(product_description, feedback, rating):
    """
    Collect user feedback and rating for the generated description and push metrics to Prometheus.
    """
    FEEDBACK_COUNT.inc()  # Increment feedback count
    if rating:
        FEEDBACK_RATING.set(rating)  # Set the latest rating value
    feedback_summary = f"Feedback: {feedback}" if feedback else "No feedback provided."
    rating_summary = f"Rating: {rating}/5" if rating else "No rating provided."
    return feedback_summary, rating_summary

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("### VisionClarity: Product Description Generator"),
    gr.Markdown("Upload an image to generate a product description, and optionally provide feedback.")

    # Step 1: Image Upload and Description Generation
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Image")  # Input for image upload
        with gr.Column():
            description_output = gr.Textbox(label="Product Name & Description", interactive=False)
            latency_output = gr.Textbox(label="Latency (seconds)", interactive=False)

    # Step 2: Feedback and Rating
    with gr.Row():
        with gr.Column():
            feedback_input = gr.Textbox(label="Your Feedback")
            rating_input = gr.Slider(minimum=1, maximum=5, step=1, label="Rate the Description (1-5)")
        with gr.Column():
            feedback_output = gr.Textbox(label="User Feedback", interactive=False)
            rating_output = gr.Textbox(label="User Rating", interactive=False)

    # Logic for Step 1: Generate Description
    image_input.change(
        fn=generate_description,
        inputs=image_input,
        outputs=[description_output, latency_output]
    )

    # Logic for Step 2: Collect Feedback and Rating
    feedback_input.change(
        fn=collect_feedback,
        inputs=[description_output, feedback_input, rating_input],
        outputs=[feedback_output, rating_output]
    )
    rating_input.change(
        fn=collect_feedback,
        inputs=[description_output, feedback_input, rating_input],
        outputs=[feedback_output, rating_output]
    )

# Launch the Gradio interface
demo.launch(server_name="0.0.0.0", server_port=7860, debug=True)
