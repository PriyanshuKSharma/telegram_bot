# AI-Powered Pull Request Review Automation

### Automated Code Review System using n8n, GitHub & Google Gemini

---

## Executive Summary

This workflow implements an automated AI-driven Pull Request review system using n8n orchestration, GitHub webhooks, and Google Gemini 2.5 Pro.

The system:

* Triggers on new Pull Requests
* Fetches modified files and diffs
* Constructs a structured AI prompt
* Generates contextual code review feedback
* Posts review comments automatically
* Labels the Pull Request for traceability

This solution enhances review efficiency, enforces coding standards, and reduces manual review overhead.

---

# Tools & Technologies Used

## n8n – Workflow Orchestration Engine

![Image](https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/N8n-logo-new.svg/1280px-N8n-logo-new.svg.png)

![Image](https://community.n8n.io/uploads/default/original/2X/a/a5f04bbc83726ca2c4edd7a8b38daa4328625f84.png)

![Image](https://n8niostorageaccount.blob.core.windows.net/n8nio-strapi-blobs-prod/assets/Agent_chat_818315ae64.webp)

![Image](https://community.n8n.io/uploads/default/original/3X/f/2/f2ca7ddb9f52ce8490e84991990c3b133de494d9.jpeg)

n8n is used as the core automation engine. It:

* Listens for GitHub Pull Request events
* Orchestrates API calls
* Transforms data via Code nodes
* Connects to the AI model
* Posts review results back to GitHub

---

## GitHub – Repository & Webhook Source

![Image](https://cdn-icons-png.flaticon.com/256/25/25231.png)

![Image](https://docs.github.com/assets/cb-87213/images/help/pull_requests/pull-request-review-edit-branch.png)

![Image](https://cm.magefan.com/mf_webp/png/media/archive/add-webhook-in-github.webp)

![Image](https://assets.website-files.com/61d6b61c7084bb1d721a21aa/64f82dd49eb303b99d236514_5JRB0R6uJGzD6vPYJN2kfYTGr2vAHrZww2MTDvbQOw-4dL--uHUoJzLHetvsJRrGfbBK9jE3U-NtscELZCmH8xGn9kP1DKsjMpDiys2gXgh8uURqi1ehUEbqaL0cdKKmuqkcVp6-SuqeeYovAp4n04M.png)

GitHub provides:

* Pull Request event triggers
* Repository diff access via REST API
* Review comment publishing
* Label management

The workflow uses GitHub OAuth2 authentication to securely access repository data.

---

## Google Gemini 2.5 Pro – AI Code Review Engine

![Image](https://images.openai.com/static-rsc-3/VURonqa_PGti1jtz9Ooe_IU5TzIsh_NGEMIAUkVf93aioXSzFhVK0ek8IHpAh-fxb7CvoO8HWXtrw2igglSEQmUHqxiaD0IVnCosJaViGtU?purpose=fullsize\&v=1)

![Image](https://images.indianexpress.com/2025/08/Google-AI-Studio-Tutorial.jpg)

![Image](https://images.ctfassets.net/lzny33ho1g45/3fyCJYJeBJPc6ksXWSJsz0/7f48fc185b0c29b68634f6bc417cce0b/gemini-api-image7.png)

![Image](https://raw.githubusercontent.com/gemini-api-php/client/main/assets/example.png)

Google Gemini 2.5 Pro is used as the Large Language Model responsible for:

* Understanding code diffs
* Context-aware analysis
* Generating structured inline feedback
* Producing concise and technical reviews

The integration is handled via the n8n LangChain Agent node.

---

## Google Sheets (Optional) – Coding Standards Reference

![Image](https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Google_Sheets_logo_%282014-2020%29.svg/500px-Google_Sheets_logo_%282014-2020%29.svg.png)

![Image](https://codelabs.developers.google.com/static/codelabs/sheets-api/img/6e4b8c5ba82c473b.png)

![Image](https://images.ctfassets.net/mrsnpomeucef/257vl6kO9hXjX5CVzkQj9m/9b165cbd287eb10685ed333e55f047f8/R__9_.png)

![Image](https://images.ctfassets.net/lzny33ho1g45/3urOHYTPb2mZCVe63uZafY/4377e8f0616ccf86c39d52db0d76936e/google-sheets-tutorial-image26.png)

Google Sheets can optionally store:

* Team coding standards
* Naming conventions
* Security policies
* Performance guidelines

The AI agent can reference this sheet for opinionated and team-aligned reviews.

---

# System Architecture

```
GitHub Pull Request Event
        │
        ▼
GitHub Trigger (n8n)
        │
        ▼
Fetch PR Diffs (GitHub REST API)
        │
        ▼
Prompt Engineering (Code Node)
        │
        ▼
Google Gemini 2.5 Pro
        │
        ▼
Post Review Comment
        │
        ▼
Add Label to PR
```

---

# Implementation Guide (n8n Configuration)

---

## 1. GitHub Trigger Node

### Objective

Initiates workflow execution when a Pull Request event occurs.

### Configuration

* Authentication: OAuth2
* Owner: PriyanshuKSharma
* Repository: telegram_bot
* Event: pull_request

After saving and activating the workflow, n8n automatically registers a webhook inside GitHub.

---

## 2. HTTP Request Node – Fetch PR Diffs

### Objective

Retrieve changed files and patch diffs from the Pull Request.

### Method

GET

```
=https://api.github.com/repos/{{$json.body.sender.login}}/{{$json.body.repository.name}}/pulls/{{$json.body.number}}/files
```

### Output Includes

* Filename
* Patch (diff)
* Change status
* Metadata

This provides the AI with full contextual information for accurate review.

---

## 3. Code Node – Prompt Engineering

### Objective

Convert GitHub diff data into a structured AI instruction prompt.

### Processing Logic

* Iterates through modified files
* Extracts file.patch
* Escapes triple backticks
* Wraps changes inside diff blocks
* Constructs structured instructions

### AI Instructions Embedded

The model is instructed to:

* Act as a senior Python developer
* Review file-by-file
* Generate inline comments
* Ignore binary files
* Avoid repeating code
* Provide concise, actionable feedback

This ensures high-quality and deterministic output.

---

## 4. AI Agent – Code Review Engine

Node Type: `@n8n/n8n-nodes-langchain.agent`

### Configuration

* Prompt Type: Define
* Input:

  ```
  {{$json.user_message}}
  ```

Connected Language Model: Google Gemini 2.5 Pro

This structured agent ensures controlled and task-focused AI reasoning.

---

## 5. GitHub Review Poster Node

### Objective

Publish AI-generated review as a Pull Request comment.

### Configuration

* Resource: review
* Operation: comment
* Pull Request Number:

  ```
  {{$('PR Trigger').first().json.body.number}}
  ```
* Body:

  ```
  {{$json.output}}
  ```

This posts the structured AI review directly inside the PR discussion.

---

## 6. PR Label Automation

### Objective

Tag Pull Requests after AI review is completed.

Label added:

```
ReviewedByAI(n8n)
```

This improves traceability and visibility within the repository.

---

# Credential Setup Guide

---

## GitHub OAuth2 Setup

1. Go to GitHub → Developer Settings
2. Create a new OAuth App
3. Set callback URL from n8n
4. Add credentials in n8n

Required scopes:

* repo
* read:org

---

## Google Gemini API Setup

1. Go to Google AI Studio
2. Generate API key
3. Add credential in n8n (Google Palm API type)

---

## Google Sheets OAuth2 (Optional)

1. Enable Google Sheets API
2. Configure OAuth consent screen
3. Add OAuth2 credentials in n8n

---

# AI Review Strategy

This system applies:

* File-level diff segmentation
* Context-preserving prompt engineering
* Structured review generation
* Inline actionable comments
* Non-redundant output

The design avoids:

* Repeating code snippets
* Reviewing binary files
* Producing overly verbose feedback

---

# Security Best Practices

* Never commit credentials to version control
* Use environment variables in self-hosted setups
* Restrict GitHub OAuth scopes
* Monitor API rate limits
* Secure n8n instance with authentication

---

# Scalability Roadmap

Future enhancements may include:

* Slack or Microsoft Teams notifications
* Severity classification (Critical / Warning / Info)
* Automatic PR approval for low-risk changes
* Persistent review logging in a database
* Multi-repository deployment

---

# Deployment Instructions

1. Import the workflow JSON into n8n
2. Configure required credentials
3. Activate the workflow
4. Create a Pull Request
5. Observe automated AI review generation

---

# Conclusion

This AI-driven Pull Request Review system demonstrates:

* Workflow orchestration expertise
* Advanced prompt engineering
* Practical LLM integration
* DevOps automation capability
* Scalable engineering design

It is suitable for modern development teams seeking automated, consistent, and scalable code review processes.

---

This is strong automation architecture work.
