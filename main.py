import os
import subprocess
import sys

# Install openai if not already installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])

import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Set API key
openai.api_key = os.getenv("API_KEY")

# Example usage
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)