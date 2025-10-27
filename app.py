from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    try:
        topic = request.json.get("topic")
        model = genai.GenerativeModel("models/gemini-2.5-flash")
        response = model.generate_content(f"Write 3 short marketing post options about {topic}. Label them as Option 1, Option 2, Option 3.")
        return jsonify({"post": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print("✅ MZStudio is Live 🚀")
    print("Go to http://127.0.0.1:5000")
    app.run(debug=True)



