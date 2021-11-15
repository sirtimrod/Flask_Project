# Start with a base image
FROM python:3-onbuild
# Copy our application code
WORKDIR /usr/src/app
COPY requirements.txt ./
# Fetch app specific dependencies
RUN pip install -r requirements.txt
EXPOSE 5000