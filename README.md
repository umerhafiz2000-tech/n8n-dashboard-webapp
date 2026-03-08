# N8N Workflow Monitoring Dashboard

A lightweight dashboard built with **Python FastAPI** that connects with **n8n** to monitor workflows and nodes in a centralized interface.

This application provides quick insights into workflow activity by displaying the total number of workflows, nodes, and the status of active and inactive workflows. It also allows users to open workflows directly in n8n for management.

The frontend is built using **HTML, CSS, and JavaScript**, while the backend uses **FastAPI** to fetch and process data from the n8n API.

---

# Features

* View total number of workflows
* View total number of nodes across workflows
* Monitor **active workflows**
* Monitor **inactive workflows**
* Open workflow details in a **separate window**
* Directly access workflows in **n8n**
* Simple and lightweight dashboard interface

---

# Tech Stack

## Backend

* Python
* FastAPI

## Frontend

* HTML
* CSS
* JavaScript

## Integration

* n8n API

---

# Project Structure

```
N8N/
│
├── static/
│   ├── index.html        # Main dashboard UI
│   ├── script.js         # Frontend logic
│   └── try.html          # Additional workflow view page
│
├── app.py                # Main FastAPI application
├── n8n.py                # Handles communication with n8n API
├── requirements.txt      # Python dependencies
│
├── venv/                 # Virtual environment (ignored in git)
└── __pycache__/          # Python cache files
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/n8n-dashboard.git
```

```bash
cd n8n-dashboard
```

---

# 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\\Scripts\\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Run the Application

```bash
uvicorn app:app --reload
```

The application will run at:

```
http://127.0.0.1:8000
```

Open `static/index.html` in your browser to view the dashboard.

---

# How It Works

1. The FastAPI backend connects with the **n8n API**.
2. Workflow data is fetched and processed.
3. The dashboard displays:

   * Total workflows
   * Active workflows
   * Inactive workflows
   * Node statistics
4. Users can open workflows directly inside **n8n** for further management.

---

# Future Improvements

* Real-time workflow monitoring
* Workflow execution logs
* Authentication system
* Workflow filtering and search
* Analytics dashboard with charts
* Error monitoring for failed workflows

---

# Screenshots
<img width="940" height="431" alt="image" src="https://github.com/user-attachments/assets/977cb7b1-52c8-49f3-bad3-e26cc3bcfacb" />
<img width="923" height="356" alt="image" src="https://github.com/user-attachments/assets/015da259-2e4d-4611-ba6c-69b6bbced4ee" />


# We can search the nodes inside the workflows as well.
<img width="292" height="321" alt="image" src="https://github.com/user-attachments/assets/272cf1d1-80ad-4d5c-b712-f7f2696ac201" />


# We can view the workflows in the web app, Also can view it on N8N.
<img width="947" height="436" alt="image" src="https://github.com/user-attachments/assets/467483df-29b1-4b54-8007-e66792418735" />


# Active and published workflows
<img width="930" height="389" alt="image" src="https://github.com/user-attachments/assets/501c9604-ba5d-41b0-9871-5fbca7d24ef9" />


# Inactive Workflows
<img width="846" height="401" alt="image" src="https://github.com/user-attachments/assets/27855f31-b9d1-4065-8f90-f5cca999d55a" />




# Author

Umer
Python Developer

---

# .gitignore

Create a `.gitignore` file and add the following:

```
venv/
__pycache__/
.env
*.pyc
```
