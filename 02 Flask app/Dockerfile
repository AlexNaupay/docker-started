FROM python:3.12-alpine3.17

# Establece el directorio de trabajo dentro del contenedor.
# Las instrucciones siguientes se ejecutarán en este directorio:
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# From . to WORKDIR
COPY . .

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]

# ENV FLASK_APP=app.py
# CMD ["flask", "run", "--host=0.0.0.0"]

# docker build -t flaskapp:latest .
# docker run --name flaskapp --rm -d -p 8090:5000 flaskapp:latest