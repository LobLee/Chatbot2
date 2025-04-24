from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import time
import logging
from chatbot import get_response  # ✅ Import the chatbot function

# ✅ Setup Flask App
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ Configurable CORS

# ✅ Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@app.route("/chat", methods=["GET", "POST"])  # ✅ Allows both GET and POST
def chat():
    if request.method == "GET":
        return jsonify({"message": "Chatbot API is running. Use POST to send messages."}), 200

    if request.content_type != "application/json":
        logging.warning("Invalid content type")
        return jsonify({"error": "Content-Type must be application/json"}), 415

    try:
        data = request.get_json(silent=True)

        if not data or "message" not in data:
            logging.warning("No message received in request")
            return jsonify({"error": "No message received"}), 400

        user_message = data["message"].strip().lower()
        logging.info(f"Received message: {user_message}")

        # ✅ Get response from chatbot.py
        response_text = get_response(user_message)
        logging.info(f"Response: {response_text}")

        return jsonify({"response": response_text})

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500  # ✅ Handles unexpected errors


if __name__ == "__main__":
    logging.info("Starting Flask server...")
    app.run(debug=True, host="0.0.0.0", port=5000)  # ✅ Runs Flask on all interfaces
