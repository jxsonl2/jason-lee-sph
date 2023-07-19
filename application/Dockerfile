FROM python:3.9.6-slim-buster
COPY . .
RUN chmod 0644 crontab
RUN chmod 0744 response.py
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y cron
RUN crontab crontab
CMD ["cron", "-f"]