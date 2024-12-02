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

    - **Download the pre-trained model** from Google Drive:
      Since the model file is large, you can download it directly from Google Drive using the following link:  
      [Download the model](https://drive.google.com/file/d/1Xrpo-fuwqbaeOnKht5V2DSTkPUGzNZUo/view?usp=sharing)

      After downloading the model, move it to your project directory or specify the correct path in the code. The model is necessary for generating product descriptions accurately.

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
[Link to Demo Video](video)

## Deployment Strategy

**Deployment Method**:  
The application is deployed using **Docker**, allowing for easy containerization and deployment across different environments. The Docker container includes all necessary dependencies, ensuring that the system runs smoothly across any platform.

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t visionclarity-app .
   ```
2.  Run the Docker container:
   
   ```bash
    docker run -p 7860:7860 -p 8000:8000 visionclarity-app
   ```
### Monitoring and Metrics
We use Prometheus and Grafana for monitoring the performance of the VisionClarity application.

Prometheus is used to scrape metrics from the application, such as request counts, latency, and system performance.
Grafana is used to visualize the metrics collected by Prometheus. The Grafana dashboard can be accessed at http://localhost:3000.
Monitoring Setup in Docker
To enable Prometheus and Grafana for monitoring, please refer to the docker-compose.yml and prometheus.yml files in the monitoring/ folder.

### Project Documentation
AI System Project Proposal
Project Report 

### Version Control and Team Collaboration
Version Control: We use Git for version control. The repository is managed with the following branching strategy:
main: The stable branch with production-ready code.

Code Review: All pull requests are reviewed by a team member before being merged into the main branch to ensure code quality and consistency


