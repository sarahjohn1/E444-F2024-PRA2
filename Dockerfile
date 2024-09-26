# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container to /app which is the root directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install all packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=hello.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]


# docker run -d -p 5000:5000 flask-app
# or on docker desktop in the containers