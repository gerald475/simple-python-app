from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, my name is Gerald. What is your name?"

@app.route('/greet', methods=['POST'])
def greet():
    user_name = request.form.get('name', 'Guest')
    return f"Hello {user_name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
