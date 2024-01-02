# Use python:3-alpine as base image
FROM python:3-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to /app
COPY requirements.txt /app

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the app.py file to /app
COPY app.py /app

# Expose port 5000
EXPOSE 5000

# Run the app.py file as the entrypoint
ENTRYPOINT ["python", "app.py"]