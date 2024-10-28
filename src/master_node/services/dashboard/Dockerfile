FROM debian:bookworm-slim

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "asgi.py"]