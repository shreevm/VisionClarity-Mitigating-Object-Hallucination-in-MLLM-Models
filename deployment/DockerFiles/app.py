import gradio as gr
import torch
import joblib
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load the trained model and processor
processor = joblib.load('./blip_processor.pkl')  # Path to the processor file
model = joblib.load('./blip_trained_model.pkl')  # Path to the trained model file

# Set the device (use GPU if available, otherwise fallback to CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()  # Set model to evaluation mode

# Function to generate product name and description
def generate_description(image):
    """
    Generates the product name and description based on the image.
    """
    try:
        # Preprocess the image for the model
        inputs = processor(images=image, return_tensors="pt").to(device)

        # Generate a caption for the image
        with torch.no_grad():
            output = model.generate(**inputs, max_length=50)
            generated_caption = processor.decode(output[0], skip_special_tokens=True)

        # Extract product name and description from the generated caption
        parts = generated_caption.split("|")
        product_name = parts[0].strip() if len(parts) > 0 else "Product name not available."
        product_description = parts[1].strip() if len(parts) > 1 else "Description not available."

        # Return only the product name and description
        return f"**Product Name:** {product_name}\n\n**Product Description:** {product_description}"
    except Exception as e:
        return f"Error generating description: {e}"

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_description,
    inputs=gr.Image(type="pil"),  # Input type: image (PIL format)
    outputs="text",  # Output type: single text block
    live=True,  # Update output in real-time
)

# Launch the Gradio interface
if __name__ == "__main__":
    iface.launch(debug=True)
