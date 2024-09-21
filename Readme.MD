

# Random Quote Generator - Flask App

This Flask-based web application leverages Google's LLM Gemini API to generate and display random quotes. The application is fully Dockerized and deployed to Azure.
![Preview](https://github.com/Salmoon8/Random-Quotes/blob/main/static/css/Screenshot%202024-09-21%201404172.png)


## Features

- Generates random quotes using the Gemini API
- Responsive web interface for displaying quotes
- Dockerized for easy deployment and portability
- Deployed to Azure Container Apps for scalability
- Uses Gunicorn as the WSGI HTTP Server for improved performance

## Technologies Used

- **Backend**: Flask (Python)
- **GEMINI API**: Google's LLM Gemini API
- **Containerization**: Docker
- **Cloud Platform**: Microsoft Azure (Container Apps)
- **WSGI HTTP Server**: Gunicorn

## Prerequisites

- Python 3.8+
- Docker
- Google developer account with Gemini API access
- Azure account (for deployment)

## Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/Salmoon8/Random-Quotes
   cd Random-Quotes
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Gemini API key: `GEMINI_API_KEY=your_api_key_here`

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Docker Usage

1. Build the Docker image:
   ```
   docker build -t random-quote-generator .
   ```

2. Run the container:
   ```
   docker run --detach --publish 5000:50505 random-quote-generator
   ```

3. Access the application at `http://localhost:5000`

## Deployment to Azure

1. Create an Azure Container Registry (ACR)
2. Push your Docker image to ACR
3. Create an Azure Container App, linking it to your ACR image
4. Set the necessary environment variables in the Azure Container App configuration


## API Reference

The application uses the Gemini API to generate quotes. For more information on the API usage and capabilities, refer to the [Gemini API Documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini).

