FROM python:3.10-alpine

RUN apk update && apk add --no-cache build-base python3-dev postgresql-dev

RUN mkdir /app

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml /app/

RUN poetry install

COPY . /app/

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}
ENV DEBUG=True
ENV ALLOWED_HOSTS=127.0.0.1,localhost
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]


