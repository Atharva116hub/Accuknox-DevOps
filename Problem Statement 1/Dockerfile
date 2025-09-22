FROM python:3.9-slim
RUN apt-get update && apt-get install -y cowsay fortune netcat-openbsd && rm -rf /var/lib/apt/lists/*
COPY wisecow.sh /wisecow.sh
RUN chmod +x /wisecow.sh
EXPOSE 4499
CMD ["./wisecow.sh"]
