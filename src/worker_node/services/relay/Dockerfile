FROM debian:bookworm-slim

COPY . /app


WORKDIR /app

RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]