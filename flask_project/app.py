from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Existing routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

# ✅ Separate chatbot page
@app.route('/chatbot')
def chatbot_page():
    return render_template('chatbot.html')

# Chatbot API
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    if "hello" in user_message.lower():
        bot_response = "Hello! How can I help you today?"
    else:
        bot_response = "This is a demo bot. Ask about AI or site info."
    return jsonify({"response": bot_response})
@app.route('/premium')
def premium():
    return "Upgrade to Premium for full AI features!"


@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    # Email ko file me save karte hain
    with open("subscribers.txt", "a") as f:
        f.write(email + "\n")
    return render_template("thankyou.html", email=email)




if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

