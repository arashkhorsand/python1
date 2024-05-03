# Stage 1: Build stage
# Use an official Python image as the base image
FROM python:3.8-slim as builder

# Set the working directory in the container
WORKDIR /app

# Copy only the files needed for pip install
COPY requirements.txt .

# Install Flask (no need for a requirements.txt file if you're only using Flask)
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Run stage
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /usr/local /usr/local
COPY . .

# Inform Docker that the container is listening on port 5000
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
