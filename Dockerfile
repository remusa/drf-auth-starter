# Dockerfile

# Pull base image
FROM python:3.8-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install psycopg2
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2 \
  && apk del build-deps

# Install dependencies
COPY Pipfile* /code/
RUN pip install --upgrade pip \
  && pip install pipenv \
  && pipenv install --system

# Copy project
COPY . /code/

# Collect static files
# RUN python manage.py collectstatic --noinput

# Add and run as non-root user
RUN adduser -D myuser
USER myuser

# Run gunicorn
CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT
