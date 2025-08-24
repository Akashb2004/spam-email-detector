from flask import Flask, render_template, request

app = Flask(__name__)

# Simple rule-based spam detection (for demo)
def check_spam(email_text):
    spam_keywords = ["winner", "prize", "lottery", "congratulations", "bank", "urgent", "click here"]
    email_lower = email_text.lower()
    if any(word in email_lower for word in spam_keywords):
        return "❌ Spam"
    else:
        return "✅ Not Spam"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['emailText']
    result = check_spam(email_text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
