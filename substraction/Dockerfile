# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the contents of ./app/requirements.txt to /app/requirements.txt
COPY ./app/requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN apk add --update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/*

# Copy the contents of the ./app to /app folder
COPY ./app /app

# Run the command python app.py
CMD ["python", "app.py"]