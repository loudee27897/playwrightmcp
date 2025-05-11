#!/bin/bash

# Start virtual display for GUI automation
Xvfb :99 -screen 0 1280x720x24 &
export DISPLAY=:99

# Start the Flask Playwright MCP server
python3 server.py
