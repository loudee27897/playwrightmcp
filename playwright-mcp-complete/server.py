from flask import Flask, request, jsonify, send_file
from playwright.sync_api import sync_playwright
import os

app = Flask(__name__)
browser = None
page = None

@app.route("/tool/goto", methods=["POST"])
def goto():
    global browser, page
    data = request.get_json()
    url = data.get("url")
    if not url or not url.startswith("http"):
        return jsonify({"error": "Invalid URL"}), 400

    os.environ["DISPLAY"] = ":99"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path="screenshot.png")
        return jsonify({"status": "navigated", "screenshot": "/screenshot"})

@app.route("/tool/click", methods=["POST"])
def click():
    global page
    data = request.get_json()
    selector = data.get("selector")
    if not page or not selector:
        return jsonify({"error": "Page not initialized or selector missing"}), 400
    page.click(selector)
    page.screenshot(path="clicked.png")
    return jsonify({"status": "clicked", "screenshot": "/screenshot"})

@app.route("/tool/type", methods=["POST"])
def type_text():
    global page
    data = request.get_json()
    selector = data.get("selector")
    text = data.get("text")
    if not page or not selector or text is None:
        return jsonify({"error": "Missing page, selector, or text"}), 400
    page.fill(selector, text)
    page.screenshot(path="typed.png")
    return jsonify({"status": "typed", "screenshot": "/screenshot"})

@app.route("/screenshot")
def screenshot():
    image_path = "typed.png" if os.path.exists("typed.png") else \
                 "clicked.png" if os.path.exists("clicked.png") else \
                 "screenshot.png"
    if not os.path.exists(image_path):
        return jsonify({"error": "No screenshot available"}), 404
    return send_file(image_path, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
