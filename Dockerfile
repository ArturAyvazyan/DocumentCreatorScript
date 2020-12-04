FROM python:latest

WORKDIR /usr/local/bin

COPY tuta.py 

CMD ["tuta.py", "-OPTIONAL_FLAG"]