from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import google.generativeai as genai
import os 
import random


# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)


# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "generate a random quote according to the number 153\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "\"The universe whispers secrets in the rustle of leaves, the hum of bees, and the laughter of children. Only those who listen with a quiet heart can hear them.\" \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "generate a random quote according to the number 257\n\n\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "\"The journey of a thousand miles begins with a single step, but it's the stories you tell along the way that truly matter.\" \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "generate a random quote according to the number 1588\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "\"The world is a tapestry woven with threads of both light and shadow. Embrace the darkness, for it is in the depths that we find the strength to rise.\" \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "generate a random quote according to the number 153\n\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "\"The heart is a compass, guiding us towards the truth we seek, even when the path is shrouded in uncertainty.\" \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "generate a random quote according to the number 855746",
      ],
    },
    {
      "role": "model",
      "parts": [
        "\"The stars whisper secrets in the language of the night sky, revealing truths only visible to those who dare to dream.\" \n",
      ],
    },
  ]
)


# Initialize Flask.
app = Flask(__name__)

# Define routing.
@app.route('/')
def index():
    response = chat_session.send_message(f"Generate a random quote according to {random.randint(1,10000)}")

    return render_template('index.html', quote=response.text)

if __name__ == '__main__':
   app.run()

 