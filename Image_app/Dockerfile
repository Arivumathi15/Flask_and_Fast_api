FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask application
EXPOSE 5000

# Command to run the Flask application when the container starts
CMD ["python", "image_flask.py"]
