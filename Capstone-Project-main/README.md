# DevOps Capstone Project

![CI Build](https://github.com/Syahratu015/Capstone-funal-project/actions/workflows/ci-build.yaml/badge.svg)

## Customer Accounts Microservice

This repository contains the **Customer Accounts Microservice** developed as part of the **DevOps Capstone Project**.
The microservice provides RESTful APIs to manage customer account information and demonstrates modern DevOps practices.

---

## Features

* Create Customer Account
* List All Accounts
* Read Account Details
* Update Account Information
* Delete Account

---

## Technology Stack

* Python
* Flask
* Docker
* Kubernetes
* GitHub Actions (CI/CD)
* Flask-Talisman (Security Headers)
* Flask-CORS

---

## API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| POST   | /accounts      | Create account    |
| GET    | /accounts      | List all accounts |
| GET    | /accounts/{id} | Read account      |
| PUT    | /accounts/{id} | Update account    |
| DELETE | /accounts/{id} | Delete account    |

---

## Running the Application

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install flask flask-cors flask-talisman pytest coverage
```

### Run Application

```bash
set FLASK_APP=service
flask run
```

Application will run on:

```
http://localhost:5000
```

---

## CI/CD Pipeline

This project uses **GitHub Actions** for:

* Lint checking
* Unit testing
* Coverage reporting
* Build validation

---

## Project Structure

```
.
├── service
│   └── __init__.py
├── tests
├── Dockerfile
├── setup.cfg
└── README.md
```

---

## Author

DevOps Capstone Project
IBM Skills Network
