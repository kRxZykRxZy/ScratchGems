from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

# Load user balances from a JSON file
def load_balances():
    try:
        with open("user_balances.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

user_balances = load_balances()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/user", methods=["GET"])
def get_balance():
    username = request.args.get("username", "guest")
    balance = user_balances.get(username, 0)  # Default to 0 if user not found
    return jsonify({"user": username, "balance": balance})

if __name__ == "__main__":
    app.run(debug=True)
