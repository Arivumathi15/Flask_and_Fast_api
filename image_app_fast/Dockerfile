FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt into the container and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 for the FastAPI application
EXPOSE 5000

# Command to run the FastAPI application when the container starts
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["python3", "main.py"]