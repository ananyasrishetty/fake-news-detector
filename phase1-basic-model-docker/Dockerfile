# Dockerfile

# Use an official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app code to container
COPY ./app /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Start the server
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]