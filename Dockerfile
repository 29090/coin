FROM python:3.12-slim
WORKDIR /coin
COPY . .
CMD [ "python3", "main.py"]