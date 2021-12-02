# Python image version and variant.
FROM python:3.7-alpine

# To prevent package installation errors.
RUN apk update && apk add python3-dev

# To disable .pyc files.
ENV PYTHONDONTWRITEBYTECODE 1
# To show outputs in terminal in real time, with no buffering.
ENV PYTHONUNBUFFERED 1

# Set work directory.
WORKDIR /code

# Copy project to inside of Docker container.
COPY . /code/

# Upgrade pip and install dependencies.
RUN pip install --upgrade pip && pip install -r requirements.txt
