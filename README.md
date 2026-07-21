<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=230&section=header&text=NIKHIL%20MANOJ%20PATIL&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=AI%2FML%20Engineer%20%7C%20Agentic%20AI%20%C2%B7%20RAG%20%C2%B7%20Computer%20Vision&descAlignY=55&descSize=17&fontAlign=50" width="100%"/>

<a href="https://www.linkedin.com/in/nikhil-patil-2013a0282/">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="mailto:nikhilpatil9263@gmail.com">
  <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>
<a href="https://github.com/NikhilPatil9263">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>



</div>

<br/>

### 👨‍💻 About Me

I'm a final-year **AI/ML engineering student** focused on building systems that go beyond experimentation — from model training to deployment in real, constrained environments. My work spans **Agentic AI (LangGraph)**, **Scalable RAG pipelines**, **Computer Vision**, and **cloud/serverless architecture on AWS**.

I care about the full lifecycle of a project: training a model, orchestrating multi-agent reasoning, and deploying it behind a working service — rather than stopping at a notebook or a proof of concept.

- 🎯 **Focus areas:** Multi-agent LLM orchestration, retrieval-augmented generation, computer vision for edge devices, and serverless cloud systems
- 🏗️ **Approach:** End-to-end ownership — data pipeline, model training, backend API, cloud infrastructure, and deployment
- 📊 **Selected results:** 79% mAP50 on a custom 5,000-image dataset · repository-scale code reviews in under 3 minutes across 13-language codebases
- 🎓 B.Tech, Artificial Intelligence & Machine Learning — R.C. Patel Institute of Technology (2023–Present)
- 📍 Dhule, Maharashtra, India · Open to AI/ML and Agentic AI internships and roles

<br/>

## Tech Stack

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/YOLOv8-111F68?style=for-the-badge"/>
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-FF6F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>

</div>

<br/>

## Featured Projects

<br/>

<table width="100%">
<tr>
<td width="100%">

### 🤖 CodeSensei — Multi-Agent AI Code Review System
**[→ View Repository](https://github.com/NikhilPatil9263/codesensei)**

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square"/> <img src="https://img.shields.io/badge/ChromaDB-FF6F00?style=flat-square"/> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>

A 5-agent LangGraph pipeline that reviews an entire GitHub repository autonomously — bug detection, architecture analysis, quality scoring, and report synthesis — designed to work around the context-window limits that constrain single-agent code review at scale.

**Results:** Tested end-to-end on real production codebases, including catching a security flaw in `Rich` (56K LOC) with an exact line-level fix, and identifying 12 bugs in `Flask` (67K LOC), with review times under 3 minutes.

- ⚡ Embeds 800+ code chunks per repo into ChromaDB, holding per-query LLM context to ~1,500 tokens across 150-file, 13-language codebases
- 🚀 60–170s end-to-end latency at repository scale, benchmarked on real open-source projects

</td>
</tr>
</table>

<br/>

<table width="100%">
<tr>
<td width="100%">

### 🛡️ Autonomous Military Surveillance System
**[→ View Repository](https://github.com/NikhilPatil9263/AI-based-Smart-Military-Surveillance-Integrating-With-IOT)**

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/YOLOv8-111F68?style=flat-square"/> <img src="https://img.shields.io/badge/ByteTrack-000000?style=flat-square"/> <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white"/> <img src="https://img.shields.io/badge/Raspberry%20Pi-A22846?style=flat-square&logo=raspberrypi&logoColor=white"/>

A closed-loop, autonomous threat-detection pipeline, trained from scratch and deployed on Raspberry Pi under real field conditions.

**Results:** Zone intrusion triggers detection, a GSM SMS alert, and a servo-actuated barrier, with no manual intervention required during operation.

- 🎯 Trained YOLOv8s from scratch on a custom-annotated 5,000-image, 4-class dataset — **79% mAP50** at **~0.6s inference** on-device
- 🔁 Replaced DeepSORT with ByteTrack to eliminate identity-switching during occlusion, improving tracking reliability under real-world conditions

</td>
</tr>
</table>

<br/>

<table width="100%">
<tr>
<td width="100%">

### ☁️ AI Citizen Complaint Management System (AWS Serverless)
**[→ View Repository](https://github.com/NikhilPatil9263/aws-ai-citizen-complaint-management-system)**

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/AWS%20Lambda-FF9900?style=flat-square&logo=awslambda&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon%20S3-569A31?style=flat-square&logo=amazons3&logoColor=white"/> <img src="https://img.shields.io/badge/DynamoDB-4053D6?style=flat-square&logo=amazondynamodb&logoColor=white"/> <img src="https://img.shields.io/badge/API%20Gateway-FF4F8B?style=flat-square"/>

A serverless civic-issue reporting system where citizens submit an image and description, and the system classifies the complaint automatically using Amazon Rekognition before routing it to an admin dashboard.

- Fully serverless architecture: S3 for image storage, Lambda for backend logic, API Gateway for REST endpoints, and DynamoDB for persistence
- AI-based image classification via Amazon Rekognition, removing the need for manual complaint categorization
- Admin dashboard supports status tracking from submission through resolution

</td>
</tr>
</table>

<br/>

<div align="center">

📁 **More cloud projects:** [aws-automated-cost-optimizer](https://github.com/NikhilPatil9263/aws-automated-cost-optimizer) · [aws-resource-provisioning-tool](https://github.com/NikhilPatil9263/aws-resource-provisioning-tool) · [aws-static-website-automation](https://github.com/NikhilPatil9263/aws-static-website-automation) · [aws-lamp-student-management-system](https://github.com/NikhilPatil9263/aws-lamp-student-management-system) · [attendance-ci-cd](https://github.com/NikhilPatil9263/attendance-ci-cd)

</div>

<br/>

## GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=NikhilPatil9263&show_icons=true&theme=tokyonight&hide_border=true&count_private=true"/>
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=NikhilPatil9263&layout=compact&theme=tokyonight&hide_border=true"/>

</div>

<br/>

## Areas of Strength

<div align="center">

| 🧩 Full-cycle development | 🏎️ Real-world deployment | 📐 Measurable outcomes |
|:---:|:---:|:---:|
| Training, orchestration, and deployment, not just experimentation | Projects tested against real repositories or deployed on physical hardware | 79% mAP50 · 800+ chunks/repo · 60–170s review time · 0.6s edge inference |

</div>

<br/>

## Let's Connect

<div align="center">

Open to opportunities in **AI/ML Engineering, Agentic AI, and Applied ML**. Happy to discuss multi-agent systems, RAG pipelines, or deployment challenges.

<a href="https://www.linkedin.com/in/nikhil-patil-2013a0282/">
  <img src="https://img.shields.io/badge/Connect%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>
<a href="mailto:nikhilpatil9263@gmail.com">
  <img src="https://img.shields.io/badge/Say%20Hello-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
</a>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>
