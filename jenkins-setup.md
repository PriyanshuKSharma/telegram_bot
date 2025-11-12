# Jenkins CI/CD Setup for Telegram Bot

## Prerequisites

1. **Jenkins Installation**
   ```bash
   # Install Jenkins on Ubuntu
   wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
   sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
   sudo apt update
   sudo apt install jenkins
   ```

2. **Required Jenkins Plugins**
   - Docker Pipeline
   - Git
   - Pipeline
   - Blue Ocean (optional)

## Jenkins Configuration

### 1. Create New Pipeline Job
1. Open Jenkins dashboard
2. Click "New Item"
3. Enter job name: `telegram-bot-pipeline`
4. Select "Pipeline"
5. Click "OK"

### 2. Configure Pipeline
1. In "Pipeline" section, select "Pipeline script from SCM"
2. SCM: Git
3. Repository URL: Your Git repository URL
4. Branch: `*/main`
5. Script Path: `Jenkinsfile`

### 3. Add Docker Hub Credentials
1. Go to "Manage Jenkins" > "Manage Credentials"
2. Add new "Username with password" credential
3. ID: `docker-hub-credentials`
4. Username: Your Docker Hub username
5. Password: Your Docker Hub password

### 4. Environment Variables
Add these in Jenkins job configuration:
- `DOCKER_REGISTRY`: Your Docker registry URL
- `TOKEN`: Your Telegram bot token (as secret)

## Pipeline Stages

1. **Checkout**: Gets code from repository
2. **Setup Python Environment**: Creates virtual environment
3. **Run Tests**: Validates Python syntax
4. **Build Docker Image**: Creates Docker image
5. **Push to Registry**: Pushes to Docker Hub (main branch only)
6. **Deploy**: Deploys container (main branch only)

## Manual Deployment

```bash
# Using docker-compose
docker-compose up -d --build

# Using deployment script
./.jenkins/deploy.sh
```

## Webhook Setup (Optional)

1. In GitHub/GitLab, go to repository settings
2. Add webhook: `http://your-jenkins-url/github-webhook/`
3. Select "Push events"
4. This will trigger builds automatically on code push