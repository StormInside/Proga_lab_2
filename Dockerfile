FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "./run_Flask.py" ]
