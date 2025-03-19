# Use Python official image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install -r requirements.txt

# Run Flask app
CMD ["python", "app.py"]
