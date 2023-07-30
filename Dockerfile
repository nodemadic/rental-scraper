# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Sets the working directory in the docker image
WORKDIR /app

# Copying requirements to the docker image
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copying the source code to the working directory
COPY . .

# This command will run when the container starts
CMD ["python3", "-m", "scraper.py"]
