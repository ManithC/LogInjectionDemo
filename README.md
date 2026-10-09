# How to run log injection application

This guide covers on how to run the log injection application on ubuntu environment using terminal.
Do not change the name of the files they should be "validate.py" and "login.html".

## 1. Install Python and virtual-environment tools

Open Terminal and run:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

Check that Python is available:

```bash
python3 --version
```

## 2. Check the project structure

Place the files in the following structure. The `templates` folder name must be exactly `templates` because Flask looks there for `login.html` by default.

```text
log-injection/
├── validate.py
└── templates/
    └── login.html
```

If you are transferring the project from another computer, copy the files into a folder on Ubuntu, then open that folder in Terminal. For example:

```bash
cd ~/log-injection
```

Replace `~/log-injection` with the actual location of your project.

## 3. Create and activate a virtual environment

From the project folder, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

When the environment is active, the terminal prompt will usually show `(.venv)`.

## 4. Install Flask

With the virtual environment activated, run:

```bash
python -m pip install --upgrade pip
python -m pip install Flask
```

You only need to install Flask once in this virtual environment.

## 5. Start the application

Make sure the virtual environment is still active and that the terminal is in the same folder as `validate.py`. Run:

```bash
python validate.py
```

When Flask starts, the terminal should display a local address similar to:

```text
Running on http://127.0.0.1:4000
```

Keep this terminal open while using the application. The server is running as long as the process remains active.

## 6. Open the application

Open Firefox or another browser **inside Ubuntu** and visit:

```text
http://127.0.0.1:4000
```

Enter a username and submit the form. With the current validation rules, usernames may contain letters, numbers, underscores (`_`), periods (`.`), and hyphens (`-`). Other characters, including `@`, and input containing carriage-return or newline characters should be rejected and shown in the page's notification bar.

Examples:

- Valid format: `john_123`
- Invalid format: `john@123`

## 7. Check the security log

The application creates `app_security.log` in the directory from which you launched `validate.py`. To view the log in another terminal, navigate to the project folder and run:

open the app_security.log file which contains the log entries. if there is no such a file this will be created automatically


Expected behavior:

- A valid username creates an `INFO` entry.
- An invalid username creates a `WARNING` entry such as `Invalid Username`.
- The invalid username is rejected before it reaches the normal username-logging statement.

## 8. Stop the application

Return to the terminal running Flask and press:

```text
Ctrl+C
```
