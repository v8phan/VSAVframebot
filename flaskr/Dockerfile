# dockerfile, Image, Container
# 'docker build -t VSAVbot' to build image
# 'docker run VSAVbot' to run
# must rebuild docker image whenever you make changes
FROM python:3
FROM gorialis/discord.py

RUN mkdir -p /usr/src/bot
COPY requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR /usr/src/bot

COPY . .
CMD [ "python3", "bot.py" ]