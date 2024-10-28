FROM debian:bullseye-slim

RUN apt-get update && apt-get install -y curl wget

# Install the step-cli
RUN wget https://dl.smallstep.com/cli/docs-ca-install/latest/step-cli_amd64.deb
RUN dpkg -i step-cli_amd64.deb

# Install the step-ca
RUN wget https://dl.smallstep.com/certificates/docs-ca-install/latest/step-ca_amd64.deb
RUN dpkg -i step-ca_amd64.deb

COPY config/smallstep_ca.json /etc/step-ca/config/ca.json

CMD ["step-ca", "/etc/step-ca/config/ca.json"]