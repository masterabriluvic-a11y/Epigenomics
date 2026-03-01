FROM python:3.12-slim

LABEL maintainer="masterabriluvic-a11y <masterabriluvic@gmail.com>" \
      version="1.0" \
      description="Docker image for seqClass DNA/RNA classifier"

WORKDIR /app

COPY seqClass.py /usr/local/bin/seqClass.py

RUN chmod +x /usr/local/bin/seqClass.py

ENV PATH="/usr/local/bin:${PATH}"

CMD ["bash"]


