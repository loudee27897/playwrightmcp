# 🧠 Playwright MCP Server (Complete)

A fully functional MCP (Model-Controlled Protocol) server built with **Flask** and **Playwright**, designed for AI agents like **Gemini**, **Flowise**, or **LangChain** to perform browser automation via simple HTTP APIs.

Supports full GUI automation using `Xvfb`, with automatic screenshot capture and direct access to DOM events via Playwright.

---

## ✅ Features

- `POST /tool/goto` – Navigate to a webpage  
- `POST /tool/click` – Click an element using a CSS selector  
- `POST /tool/type` – Fill input fields with text  
- `GET  /screenshot` – Download or view the latest screenshot

---

## ⚙️ Setup Options

### 🅰️ Manual Setup (Local, Codespaces, or Cloud VM)

```bash
pip install flask playwright
playwright install
Xvfb :99 -screen 0 1280x720x24 &
export DISPLAY=:99
python3 server.py
```

### 🅱️ Docker (Recommended)

```bash
docker build -t playwright-mcp .
docker run -p 5000:5000 playwright-mcp
```

---

## 🚀 Quick Start Script

To launch everything in one step:

```bash
./run.sh
```

> Starts `Xvfb`, sets `DISPLAY`, and runs your Flask MCP server.

---

## 🌐 API Usage Examples

### `POST /tool/goto`

```bash
curl -X POST http://localhost:5000/tool/goto \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

### `POST /tool/click`

```bash
curl -X POST http://localhost:5000/tool/click \
  -H "Content-Type: application/json" \
  -d '{"selector": "#submit"}'
```

### `POST /tool/type`

```bash
curl -X POST http://localhost:5000/tool/type \
  -H "Content-Type: application/json" \
  -d '{"selector": "#email", "text": "test@example.com"}'
```

### `GET /screenshot`

Open in browser:

```
http://localhost:5000/screenshot
```

---

## 📁 Project Structure

```
/workspaces/playwrightmcp/
├── server.py             # Flask + Playwright API
├── run.sh                # Startup script for Xvfb + Flask
├── Dockerfile            # Container-ready with system libs
├── requirements.txt      # Python dependencies
├── .env                  # DISPLAY config for headless GUI
├── .vscode/              # Debug + interpreter settings
├── .devcontainer/        # Codespaces config
└── README.md             # You’re reading this 📖
```

---

## 🤖 Use Case Scenarios

| Agent Type     | Integration |
|----------------|-------------|
| **Gemini / Bard** | Use `/tool/goto` + `/tool/type` for smart form submission |
| **LangChain**     | Wrap HTTP tools to auto-click or extract page state |
| **Flowise**       | Use as a browser-action node via REST |
| **Human QA**      | Run this in VNC + Codespaces for exploratory testing |

---

## 🛠 Tips

- Use `headless=False` in `server.py` for interactive debugging
- Restart `run.sh` if GUI automation stops
- Works in Codespaces, Oracle Cloud, Docker, or bare Ubuntu

---

## 🧠 Credits

Built for AI-first automation workflows with minimal setup.  
Inspired by browser agents like **AutoGPT**, **SWE-agent**, and **Gemini Pro + Playwright**.

---

## 📝 License

MIT License — use it freely, improve it aggressively.
