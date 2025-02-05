import os
import logging
from flask import Flask, request, jsonify, send_from_directory
from gpt4all import GPT4All

# Disable unnecessary logs
logging.getLogger("gpt4all").setLevel(logging.ERROR)

# Debugging: Print only necessary startup steps
print("✅ Starting Flask Chatbot...")

app = Flask(__name__)

# Disable GPU usage (Force CPU mode)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["NO_CUDA"] = "1"

# Load GPT4All Model (Use absolute path to the model)
model_path = r"C:\GPT4All-Chatbot\models\mpt-7b-chat-newbpe-q4_0.gguf"  # Use your model path

try:
    model = GPT4All(model_path, allow_download=False, n_threads=os.cpu_count())  # Use all CPU cores
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit(1)

# Define routes
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot requests."""
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Generate response with optimized settings
    try:
        response = model.generate(user_input, 
                                  max_tokens=100,  # Allow slightly longer responses
                                  temp=0.7,        # Increase temperature for slightly more creativity
                                  top_k=50,        # Ensure diversity in word selection
                                  top_p=0.9)       # A bit more randomness but within bounds

        # Log the response for debugging
        print(f"Response: {response}")

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Fix missing favicon request
@app.route('/favicon.ico')
def favicon():
    return "", 204  # No Content response

# Start Flask Server
if __name__ == "__main__":
    print("✅ Flask server is running at http://127.0.0.1:5000")
    app.run(debug=False, host="0.0.0.0", port=5000)
