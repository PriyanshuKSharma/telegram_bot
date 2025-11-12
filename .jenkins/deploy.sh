#!/bin/bash

# Deployment script for Jenkins
set -e

echo "Starting deployment..."

# Stop existing container
docker-compose down || true

# Build and start new container
docker-compose up -d --build

# Check if container is running
if docker-compose ps | grep -q "Up"; then
    echo "Deployment successful!"
else
    echo "Deployment failed!"
    exit 1
fi