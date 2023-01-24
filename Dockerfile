FROM python:3.9

RUN apt-get update && apt-get install -y iputils-ping
RUN apt-get update && apt-get install -y curl
RUN echo "deb http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu bionic main" >> /etc/apt/sources.list.d/firefox.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE49EC21 && \
    apt-get update && \
    apt-get install -y firefox

# Add your dependencies
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# Run the bot
CMD ["python3", "main.py"]