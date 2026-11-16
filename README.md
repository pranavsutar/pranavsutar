# Pratik Modi — 3D Interactive Portfolio

[![Live Portfolio](https://img.shields.io/badge/Live_Portfolio-pratikmodi22.github.io-2563eb?style=for-the-badge&logo=googlechrome&logoColor=white)](https://pratikmodi22.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pratik_Modi-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pratik-modi-11ba02283)
[![GitHub](https://img.shields.io/badge/GitHub-PratikModi22-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PratikModi22)
[![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://github.com/PratikModi22)
[![Azure](https://img.shields.io/badge/Azure-Cloud_Data-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)](https://github.com/PratikModi22)

An interactive 3D portfolio website for **Pratik Modi** — **Data Engineer** specializing in **PySpark, Databricks, Azure, and Medallion Architecture Data Warehousing**.

---

## 🌟 About Me

Recent **B.Tech (Information Technology)** graduate (2022 – 2026, **CGPA: 7.89 / 10.0**) from **MGM University – IICT**, Chh. Sambhajinagar, Maharashtra. 
- Hands-on data engineering experience building **Bronze–Silver–Gold Medallion Lakehouses** on **Azure Databricks** with **PySpark** and **Delta Lake**.
- Production SQL database experience from **Yardi Systems India**, writing Stored Procedures, complex CTEs, cursors, and triggers.
- **2× State-Level Hackathon Winner** and active tech community leader (GDSC Technical Committee, TEDx MGMU Organizing Committee).

---

## 🛠️ Technical Skills

| Domain | Technologies & Frameworks |
| :--- | :--- |
| **Data Engineering** | PySpark, Databricks (Badges), Medallion Architecture, Delta Lake, ETL Pipelines, Data Warehousing, Unity Catalog |
| **Cloud Platforms** | Microsoft Azure (Azure Data Factory, Data Lake / ADLS Gen2, Blob Storage), Databricks on Azure, Google Cloud (Basics) |
| **Languages & Databases** | SQL (Stored Procedures, CTEs, Triggers, Cursors), Python (Pandas, NumPy), MySQL, PostgreSQL, SQL Server |
| **Data Modeling & BI** | Star Schema, Kimball Dimensional Modeling, SCD Type 2, RDBMS Design, EDA, Power BI (Basics), Excel, Streamlit |
| **Developer Tools** | Git, GitHub, Postman, Jupyter Notebook, n8n, VS Code, Agile / Scrum |

---

## 🚀 Featured Projects

### 1. [Retail Data Warehouse – Medallion Architecture](https://github.com/PratikModi22/retail-databricks)
**Stack:** Azure Databricks, PySpark, Delta Lake, Unity Catalog, Star Schema
- Engineered an end-to-end **Bronze–Silver–Gold Lakehouse pipeline** in PySpark on Azure Databricks using Unity Catalog over a retail dataset.
- Cleaned and standardized data in the **Silver layer**: type casting, mixed date format resolution, null handling, deduplication, and referential-integrity validation.
- Designed a **Gold-layer dimensional Star Schema** (fact sales with product, customer, and store dimensions) delivering actionable sales intelligence dashboards.

### 2. [SkillFlow – Enterprise Data Warehouse](https://github.com/PratikModi22/SkillFlow)
**Stack:** Python, MySQL, Streamlit, Star Schema, SCD Type 2, ETL, Window Functions
- Built a three-tier enterprise data warehouse (3NF OLTP + Kimball Star Schema) seeded with **15,000 employees, 19,900+ SCD Type 2 versions, and 38,000+ appraisals**.
- Implemented **Slowly Changing Dimensions (SCD Type 2)** on `dim_employee` and stored procedures for automated delta reconciliation and ETL.
- Developed an interactive Streamlit dashboard leveraging SQL window functions (`LAG`, `DENSE_RANK`) for YoY performance trends, leaderboards, attrition risk, and 4-role RBAC.

---

## 💼 Professional Experience

- **Data Engineer Intern** — **V4C.ai** *(Sept 2026 – Present)*
  - Completed 30 hands-on Medallion Architecture labs on Databricks with PySpark, Delta Lake, and SQL.
  - Built 2 end-to-end projects: Lakehouse Medallion pipelines and dimensional data warehouse architectures.
  - Earned official Databricks badges across Azure, data warehousing, and PySpark.
- **Software Engineer Intern** — **Yardi Systems India** *(Jan 2026 – June 2026 | Pune, India)*
  - Developed production SQL packages and Stored Procedures with CTEs, cursors, and triggers to automate business logic and enterprise reporting.
  - Ensured high data quality across large relational datasets using query optimization, index tuning, and SSMS / SQL Profiler validation.
- **Web Development & AI Intern** — **The Startup Mentor** *(Oct 2024 – July 2025 | Remote)*
  - Built AI automation workflows with n8n; tracked leads and SEO metrics in Excel and Odoo CRM.
  - Deployed client web platforms (WordPress, Shopify) and authored technical SaaS documentation.

---

## 🌐 3D Portfolio Features

- **Interactive 3D Isometric Room**: Built with Three.js and WebGL rendering, featuring a detailed developer workstation.
- **Scroll-Linked Camera Choreography**: Smoothly navigates through room angles in sync with section scrolling.
- **Interactive Day & Night Mode**: Curated color palettes from [Figma's Color Combinations Library](https://www.figma.com/resource-library/color-combinations/):
  - **Light Mode**: Figma Combo 8 (*"Ink Wash"*) + Combo 85 (*"Frozen Lake"*) — Soft Ice Mist canvas (`#f8fafc`), Charcoal Black typography (`#0f172a`), and Electric Cobalt Blue accents (`#2563eb`).
  - **Dark Mode**: Figma Combo 53 (*"Cobalt Sky"*) + Combo 3 (*"Blue Eclipse"*) — Deep Midnight Abyss background (`#0b0f19`) and Radiant Cyber Cobalt accents (`#38bdf8`).
- **Floating Side Menu Navbar**: Non-intrusive frosted glass drawer (`backdrop-filter: blur(28px)`) that slides out on demand without obstructing the 3D room.
- **Full Mobile Responsiveness**: Fluid clamp typography, touch-optimized card paddings, and thumb-friendly controls.

---

## 💻 Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PratikModi22/pratikmodi22.github.io.git
   cd pratikmodi22.github.io
   ```

2. **Run locally:**
   ```bash
   # Option 1: Python HTTP server
   python -m http.server 8000
   
   # Option 2: Windows batch launcher
   run_portfolio.bat
   ```
   Open `http://localhost:8000` in your browser.

3. **Compile updates:**
   Edit `portfolio.config.json` to update content, then recompile:
   ```bash
   python update_content.py
   ```

---

## 📬 Contact & Connect

- **Email**: [pratikgmodi22@gmail.com](mailto:pratikgmodi22@gmail.com)
- **LinkedIn**: [linkedin.com/in/pratik-modi-11ba02283](https://www.linkedin.com/in/pratik-modi-11ba02283)
- **GitHub**: [github.com/PratikModi22](https://github.com/PratikModi22)
- **Location**: Pune, Maharashtra, India
