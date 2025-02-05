# GPT4All Chatbot
A lightweight, AI-powered chatbot built using the GPT4All library and Flask . This chatbot runs entirely on your local machine, eliminating the need for external APIs or internet connectivity. 
Perfect for personal use, educational purposes, or experimentation with conversational AI.

## Features
Local Execution : Runs offline on your machine without relying on external APIs.

Efficient Model : Utilizes the mpt-7b-chat-newbpe-q4_0.gguf model for fast, natural, and context-aware responses.

User-Friendly Interface : A clean and simple web-based UI for seamless interaction.

Customizable : Easily swap models, tweak parameters, or extend functionality.

Open Source : Built using the open-source GPT4All library.

## 🛠️ Installation
**Prerequisites**

Python 3.8 or higher installed on your system.

Git (optional, for cloning the repository).

**Steps**

Clone the Repository :
git clone https://github.com/your-username/GPT4All-Chatbot.git
cd GPT4All-Chatbot

Install Dependencies :
Install the required Python libraries:
pip install -r requirements.txt

Download the Model :
Visit the GPT4All Models Page and download the mistral-7b-instruct-v0.2.Q4_K_M.gguf.

Place the downloaded model file in the models folder.

Run the Application :
Start the Flask server:
python app.py

Access the Chatbot :
Open your browser and navigate to:
http://127.0.0.1:5000


## 🚀 Usage
Type your question in the input box and click "Send" .

The chatbot will generate a response using the mistral-7b-instruct-v0.2.Q4_K_M.gguf.
**Example Questions**

"What is machine learning?"

"How do I write a strong resume?"

"Explain recursion in Python."

**Tips for Better Responses**

Use clear and concise inputs.

Avoid overly complex or ambiguous questions.

Experiment with the max_tokens parameter in app.py to control response length.
