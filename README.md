# Pranav Sutar — 3D Interactive Portfolio

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pranav_Sutar-0d9488?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pranav-sutar/)
[![GitHub](https://img.shields.io/badge/GitHub-pranavsutar-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pranavsutar)
[![Role](https://img.shields.io/badge/Role-AI_&_Data_Engineer-059669?style=for-the-badge&logo=python&logoColor=white)](https://github.com/pranavsutar)
[![Education](https://img.shields.io/badge/IIT_Tirupati-B.Tech_CSE_8.81_CGPA-2dd4bf?style=for-the-badge&logo=academic&logoColor=black)](https://github.com/pranavsutar)

An interactive 3D portfolio website for **Pranav Sutar** — **AI and Data Engineer** at **ZS Associates**, and **B.Tech CSE graduate from IIT Tirupati**.

---

## 🌟 About Me

- **CSE Graduate from IIT Tirupati** (2020 – 2024, **CGPA: 8.81 / 10.0**).
- **Data Engineer at ZS Associates** (June 2024 – Present, Pune, India) working on clinical data anomaly-detection pipelines (LOF, Isolation Forest, COPOD), internal issue-tracking tools (Power Apps, Databricks), and GxP-compliant data ingestion (REST APIs, AWS S3, DocumentDB).
- **Winner — GEP Techathon 2023** for building SalesVision (multi-model sales forecasting web dashboard).
- **Grand Finalist — Smart India Hackathon 2022** and **3rd Place — Intra IIT Ideathon**.
- Strong academic foundation and personal exploration across classical machine learning, computer vision, NLP, and LLM prompt chaining.

---

## 🛠️ Technical Skills

| Domain | Technologies & Frameworks |
| :--- | :--- |
| **Data Engineering & Cloud** | Azure Databricks, AWS S3, Amazon DocumentDB, Amazon Redshift, ETL Pipelines, Data Ingestion, REST API Integration, MySQL, MongoDB |
| **Machine Learning & AI** | scikit-learn, PyTorch, Anomaly Detection (LOF, Isolation Forest, COPOD), PCA, OpenCV, Regression Models, Object Detection (YOLO, Faster R-CNN), LangChain, LLM APIs (Gemini, Grok) |
| **Programming Languages** | Python, SQL, C++, JavaScript, TypeScript, Java, Shell |
| **App Development & Tools** | React, Flask, MERN Stack, Angular, Power Apps, Power Automate, Streamlit, Pandas, NumPy, Git, Linux |

---

## 🚀 Featured Projects

### 1. [LangChain Sanskrit Chhanda / Metric Poetry](https://sanskrit-metric-poetry.streamlit.app/)
**Stack:** Python, LangChain, Gemini API, Grok API, Streamlit, Prompt Chaining
- Personal exploration using LLMs to generate Sanskrit verses and iteratively improve alignment with target metre (chhanda).
- Implemented prompt chaining: when generated text fails metre checks, detailed validator reports are looped back to the LLM for iterative refinement.
- Built a deterministic Sanskrit prosody parser for syllable weight (Laghu/Guru) analysis and deployed an interactive demo on Streamlit.

### 2. [SalesVision – ML Forecasting Dashboard](https://github.com/pranavsutar/TechathonSalesVision)
**Stack:** MongoDB, Express, React, Node.js, Flask, Python, Regression Models
- Interactive sales forecasting dashboard awarded **1st Place in GEP Techathon 2023**.
- Implemented multiple regression-based forecasting models supporting daily, weekly, and monthly forecasting granularities.
- Built dynamic React charting interfaces for multi-model comparison across historical sales data.

### 3. [Sniff CSV – Data Quality Analyzer](https://github.com/pranavsutar/tool_dev)
**Stack:** Python, Flask, React, Data Profiling & Quality
- Modular web tool detecting 10+ data-quality anomalies in CSV datasets using rule-based and statistical checks.
- Generates automated Python refactoring scripts and downloadable data health reports.
- Provides interactive visual summaries through a Flask + React interface.

### 4. Object Detection Model Benchmarking
**Stack:** PyTorch, YOLO, Faster R-CNN, Computer Vision
- B.Tech thesis project under Prof. Kalidas at IIT Tirupati, benchmarking object-detection models to explore lighter architectures.
- Explored architectural decoupling between classifier and bounding-box regression heads.
- Conducted extensive research review on detection efficiency, feature pyramid networks, and inference latency.

### 5. [Jan Dhan Darshak – Utility Locator App](https://github.com/devella1/RS1079/)
**Stack:** Android Studio, Java, Geolocation, Voice Search
- Contributed feature enhancements to an Android utility locator app helping citizens find nearby financial touchpoints.
- Implemented voice search functionality, custom-radius geolocation filters, and dynamic dataset upload capabilities.

---

## 💼 Professional Experience

- **Data Engineer** — **ZS Associates** *(June 2024 – Present | Pune, India)*
  - Worked on an anomaly-detection pipeline for clinical datasets using Local Outlier Factor (LOF), Isolation Forest, and COPOD, applying PCA for dimensionality reduction.
  - Designed and developed an internal issue-tracking tool utilizing Power Apps and Azure Databricks, delivering a reported reduction in debugging turnaround time of ~40%.
  - Built GxP-compliant data-ingestion pipelines integrating REST APIs with AWS S3 and Amazon DocumentDB.
  - Integrated Databricks jobs and APIs with Power Automate and user-facing Power Apps workflows.
- **SDE Intern** — **GEP Worldwide** *(May 2023 – Jul 2023 | Mumbai, India)*
  - Resolved 14+ UI and accessibility issues across Angular components, enhancing usability and accessibility compliance including for visually impaired users.
  - Worked in an enterprise engineering environment using Angular 8, TypeScript, HTML, CSS, CI/CD, and Linux.

---

## 🌐 3D Portfolio Features

- **Interactive 3D Isometric Room**: Built with Three.js and WebGL rendering, featuring an interactive developer workstation.
- **Scroll-Linked Camera Choreography**: Smoothly navigates through room perspectives in sync with section scrolling.
- **Cyber Jade & Obsidian Emerald Theme**: Curated dual palette:
  - **Light Mode**: Crisp mint backdrop (`#f8fafc`), deep slate typography (`#0f172a`), and rich teal-emerald accents (`#0d9488`, `#059669`).
  - **Dark Mode**: Obsidian jade abyss background (`#080d11`) and glowing electric cyan-mint accents (`#2dd4bf`, `#34d399`).
- **Floating Side Menu Navbar**: Frosted glass drawer (`backdrop-filter: blur(28px)`) that slides out cleanly on demand.
- **Full Mobile Responsiveness**: Fluid clamp typography, touch-optimized card layouts, and responsive action buttons.

---

## 💻 Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pranavsutar/pranavsutar.git
   cd pranavsutar
   ```

2. **Run locally:**
   ```bash
   # Option 1: Python HTTP server
   python serve.py
   
   # Option 2: Windows batch launcher
   run_portfolio.bat
   ```
   Open `http://localhost:3000` in your browser.

3. **Recompile content:**
   Edit `portfolio.config.json` to update content, then recompile:
   ```bash
   python update_content.py
   ```
