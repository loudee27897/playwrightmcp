FROM mcr.microsoft.com/playwright:v1.41.1-focal

RUN apt update && apt install -y python3-pip xvfb
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt && playwright install
ENV DISPLAY=:99
CMD ["bash", "-c", "Xvfb :99 -screen 0 1280x720x24 & python3 server.py"]
