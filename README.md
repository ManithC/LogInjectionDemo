# How to run log injection application

This guide covers on how to run the log injection application on ubuntu environment using terminal.
Do not change the name of the files they should be "validate.py" and "login.html".

## 1. Install Python and flask

Open Terminal and run:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Check that Python is available:

```bash
python3 --version
```

Install flask
```bash
python3 -m pip install Flask
```

## 2. Check the project structure

Place the files in the following structure. The `templates` folder name must be exactly `templates` because Flask looks there for `login.html` by default.

```text
log-injection/
├── app_security.log
├── login.log
├── validate.py
├── Unvalidate.py
└── templates/
    └── login.html
```

## 3. Start the application

To run the system with input validation
```bash
python validate.py
```

When Flask starts, the terminal should display a local address similar to:

```text
Running on http://127.0.0.1:4000
```

Keep this terminal open while using the application.

To run application with unvalidated inputs

```bash
python unvalidate.py
```
When flask starts, the terminal should display a local address similar to
```text
Running on http://127.0.0.1:5000
```
keep this terminal open while using the application
## 4. Open the application

Open Firefox or another browser **inside Ubuntu** and visit:

```text
http://127.0.0.1:4000
```

Enter a username and submit the form. With the current validation rules, usernames may contain letters, numbers, underscores (`_`), periods (`.`), and hyphens (`-`). Other characters, including `@`, and input containing carriage-return or newline characters should be rejected and shown in the page's notification bar.

Examples:

- Valid format: `john_123`
- Invalid format: `john@123`

## 5. Check the security log

The application `validate.py` creates a log called `app_security.log` 

The application `unvalidate.py` creates a log called `login.log`

accordig the code you are running you can check the log files

Expected behavior:

- A valid username creates an `INFO` entry.
- An invalid username creates a `WARNING` entry such as `Invalid Username`.
- The invalid username is rejected before it reaches the normal username-logging statement.

## 6. Stop the application

Return to the terminal running Flask and press:

```text
Ctrl+C
```
