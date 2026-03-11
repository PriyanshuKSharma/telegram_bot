# AI-Powered Pull Request Code Review Workflow

<p align="center">

<img src="https://raw.githubusercontent.com/n8n-io/n8n/master/assets/n8n-logo.png" width="120"/>
<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="120"/>
<img src="https://groq.com/wp-content/uploads/2024/03/groq-logo.svg" width="120"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Sheets_2020_Logo.svg/768px-Google_Sheets_2020_Logo.svg.png" width="120"/>

</p>

---

# 📌 Overview

This project implements an **AI-powered automated Pull Request review system** using **n8n workflow automation, GitHub API, and Groq LLM models**.

Whenever a developer creates or updates a Pull Request, the workflow automatically:

1️⃣ Detects the Pull Request event from GitHub
2️⃣ Fetches the modified files and diffs
3️⃣ Converts the diffs into an AI prompt
4️⃣ Sends the prompt to a Large Language Model
5️⃣ Generates intelligent code review comments
6️⃣ Posts the review automatically on the Pull Request
7️⃣ Labels the PR as **ReviewedByAI(n8n)**

This workflow helps **improve code quality, reduce manual reviews, and accelerate development pipelines**.

---

# 🧠 Core Technologies

| Tool              | Purpose                                |
| ----------------- | -------------------------------------- |
| **n8n**           | Workflow automation platform           |
| **GitHub API**    | Retrieves PR diffs and posts comments  |
| **Groq LLM**      | Runs the AI model for code review      |
| **LLaMA 3.1**     | Language model used for analysis       |
| **Google Sheets** | Stores coding guidelines for reference |

---

# 🏗 Workflow Architecture

```
Developer Creates Pull Request
            │
            ▼
     GitHub Trigger
            │
            ▼
    Fetch PR File Diffs
            │
            ▼
   Generate Prompt from Diffs
            │
            ▼
      AI Code Review Agent
            │
            ▼
      Groq LLM Model
            │
            ▼
   Generate Code Review Comments
            │
            ▼
   Post Comment to Pull Request
            │
            ▼
 Add "ReviewedByAI(n8n)" Label
```

---

# ⚙ Workflow Components

## 1️⃣ GitHub Trigger

The workflow begins with a **GitHub Trigger node** that listens for Pull Request events.

### Trigger Conditions

```
Event: pull_request
Repository: PriyanshuKSharma/multi-cloud
```

### Function

* Detects when a PR is created or updated
* Sends the payload to the next node in the workflow

---

# 🌐 2️⃣ Fetch Pull Request File Diffs

This step retrieves all modified files from the Pull Request.

### Node Used

```
HTTP Request Node
```

### GitHub API Endpoint

```
https://api.github.com/repos/{{$json.body.sender.login}}/{{$json.body.repository.name}}/pulls/{{$json.body.number}}/files
```

### Returned Data

The API response includes:

| Field     | Description                |
| --------- | -------------------------- |
| filename  | Modified file name         |
| patch     | Code diff                  |
| status    | Added / Modified / Deleted |
| additions | Number of added lines      |
| deletions | Number of removed lines    |

This data is required to allow the AI to analyze **actual code changes**.

---

# 🧾 3️⃣ Create Prompt From PR Diffs

A **JavaScript Code Node** processes the retrieved file diffs.

### Responsibilities

* Parse all changed files
* Extract code patches
* Format them into readable diff blocks
* Build a structured AI prompt

### Example Generated Prompt

```
You are a senior Python developer working on a Telegram bot.

Please review the following code changes.

Your mission:

- Review the proposed code changes
- Generate inline comments
- Ignore files without patches
- Do not repeat code snippets
```

This structured prompt helps the AI generate **professional developer-style reviews**.

---

# 🤖 4️⃣ AI Code Review Agent

The **n8n LangChain Agent** acts as the intelligent reviewer.

### Responsibilities

* Understand code diffs
* Detect coding issues
* Suggest improvements
* Generate meaningful developer comments

It acts like an **automated senior developer reviewing the PR**.

---

# ⚡ 5️⃣ Groq LLM Integration

The workflow uses the **Groq Chat Model node**.

### Model Used

```
llama-3.1-8b-instant
```

### Why Groq?

Groq provides:

* ⚡ Ultra-low latency
* 🧠 High-performance inference
* 🔁 Real-time responses

This allows the workflow to **review Pull Requests instantly**.

---

# 📊 6️⃣ Google Sheets Integration (Optional)

The workflow can optionally reference **coding standards stored in Google Sheets**.

Example guidelines stored in the sheet:

| Rule              | Description                             |
| ----------------- | --------------------------------------- |
| Naming Convention | Use snake_case for Python variables     |
| Logging           | Every API endpoint must include logging |
| Error Handling    | Avoid bare except blocks                |
| Security          | Validate all user inputs                |

The AI agent can use these guidelines when generating reviews.

---

# 💬 7️⃣ Post Review Comment to GitHub

After generating the review, the workflow posts the AI output to the Pull Request.

### GitHub Node Operation

```
Resource: review
Event: comment
```

### Result

The Pull Request will automatically receive an AI-generated review comment.

Example:

```
⚠ Potential issue: Missing exception handling in the API request.

Suggestion:
Add try/except block to avoid application crashes.
```

---

# 🏷 8️⃣ Add Label to Pull Request

After posting the comment, the workflow automatically adds a label.

### Label

```
ReviewedByAI(n8n)
```

### Benefits

* Indicates the PR was reviewed by automation
* Helps teams track AI-reviewed PRs
* Improves project visibility

---

# 🔄 End-to-End Workflow Example

1️⃣ Developer submits a Pull Request
2️⃣ GitHub sends a webhook event
3️⃣ n8n workflow starts automatically
4️⃣ GitHub API retrieves modified files
5️⃣ Code Node converts diffs into prompt
6️⃣ Groq LLM analyzes the code
7️⃣ AI generates review comments
8️⃣ GitHub node posts the review
9️⃣ Label **ReviewedByAI(n8n)** is added

---

# 🚀 Benefits of This System

✔ Automated code reviews
✔ Faster developer feedback
✔ Reduced manual review workload
✔ Consistent coding standards
✔ AI-assisted development pipeline
✔ Improves DevOps automation

---

# 🔮 Future Improvements

Potential enhancements for this workflow:

* 🔐 Security vulnerability detection
* 🧪 Automatic test coverage review
* 📉 Code complexity analysis
* 🔔 Slack / Discord notifications
* 🧾 Review history database
* 🌍 Multi-language support

---

# 📂 Repository

GitHub Repository

```
https://github.com/PriyanshuKSharma/multi-cloud
```

---

# 👨‍💻 Author

**Priyanshu Kumar Sharma**

Cloud & AI Systems Enthusiast
Research Experience: **IIT Ropar (Cloud Computing Research)**
Interested in **Multi-Cloud Systems, DevOps Automation, and AI-Driven Development Tools**

---

⭐ If you find this workflow useful, feel free to **fork the repository and contribute!**
