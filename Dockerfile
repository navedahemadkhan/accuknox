# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port 8000
EXPOSE 5001

# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "networknox.wsgi:application"]

