from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Check if both username and password
        if username == "admin" and password == "1234":
            message = "Login successful for user : " + username
            success = True
        else:
            message = "Login failed for user : " + username
            success = False

        # Write the message to the log file
        with open("login.log", "a") as file:
            file.write(message + "\n")

        # Send login result to the browser
        return jsonify({
            "success": success,
            "message": message
        })

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)