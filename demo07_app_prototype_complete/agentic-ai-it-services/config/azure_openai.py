# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path).
folder_path = os.path.join(os.path.dirname(__file__), '../..')
sys.path.insert(0, folder_path)

import config

# Start.
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create reusable Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
