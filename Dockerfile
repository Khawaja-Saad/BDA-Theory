# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make shell script executable
RUN chmod +x start.sh

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Start the backend and frontend
CMD ["./start.sh"]
