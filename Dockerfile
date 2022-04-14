# Using Python Slim-Buster
FROM kyyex/kyy-userbot:busterv2
#━━━━━ Userbot Telegram ━━━━
#━━━━━ By Kyy-Userbot ━━━━━ 
#━━━━━ By Kyuraa-Userbot ━━━━━

RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y
RUN git clone -b Warpath-Userbot https://github.com/Kyuraxp/warpath-userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Kyuraxp/warpath-userbot/Warpath-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
