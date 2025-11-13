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
    /res
ume     - Will list the contents

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
Semester: 6 (SCGPA: 10 | CGPA: 9.9)
Email: priyanshu17ks@gmail.com
Phone: (91) 93923 81422
Location: Pune, Maharashtra, India - 411047

Overview:
I am a B.Tech candidate specializing in Cloud Technology and Information Security. My expertise includes cloud computing, cybersecurity, DevOps, and quantum computing, with hands-on experience in AWS, Azure, Docker, Terraform, and security frameworks. I have contributed to research, internships, and open-source projects in secure cloud architectures, serverless computing, and advanced security implementations.

Technical Skills:
- Programming: Java, Python, Dart, SQL, Shell Scripting
- Web: HTML, CSS, Tailwind CSS, JavaScript, Node.js, Express, EJS
- DevOps: Git/GitHub, Terraform, Pulumi, GitLab, Redis, Docker
- CS Fundamentals: DSA, DBMS
- Cloud: AWS, Azure, GCP

Languages: English, Hindi, Gujarati
    """)

async def experience(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Experience:

1. Marquardt India Pvt. Ltd., Pune — Web Dev Intern (June 2025–Present)
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

1. Storage SaaS Platform
   - AI-powered SaaS for automated business solutions (Next.js, Tailwind CSS, Prisma, Neon DB, Clerk, Cloudinary, Vercel)

2. Quantum Cloud Integration
   - Hybrid cloud-quantum system (AWS, IBM Quantum, Docker, Python)

3. SkyVault
   - Personal cloud storage with Docker, Flask, Bcrypt, HTML, CSS

4. Ecobizz: An E-commerce App
   - Flutter/Dart, iOS & Android, sustainable products

5. Li-Fi Tech
   - IoT device for message passing using light (Research, hardware)
        """)

async def skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Technical Skills:
- Programming: Java, Python, Dart, SQL, Shell Scripting
- Web: HTML, CSS, Tailwind CSS, JavaScript, Node.js, Express, EJS
- DevOps: Git/GitHub, Terraform, Pulumi, GitLab, Redis, Docker
- CS Fundamentals: DSA, DBMS
- Cloud: AWS, Azure, GCP
- Languages: English, Hindi, Gujarati
        """)

async def awards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Awards & Certifications:

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
Email: priyanshu17ks@gmail.com
Phone: (91) 93923 81422
Location: Pune, Maharashtra, India - 411047
    """)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said {update.message.text}, This is not accepted, please try other command:(. Start with /resume")

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
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
