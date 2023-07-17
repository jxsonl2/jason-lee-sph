FROM python:3.9.6-slim-buster
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY response.py response.py
COPY sample-url.csv sample-url.csv
CMD [ "python3", "response.py" ]