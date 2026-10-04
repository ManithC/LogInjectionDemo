from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST": # make sure get data after clicking login

        username = request.form["username"]
        password = request.form["password"]

        # Check if both username and password are entered
        if username and password:
            message = "Login successful for user : " + username
        else:
            message = "Login unsuccessful"

        # Write the message to the log file
        with open("login.log", "a") as file:
            file.write(message + "\n")

        return message

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)