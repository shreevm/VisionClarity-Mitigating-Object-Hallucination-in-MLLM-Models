# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container
COPY . /app

# Install necessary system packages
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean

# Install Python dependencies
RUN pip install --no-cache-dir torch torchvision transformers gradio joblib pillow scikit-learn

# Expose the port Gradio will use
EXPOSE 7860

# Command to run the application
CMD ["python", "app.py"]
