from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

import openai
import os

app = Flask(__name__)

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    try:
        response = client.chat.completions.create(
            model="grok-3-beta",
            messages=[
                {"role": "system", "content": "You are Grok, a highly intelligent, helpful AI assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7,
            stream=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(e)
        reply = f"Error：{str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
