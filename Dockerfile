FROM python:alpine

COPY . /app

WORKDIR /app

ENTRYPOINT ["python3", "test.py"]
CMD ["add", "2", "2"]