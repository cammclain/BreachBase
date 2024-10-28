FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y tor nginx

COPY torrc /etc/tor/torrc

COPY entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]