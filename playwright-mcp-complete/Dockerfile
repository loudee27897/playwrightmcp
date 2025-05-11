# Base image with Playwright and browser support
FROM mcr.microsoft.com/playwright:v1.41.1-focal

# Install system dependencies for WebKit, Chromium, and Firefox GUI support
RUN apt update && apt install -y \
    python3-pip \
    xvfb \
    libwoff1 libopus0 libwebpdemux2 libharfbuzz-icu0 libwebpmux3 \
    libenchant-2-2 libhyphen0 libegl1 libglx0 libgudev-1.0-0 \
    libevdev2 libgles2 libx264-dev

# Set working directory and copy all files
WORKDIR /app
COPY . .

# Install Python packages and Playwright drivers
RUN pip3 install --no-cache-dir -r requirements.txt && \
    playwright install

# Set default environment variable
ENV DISPLAY=:99

# Make sure run.sh is executable
RUN chmod +x /app/run.sh

# Entry point to start the server
CMD ["/app/run.sh"]
