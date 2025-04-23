from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()  
    message = data.get("message", "")
    print("收到訊息：", message)

    reply = f"你說的是：{message}"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
