import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env file
print("DEBUG: Loading .env file...")
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"DEBUG: API key loaded -> {api_key[:6]}********")

if not api_key:
    raise ValueError("❌ API key not found. Please set GOOGLE_API_KEY in your .env file")

# Configure Gemini API
genai.configure(api_key=api_key)

# Ask user for topic
topic = input("Enter a topic: ")
print("\nGenerating post...\n")

# Use Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")
prompt = f"Write a catchy social media post about {topic}. Include emojis and hashtags."

response = model.generate_content(prompt)

# Show post on screen
print("✅ Generated Post:\n")
print(response.text)

# Save post to a file
with open("generated_post.txt", "w", encoding="utf-8") as f:
    f.write(response.text)
print("\n📝 Post saved to generated_post.txt!")
