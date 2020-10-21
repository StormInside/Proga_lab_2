FROM alpine
RUN apk add --update python3 py-pip
RUN pip3 install flask
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["run_Flask.py"]