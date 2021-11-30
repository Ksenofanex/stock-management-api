# Python version.
FROM python:3.7

# To prevent package installation errors.
RUN apt-get update
RUN apt-get install build-essential

# To disable .pyc files.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory.
WORKDIR /code

# Copy project to inside of Docker container.
COPY . /code/

# Upgrade pip and install dependencies.
RUN pip install --upgrade pip && pip install -r requirements.txt
