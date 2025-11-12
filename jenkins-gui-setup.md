# Jenkins GUI Setup - Execute Shell Commands

## Create Freestyle Project

1. **New Item**
   - Click "New Item"
   - Enter name: `telegram-bot-freestyle`
   - Select "Freestyle project"
   - Click "OK"

## Source Code Management
- Select "Git"
- Repository URL: `https://github.com/PriyanshuKSharma/telegram_bot.git`
- Branch: `*/main`

## Build Triggers
- Check "GitHub hook trigger for GITScm polling" (for webhook)
- Or check "Poll SCM" with schedule: `H/5 * * * *` (every 5 minutes)

## Build Environment
- Check "Delete workspace before build starts"

## Build Steps

### Step 1: Setup Python Environment
**Execute shell:**
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirement.txt
```

### Step 2: Run Tests
**Execute shell:**
```bash
. venv/bin/activate
python -m py_compile tele-bot.py
echo "Python syntax check passed"
```

### Step 3: Build Docker Image
**Execute shell:**
```bash
docker build -t priyanshuksharma/telegram_bot:${BUILD_NUMBER} .
docker tag priyanshuksharma/telegram_bot:${BUILD_NUMBER} priyanshuksharma/telegram_bot:latest
echo "Docker image built successfully"
```

### Step 4: Push to Docker Hub
**Execute shell:**
```bash
echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin
docker push priyanshuksharma/telegram_bot:${BUILD_NUMBER}
docker push priyanshuksharma/telegram_bot:latest
echo "Images pushed to Docker Hub"
```

### Step 5: Deploy Application
**Execute shell:**
```bash
docker stop telegram-bot || true
docker rm telegram-bot || true
docker run -d --name telegram-bot --env-file .env priyanshuksharma/telegram_bot:latest
echo "Application deployed successfully"
```

## Environment Variables
In "Build Environment" section:
- Check "Use secret text(s) or file(s)"
- Add:
  - `DOCKER_HUB_USERNAME` (your Docker Hub username)
  - `DOCKER_HUB_PASSWORD` (your Docker Hub password)
  - `TOKEN` (your Telegram bot token)

## Post-build Actions
- Add "Archive the artifacts": `*.log`
- Add "Publish JUnit test result report" (if you add tests later)

## Complete Execute Shell Script (All-in-One)
```bash
#!/bin/bash
set -e

echo "=== Starting CI/CD Pipeline ==="

# Setup Python Environment
echo "Setting up Python environment..."
python3 -m venv venv
. venv/bin/activate
pip install -r requirement.txt

# Run Tests
echo "Running tests..."
python -m py_compile tele-bot.py
echo "✓ Python syntax check passed"

# Build Docker Image
echo "Building Docker image..."
docker build -t priyanshuksharma/telegram_bot:${BUILD_NUMBER} .
docker tag priyanshuksharma/telegram_bot:${BUILD_NUMBER} priyanshuksharma/telegram_bot:latest
echo "✓ Docker image built successfully"

# Push to Docker Hub
echo "Pushing to Docker Hub..."
echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin
docker push priyanshuksharma/telegram_bot:${BUILD_NUMBER}
docker push priyanshuksharma/telegram_bot:latest
echo "✓ Images pushed to Docker Hub"

# Deploy Application
echo "Deploying application..."
docker stop telegram-bot || true
docker rm telegram-bot || true
docker run -d --name telegram-bot --env-file .env priyanshuksharma/telegram_bot:latest

# Verify deployment
if docker ps | grep -q telegram-bot; then
    echo "✓ Application deployed successfully"
else
    echo "✗ Deployment failed"
    exit 1
fi

echo "=== Pipeline completed successfully ==="
```