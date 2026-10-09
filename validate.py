from flask import Flask, request, render_template, abort, jsonify
import logging
import re

app = Flask(__name__)

security_logger = logging.getLogger('security')
security_logger.setLevel(logging.INFO)

file_handler=logging.FileHandler("app_security.log")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)
security_logger.addHandler(file_handler)

security_logger.propagate = False

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        raw_username = request.form.get('username', '')

        if not re.match(r"^[a-zA-Z0-9_.-]+$", raw_username):
            security_logger.warning("Invalid Username")

            return jsonify({"success": False, "message": "Invalid Username"}),400

        safe_username = raw_username.replace("\n",'').replace('\r','')

        security_logger.info("Recorded Username: %s", safe_username)
        return jsonify({"success": True, "username": safe_username})
    return render_template("login.html")
if __name__ == '__main__':
    app.run(port=4000,debug=True)