# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run the iris_classifier.py when the container launches
CMD ["python", "iris_classifier.py"]

