FROM python:latest
LABEL Maintaner="Maycon Moreira"
COPY . /var/www
WORKDIR /var/www
RUN python3 -m pip install --upgrade pip && \
pip install -r requirements.txt
ENTRYPOINT python3 main.py
EXPOSE 5000