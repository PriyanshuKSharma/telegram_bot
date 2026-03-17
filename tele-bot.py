import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Load .env only if running locally (not in Docker)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not available in Docker

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Namaste!! You are welcome to my resume bot. To start type: /resume")

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
Hi There! I'm Telegram bot created by Priyanshu K Sharma. Please follow these commands:
    /start      - Start a conversation
    /content    - About Priyanshu K Sharma
    /contact    - Contact information
    /experience - Professional experience
    /projects   - Projects
    /skills     - Technical skills
    /awards     - Awards & Certifications
    /roles      - Leadership & Club Roles
    /resume     - Will list the contents

Aasha hai isse aapki sahayta hogi!! :)
I hope this will help you!! :)
        """
    )

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Name: Priyanshu Kumar Sharma
Degree: B.Tech in Information Technology
Specialization: Cloud Technology and Information Security
University: Ajeenkya D Y Patil University, Pune
Semester: 8 (SCGPA: 9.9 | CGPA: 9.9)
Email: priyanshu17ks@gmail.com
Phone: (91) 93923 81422
Location: Pune, Maharashtra, India - 411047

Overview:
I am a B.Tech candidate specializing in Cloud Technology and Information Security. My expertise includes cloud computing, cybersecurity, DevOps, and quantum computing, with hands-on experience in AWS, Azure, Docker, Terraform, and security frameworks. I have contributed to research, internships, and open-source projects in secure cloud architectures, serverless computing, and advanced security implementations.

Technical Skills:
- Programming: Java, Python, Dart, SQL, Shell Scripting
- Web: HTML, CSS, Tailwind CSS, JavaScript, Node.js, Express, EJS
- DevOps: Git/GitHub, Terraform, Pulumi, GitLab, Redis, Docker, Jenkins, Kubernetes
- CS Fundamentals: DSA, DBMS, OS, CN
- Cloud: Amazon Web Services, MS Azure, Google Cloud Platform
- AI & ML Tools:  ML Fundamentals, Generative AI, Prompt Engineering, AI Workflow Design, MLFlow

Languages: English, Hindi, Gujarati
    """)

async def experience(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Experience:

1. Marquardt India Pvt. Ltd., Pune — Web Dev Intern (June 2025–September 2025)
   - Frontend development, UI/UX, full-stack features, responsive web interfaces (HTML5, CSS3, JS, EJS, MySQL, Express.js)
   - Unit testing, debugging, performance tuning, automation, dashboard maintenance

2. Seamless Education and Services (Seamedu) Pvt. Ltd., Pune — IT Intern–Placement Coordinator (Mar 2025–June 2025)
   - IT infrastructure, software tools, process optimization, placement activities, technical reports, digital collaboration

3. Indian Institute of Technology Ropar, Punjab — Cloud Research Intern (May 2024–July 2024)
   - Research on distributed/serverless computing, XFBench/XFaaS, serverless deployments, performance profiling
        """)

async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Projects:

1. Multi-Cloud SaaS Orchestration Platform:
    - Built and deployed a cloud-native multi-cloud orchestration platform with containerized microservices using Docker and infrastructure provisioning via Terraform. Implemented automated background jobs with Celery and Redis for periodic synchronization of cloud resource data from AWS, Azure, and GCP APIs. Designed CI/CD-friendly architecture and production-ready deployments with secure JWT authentication, PostgreSQL-backed services, and scalable FastAPI backend. This project highlights practical experience in infrastructure automation, containerization, service orchestration, and operational reliability.

2. Storage SaaS Platform
   - Built a Software-as-a-Service (SaaS) platform leveraging AI to provide automated business solutions for modern video management. The platform utilizes a robust tech stack, including Next.js 14 for the frontend framework, TypeScript and JavaScript for application logic, and Tailwind CSS for responsive styling. For secure user authentication, it integrates Clerk, while Prisma ORM with Neon DB (PostgreSQL) manages the database. Cloudinary is used for scalable video storage and optimized delivery, and the platform is deployed seamlessly on Vercel. AI is harnessed to automate business workflows and enhance video-related operations, creating an efficient, scalable, and user-friendly solution.

3. Quantum Cloud Integration
   - Developed a hybrid cloud-quantum system that seamlessly integrates classical cloud computing with quantum processing to achieve enhanced computational efficiency. The workflow enables interoperability between traditional cloud services and quantum systems, providing secure and scalable solutions. This hybrid architecture is implemented using AWS for cloud infrastructure, IBM Quantum for quantum resources, and Docker for containerization, ensuring flexible deployment and robust integration across platforms.

4. Rural Gyan Platform
   - Developed a comprehensive full-stack educational management system featuring role-based dashboards, integrated AI-powered tools, and bilingual (English/Hindi) support. The platform offers streamlined admin, teacher, and student workflows, including live virtual classes, automated quiz grading, real-time analytics, AI-assisted tutoring, and activity monitoring. The tech stack includes React.js and Tailwind CSS for the frontend, Node.js, Express.js, and Socket.io for the backend, and MongoDB for data storage. Secure authentication is implemented using JWT, with AI functionalities powered by OpenAI API and TensorFlow.js. Translation is enabled via the Google Cloud Translate API, and the system is deployed using Docker and Nginx for scalability and reliability.

5. XAI Interpret
    - Developed XAI Interpret, a hands-on platform for model interpretability that implements state-of-the-art Explainable AI (XAI) techniques using SHAP and LIME. The project provides a complete machine learning pipeline, from data preprocessing and model training to real-time, interactive explanations for individual predictions. Supporting various ML algorithms, the system helps users understand both global and local model behavior, feature interactions, and produces rich visualizations for interpretability. Built for practical use, it’s compatible with Google Colab and supports cloud deployment on Vertex AI, featuring production-ready model persistence, scalable architecture, and comprehensive LaTeX documentation. This solution fosters transparency and trust in machine learning models, making it especially valuable for black-box medical diagnostics and other high-stakes domains.
    
6. SkyVault
   - Built a personal cloud storage system using Docker containers, featuring an interactive user interface for seamless file management. The platform supports file uploading, listing, and downloading functionalities, while Dockerized deployment ensures easy scalability. Secure authentication mechanisms and robust data storage practices safeguard user data, making the system both efficient and secure for personal cloud storage needs

7. Ecobizz: An E-commerce App
   - Cross-platform mobile application built with Flutter SDK for sustainable products marketplace, running on both iOS and Android devices.

        """)

async def skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Technical Skills:
- Programming: Java, Python, Dart, SQL, Shell Scripting
- Web: HTML, CSS, Tailwind CSS, JavaScript, Node.js, Express, EJS
- DevOps: Git/GitHub, Terraform, Pulumi, GitLab, Redis, Docker, Jenkins, Kubernetes
- CS Fundamentals: DSA, DBMS, OS, CN
- Cloud: Amazon Web Services, MS Azure, Google Cloud Platform
- AI & ML Tools:  ML Fundamentals, Generative AI, Prompt Engineering, AI Workflow Design, MLFlow
- Languages: English, Hindi, Gujarati
        """)

async def awards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Awards & Certifications:

- IBM ICE Day Ideathon: 3rd Place (2025)
- Seamedu Awards 2025: Creative Cloud Integration Award
- SOF International Mathematics Olympiad: School Rank 3rd (2019)
- Hackathons: ADYPU Problem-A-Thon, Sharda Tech-a-thon, Smart India Hackathon, NASA Space App Challenge, UNESCO-MIL 2023, Google Solution Challenge 2024, Hackron 2025
- Certifications: Fortinet Certified Fundamentals & Associate in Cybersecurity, Zscaler Fundamentals & Zero Trust Certified Associate
        """)

async def roles(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Leadership & Club Roles:

- Vice President | Matheletes — Maths Club (Mar 2023–Jul 2024)
  - Founding member, quiz formats, event planning, digital tools
- Core Member | Happier and Safer Internet Club (Cyber Security Awareness) (Oct 2023–Oct 2024)
  - Founding member, UNESCO MIL 2023, debates, awareness camps
        """)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
LinkedIn: https://www.linkedin.com/in/priyanshu-kumar-sharma-333800251/
GitHub: https://github.com/PriyanshuKSharma
DockerHub: https://hub.docker.com/u/priyanshuksharma
Portfolio: https://priyanshuksharma.github.io/portfolio_priyanshuksharma/
Hackerrank: https://www.hackerrank.com/profile/priyanshu17ks
X(twitter): https://x.com/itspriyanshuks
Email: priyanshu17ks@gmail.com
Phone: (91) 93923 81422
Location: Pune, Maharashtra, India - 411047
    """)

async def hackathon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Hackathons:
- ADYPU Problem-A-Thon
- Sharda Tech-a-thon
- Smart India Hackathon
- NASA Space App Challenge
- UNESCO-MIL 2023
- Google Solution Challenge 2024
- Hackron 2025
        """)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said {update.message.text}, This is not accepted, please try other command:(. Start with /resume")

async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
    My Portfolio Website: https://priyanshuksharma.github.io/portfolio_priyanshuksharma/
    """)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("resume", resume))
    app.add_handler(CommandHandler("content", content))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("experience", experience))
    app.add_handler(CommandHandler("projects", projects))
    app.add_handler(CommandHandler("skills", skills))
    app.add_handler(CommandHandler("awards", awards))
    app.add_handler(CommandHandler("roles", roles))
    app.add_handler(CommandHandler("hackathon", hackathon))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
