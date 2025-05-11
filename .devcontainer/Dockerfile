FROM mcr.microsoft.com/playwright:v1.41.1-focal

RUN apt update && apt install -y \
    python3-pip \
    xvfb \
    libwoff1 libopus0 libwebpdemux2 libharfbuzz-icu0 libwebpmux3 \
    libenchant-2-2 libhyphen0 libegl1 libglx0 libgudev-1.0-0 \
    libevdev2 libgles2 libx264-dev

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt && playwright install

ENV DISPLAY=:99
CMD ["bash", "-c", "Xvfb :99 -screen 0 1280x720x24 & python3 server.py"]
