# Use Python 3.12
FROM python:3.12

# Set working directory
WORKDIR /opt/flask_scorepredictor

# Copy all files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
