# Playwright MCP Server (Complete)

A full MCP-style server powered by Playwright and Flask. Supports GUI browser automation with screenshot capture, and integrates with Gemini, Flowise, or any LLM agent.

---

## ✅ Features

- `/tool/goto` — Navigate to a webpage
- `/tool/click` — Click an element by selector
- `/tool/type` — Fill text into an input field
- `/screenshot` — View the latest screenshot

---

## ⚙️ Setup (for Codespaces, Oracle Cloud, Local, or Docker)

### Option A: Manual Terminal Setup

```bash
pip install flask playwright
playwright install
Xvfb :99 -screen 0 1280x720x24 &
export DISPLAY=:99
python3 server.py
```

### Option B: Docker

```bash
docker build -t playwright-mcp .
docker run -p 5000:5000 playwright-mcp
```

---

## 🌐 API Examples

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
Open: http://localhost:5000/screenshot
