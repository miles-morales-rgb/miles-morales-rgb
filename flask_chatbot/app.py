from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chatbot</title>
    <style>
        body { background: #111; color: white; font-family: Arial, sans-serif; margin-top: 50px; text-align: center; }
        .chat-box { max-width: 500px; margin: auto; background: #222; padding: 20px; border-radius: 10px; }
        .messages { text-align: left; max-height: 300px; overflow-y: auto; margin-bottom: 10px; }
        .messages div { margin: 5px 0; }
        .messages .user { color: #4caf50; }
        .messages .bot { color: #03a9f4; }
        input { width: 70%; padding: 10px; border: none; border-radius: 5px; }
        button { padding: 10px; background: #03a9f4; border: none; color: white; border-radius: 5px; }
    </style>
</head>
<body>

<div class="chat-box">
    <h2>Chatbot</h2>
    <div class="messages" id="messages"></div>
    <form onsubmit="sendMessage(event)">
        <input type="text" id="userInput" placeholder="Type your message..." autocomplete="off" required>
        <button type="submit">Send</button>
    </form>
</div>

<script>
    function sendMessage(event) {
        event.preventDefault();
        let input = document.getElementById("userInput");
        let message = input.value;
        if (!message.trim()) return;

        addMessage(message, "user");
        fetch("/get_response", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: message })
        })
        .then(res => res.json())
        .then(data => {
            addMessage(data.reply, "bot");
            input.value = "";
        });
    }

    function addMessage(msg, sender) {
        let messagesDiv = document.getElementById("messages");
        let div = document.createElement("div");
        div.className = sender;
        div.textContent = msg;
        messagesDiv.appendChild(div);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/get_response", methods=["POST"])
def get_response():
    user_msg = request.json.get("message", "").lower().strip()

    if "hello" in user_msg or "hi" in user_msg:
        reply = "Hello! How can I assist you today?"
    elif "how are you" in user_msg:
        reply = "I'm good! Thanks for asking. What about you?"
    elif "your name" in user_msg:
        reply = "I'm FlaskBot, your friendly chatbot assistant."
    elif "bye" in user_msg or "goodbye" in user_msg:
        reply = "Goodbye! Have a great day ahead!"
    elif "who created you" in user_msg or "who made you" in user_msg:
        reply = "I was created using Python and Flask by a developer like you."
    elif "help" in user_msg:
        reply = "I can answer simple questions like hello, how are you, or your name. Try typing something!"
    else:
        reply = f"Sorry, I didn’t understand: {user_msg}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
