# syntax=docker/dockerfile:1
FROM ubuntu

## Set environment variable to prevent buffering of Python's standard output
ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE 1
#
## Update package lists and install wget
RUN apt-get update && apt-get install -y  \
    apt-utils  \
    netcat \
    vim  \
    curl  \
    apache2  \
    apache2-utils \
    python3  \
    libapache2-mod-wsgi-py3
#
## Create a symlink for Python 3 if it doesn't exist
RUN ln -s /usr/bin/python3 /usr/bin/python || true
#
RUN apt-get -y install python3-pip
#
## Create a symlink for pip3 to pip if it doesn't exist
RUN ln -s /usr/bin/pip3 /usr/bin/pip || true
#
##Clean up
RUN rm -rf /var/lib/apt/lists/*
###########################################################################
#FROM python:3.11-alpine
#
#ENV PYTHONUNBUFFERED 1
#
#ENV PYTHONDONTWRITEBYTECODE 1
#
#RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
#
## Upgrade pip inside the virtual environment
#RUN pip install --upgrade pip
###########################################################################
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
# Set the working directory
WORKDIR /var/www/html

RUN chmod 700 /var/www/html
# Copy your project files
COPY social_balance  .

# Copy Apache configuration
COPY site-config.conf /etc/apache2/sites-available/000-default.conf

## Expose ports and start Apache
#EXPOSE 8000
EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]