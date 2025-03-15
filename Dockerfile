# Use an official Python runtime as a parent image
FROM python:3.11.11-slim

RUN apt update -y && apt install awscli -y

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip insatll --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# Run app.py when the container launches
CMD ["python", "app.py"]