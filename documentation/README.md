# VisionClarity: Mitigating Object Hallucination for Accurate Product Descriptions

## Project Overview

**Objective**:  
The VisionClarity project aims to create a robust system that mitigates object hallucination to ensure accurate product descriptions and reliable visual search. Object hallucination occurs when a model mistakenly identifies or describes objects that are irrelevant or absent from an image. VisionClarity addresses this challenge through two primary goals:
1. **Generate Accurate Product Descriptions**: VisionClarity ensures that product descriptions align closely with actual product images, minimizing errors caused by object hallucination, where inaccurate details might be described.
2. **Provide Reliable Visual Search**: Users can search for products using images, and the system will generate matching, accurate descriptions without hallucinating irrelevant information.

## Repository Contents

### `src/`
Contains the core system code for VisionClarity, including:
- **main.py**: The entry point for the application. It includes the logic for loading models, processing images, and generating product descriptions.
- **models/**: The machine learning models used for generating product descriptions and mitigating hallucinations.
- **utilities/**: Utility functions used for data processing, model handling, and other support tasks.
- **data/**: Sample data used for testing the system (if applicable).

### `deployment/`
Contains files for containerizing and deploying the application:
- **Dockerfile**: The configuration file to build a Docker container for VisionClarity, enabling easy deployment in different environments.
- **ci-cd-pipeline.yml**: Continuous integration/continuous deployment (CI/CD) configuration, automating the build and deployment process.

### `monitoring/`
Contains configuration files for performance monitoring:
- **Prometheus.yml**: Configuration for Prometheus to scrape metrics from the application.
- **grafana_dashboard.json**: The Grafana dashboard configuration used to visualize metrics collected by Prometheus.

### `documentation/`
Contains project lifecycle documents:
- **AI System Project Proposal**: A detailed project proposal outlining the objectives, methodology, and expected outcomes of the VisionClarity project.
- **Project Report** (optional): A comprehensive report summarizing the project's development, testing, results, and conclusions.

### `videos/`
Contains a demo screencast showcasing the VisionClarity system in action, including:
- The deployment process
- Metrics scraping and visualization
- Real-life example of how the product descriptions are generated and visualized through Grafana

## System Entry Point

### Main Script: `src/main.py`

1. **Running the system locally**:
    - Install dependencies:  
      ```bash
      pip install -r requirements.txt
      ```
    - Run the system:
      ```bash
      python src/main.py
      ```

2. **Running the system in a containerized environment**:
    - Build the Docker image:
      ```bash
      docker build -t visionclarity-app .
      ```

    - Run the container:
      ```bash
      docker run -p 7860:7860 -p 8000:8000 visionclarity-app
      ```

    This will expose the application at `http://localhost:7860`.

## Video Demonstration

Watch the video demonstration of VisionClarity, where we showcase:
- How the application works in real-time
- How product descriptions are generated
- The metrics scraping process with Prometheus and Grafana
- The entire deployment process

### Link to Video Demo:
[Link to Demo Video](path/to/demo/video)

## Deployment Strategy

**Deployment Method**:  
The application is deployed using **Docker**, allowing for easy containerization and deployment across different environments. The Docker container includes all necessary dependencies, ensuring that the system runs smoothly across any platform.

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t visionclarity-app .



