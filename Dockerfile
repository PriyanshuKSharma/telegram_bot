# Use Python 3.9 image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy script and dependencies
COPY tele-bot.py .
COPY requirement.txt .


# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Run the script
CMD ["python", "tele-bot.py"]
