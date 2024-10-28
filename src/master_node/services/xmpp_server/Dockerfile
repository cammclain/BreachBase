FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y prosody

COPY . /app

WORKDIR /app