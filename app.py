import os
import platform
import random
import sys
import time
from datetime import datetime
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Collection of programming jokes and motivational quotes
JOKES_AND_QUOTES = [
    {
        "type": "joke",
        "category": "Programming Joke",
        "content": "Why do programmers prefer dark mode?",
        "punchline": "Because light attracts bugs!",
        "author": "Dev Wisdom"
    },
    {
        "type": "joke",
        "category": "Programming Joke",
        "content": "There are 10 types of people in the world:",
        "punchline": "Those who understand binary, and those who don't.",
        "author": "Binary Humor"
    },
    {
        "type": "joke",
        "category": "Programming Joke",
        "content": "Why did the JavaScript developer wear glasses?",
        "punchline": "Because they don't C#!",
        "author": "Frontend Fun"
    },
    {
        "type": "quote",
        "category": "Motivational Quote",
        "content": "First, solve the problem. Then, write the code.",
        "author": "John Johnson"
    },
    {
        "type": "quote",
        "category": "Motivational Quote",
        "content": "Experience is the name everyone gives to their mistakes.",
        "author": "Oscar Wilde"
    },
    {
        "type": "quote",
        "category": "Motivational Quote",
        "content": "Code is like humor. When you have to explain it, it’s bad.",
        "author": "Cory House"
    },
    {
        "type": "joke",
        "category": "Programming Joke",
        "content": "A SQL query walks into a bar, walks up to two tables and asks...",
        "punchline": "'Can I join you?'",
        "author": "Database Humour"
    },
    {
        "type": "quote",
        "category": "Motivational Quote",
        "content": "Simplicity is prerequisite for reliability.",
        "author": "Edsger W. Dijkstra"
    },
    {
        "type": "joke",
        "category": "Programming Joke",
        "content": "How many programmers does it take to change a lightbulb?",
        "punchline": "None, that's a hardware problem!",
        "author": "Tech Support"
    },
    {
        "type": "quote",
        "category": "Motivational Quote",
        "content": "Make it work, make it right, make it fast.",
        "author": "Kent Beck"
    },
    {
        "type": "joke",
        "category": "Programming Joke",
        "content": "Why was the developer unhappy with their job?",
        "punchline": "Because they didn't get arrays!",
        "author": "Code Humor"
    },
    {
        "type": "quote",
        "category": "Motivational Quote",
        "content": "The best error message is the one that never shows up.",
        "author": "Thomas Fuchs"
    }
]


def get_wsl_ubuntu_details():
    """Extract Ubuntu OS distribution details and WSL info."""
    details = {
        "pretty_name": "Ubuntu Linux",
        "version_id": "Unknown",
        "version_codename": "Unknown",
        "ubuntu_codename": "Unknown",
        "kernel": platform.release(),
        "architecture": platform.machine(),
        "hostname": platform.node(),
        "is_wsl": False,
        "wsl_version": "WSL2",
        "python_version": sys.version.split()[0]
    }

    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release", "r") as f:
            for line in f:
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    key, val = line.split("=", 1)
                    val = val.strip('"\'')
                    if key == "PRETTY_NAME":
                        details["pretty_name"] = val
                    elif key == "VERSION_ID":
                        details["version_id"] = val
                    elif key == "VERSION_CODENAME":
                        details["version_codename"] = val
                    elif key == "UBUNTU_CODENAME":
                        details["ubuntu_codename"] = val

    if os.path.exists("/proc/version"):
        with open("/proc/version", "r") as f:
            proc_ver = f.read()
            if "WSL" in proc_ver or "microsoft" in proc_ver.lower():
                details["is_wsl"] = True
                if "WSL2" in proc_ver or "microsoft-standard-WSL2" in proc_ver:
                    details["wsl_version"] = "WSL2"
                else:
                    details["wsl_version"] = "WSL"

    if os.path.exists("/proc/uptime"):
        try:
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                hours, remainder = divmod(int(uptime_seconds), 3600)
                minutes, seconds = divmod(remainder, 60)
                days, hours = divmod(hours, 24)

                parts = []
                if days > 0:
                    parts.append(f"{days}d")
                if hours > 0:
                    parts.append(f"{hours}h")
                parts.append(f"{minutes}m {seconds}s")
                details["uptime"] = " ".join(parts)
        except Exception:
            details["uptime"] = "N/A"
    else:
        details["uptime"] = "N/A"

    return details


@app.route("/")
def index():
    os_info = get_wsl_ubuntu_details()
    item = random.choice(JOKES_AND_QUOTES)
    return render_template("index.html", os_info=os_info, item=item)


@app.route("/api/quote")
def api_quote():
    item = random.choice(JOKES_AND_QUOTES)
    return jsonify(item)


@app.route("/api/time")
def api_time():
    now = datetime.now()
    return jsonify({
        "time": now.strftime("%H:%M:%S"),
        "date": now.strftime("%A, %B %d, %Y"),
        "iso": now.isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
