# 🚀 GitLab CI/CD DevOps Lab

> **A practical DevOps / DevSecOps laboratory demonstrating automated testing, security validation and containerized application builds using GitLab CI/CD.**

🇬🇧 English · 🇪🇸 Español

---

## 🇬🇧 English

### 📌 Overview

**GitLab CI/CD DevOps Lab** is a practical DevOps portfolio project designed to demonstrate how a modern CI/CD pipeline can automate application testing, dependency security analysis and Docker image builds.

The project uses a small **FastAPI** application as the workload and GitLab CI/CD as the automation platform.

The objective is not to build a complex application, but to demonstrate the **engineering practices surrounding application delivery**:

- Automated testing
- Continuous Integration
- Dependency security analysis
- Containerization
- Docker image building
- Pipeline automation
- Reproducible builds

The project will progressively evolve into a more complete **DevSecOps pipeline**.

---

## 🎯 Project Goals

This laboratory demonstrates how to:

- Build and test a Python application automatically.
- Execute unit tests through GitLab CI/CD.
- Detect vulnerabilities in Python dependencies.
- Build container images automatically.
- Associate Docker images with Git commit versions.
- Establish a foundation for security gates and automated deployments.
- Apply DevOps and DevSecOps principles to the software delivery lifecycle.

---

## 🏗️ Architecture

```text
                         Developer
                             │
                             │ git push
                             ▼
                    ┌─────────────────┐
                    │     GitLab      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   CI Pipeline   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
          ┌────────┐    ┌──────────┐   ┌──────────┐
          │ Tests  │    │ Security │   │  Build   │
          │ pytest │    │pip-audit │   │  Docker  │
          └────────┘    └──────────┘   └──────────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                         Pipeline
                          Result
```

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Application runtime |
| FastAPI | REST API framework |
| Pytest | Automated testing |
| pip-audit | Python dependency security analysis |
| Docker | Application containerization |
| Git | Version control |
| GitLab | Source control and CI/CD |
| GitLab CI/CD | Pipeline automation |

---

## 📂 Project Structure

```text
gitlab-cicd-devops-lab/
│
├── app/
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── Dockerfile
├── requirements.txt
├── .gitignore
├── .gitlab-ci.yml
└── README.md
```

### Application

`app/main.py`

Contains the FastAPI application and its endpoints.

### Tests

`tests/test_main.py`

Contains automated tests executed during the CI pipeline.

### Dockerfile

Defines the container image used to package the application.

### `.gitlab-ci.yml`

Defines the GitLab CI/CD pipeline, including:

- Unit testing
- Dependency security analysis
- Docker image building

---

# 🔄 CI/CD Pipeline

The initial pipeline consists of three stages:

```text
test
  │
  ▼
security
  │
  ▼
build
```

### 1. Test

The pipeline creates a Python environment and executes:

```bash
pytest -v
```

If the tests fail, the pipeline stops and subsequent stages are not executed.

---

### 2. Security

The pipeline performs dependency security analysis using:

```bash
pip-audit -r requirements.txt
```

This stage is intended to identify known vulnerabilities in the application's Python dependencies.

---

### 3. Build

The application is packaged into a Docker image using:

```bash
docker build
```

The image is tagged using the Git commit SHA:

```text
$CI_COMMIT_SHORT_SHA
```

This creates a traceable relationship between:

```text
Git Commit
     │
     ▼
Docker Image
```

allowing a specific container image to be associated with a specific source-code version.

---

# 🐳 Running Locally

## Requirements

Install:

- Python 3.13+
- Docker
- Git

---

## Clone the repository

```bash
git clone https://gitlab.com/YOUR_USERNAME/gitlab-cicd-devops-lab.git

cd gitlab-cicd-devops-lab
```

---

## Create a Python virtual environment

```bash
python3 -m venv .venv
```

Activate it:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run tests

```bash
pytest -v
```

Expected result:

```text
2 passed
```

---

## Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Health endpoint:

```text
http://127.0.0.1:8000/health
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🐳 Running with Docker

Build the image:

```bash
docker build -t gitlab-cicd-devops-lab:1.0.0 .
```

Run the container:

```bash
docker run --rm -p 8000:8000 gitlab-cicd-devops-lab:1.0.0
```

Test the health endpoint:

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

---

# 🔐 DevSecOps Roadmap

This project is intentionally designed to evolve.

Planned security and DevSecOps capabilities include:

- [ ] Dependency vulnerability scanning
- [ ] SAST
- [ ] Secret detection
- [ ] Container image scanning
- [ ] Snyk integration
- [ ] OWASP Dependency-Check
- [ ] OWASP ZAP
- [ ] Nuclei
- [ ] Trivy
- [ ] Security quality gates
- [ ] DAST
- [ ] Security reports integrated into GitLab

---

# 🚀 CI/CD Roadmap

Future pipeline stages:

```text
                ┌──────────────┐
                │     TEST     │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   SECURITY   │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │    BUILD     │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │     PUSH     │
                │ Docker       │
                │ Registry     │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │    DEPLOY    │
                └──────────────┘
```

The final objective is to demonstrate an end-to-end automated software delivery workflow.

---

# 📊 DevOps Practices Demonstrated

This project demonstrates practical implementation of:

- Continuous Integration
- Automated Testing
- Infrastructure-aware application delivery
- Containerization
- Dependency Security
- Build Automation
- Immutable artifact versioning
- Git-based workflows
- DevSecOps principles

---

# 🧪 Testing Strategy

The project currently contains automated API tests covering:

- Root endpoint availability
- API status
- Health endpoint availability
- Health status validation

Additional tests can be added as the application evolves.

---

# 📚 Learning Objectives

This laboratory is part of a broader DevOps / DevSecOps portfolio focused on:

- CI/CD
- Docker
- Kubernetes
- Infrastructure as Code
- Linux
- Networking
- Security automation
- Observability
- Production infrastructure

The project is intentionally developed incrementally to demonstrate the evolution from basic Continuous Integration to a more complete DevSecOps delivery pipeline.

---

# 🇪🇸 Español

## 📌 Descripción

**GitLab CI/CD DevOps Lab** es un laboratorio práctico de DevOps diseñado para demostrar cómo automatizar el testing, el análisis de seguridad de dependencias y la construcción de imágenes Docker utilizando GitLab CI/CD.

El proyecto utiliza una pequeña aplicación **FastAPI** como workload y GitLab CI/CD como plataforma de automatización.

El objetivo no es desarrollar una aplicación compleja, sino demostrar las **prácticas de ingeniería que rodean el proceso de entrega de software**:

- Testing automatizado
- Integración continua
- Análisis de seguridad
- Containerización
- Construcción de imágenes Docker
- Automatización de pipelines
- Builds reproducibles

El proyecto evolucionará progresivamente hacia un pipeline DevSecOps más completo.

---

## 🎯 Objetivos

Este laboratorio demuestra cómo:

- Construir y probar automáticamente una aplicación Python.
- Ejecutar tests mediante GitLab CI/CD.
- Analizar vulnerabilidades en dependencias.
- Construir imágenes Docker automáticamente.
- Asociar imágenes Docker con versiones específicas del código.
- Incorporar controles de seguridad al pipeline.
- Aplicar principios DevOps y DevSecOps al ciclo de entrega de software.

---

## 🏗️ Arquitectura

```text
                         Developer
                             │
                             │ git push
                             ▼
                    ┌─────────────────┐
                    │     GitLab      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   CI Pipeline   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
          ┌────────┐    ┌──────────┐   ┌──────────┐
          │ Tests  │    │ Security │   │  Build   │
          │ pytest │    │pip-audit │   │  Docker  │
          └────────┘    └──────────┘   └──────────┘
```

---

## 🧰 Tecnologías

| Tecnología | Uso |
|---|---|
| Python 3.13 | Runtime |
| FastAPI | API REST |
| Pytest | Testing |
| pip-audit | Seguridad de dependencias |
| Docker | Containerización |
| Git | Control de versiones |
| GitLab | Repositorio y CI/CD |
| GitLab CI/CD | Automatización |

---

## 🔄 Pipeline

La primera versión contiene tres etapas:

```text
test
  ↓
security
  ↓
build
```

### Test

Ejecuta:

```bash
pytest -v
```

### Security

Ejecuta:

```bash
pip-audit -r requirements.txt
```

### Build

Construye la imagen Docker:

```bash
docker build
```

utilizando el SHA corto del commit como identificador de versión.

---

## 🐳 Ejecución local

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar tests:

```bash
pytest -v
```

Ejecutar la API:

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker

Construir:

```bash
docker build -t gitlab-cicd-devops-lab:1.0.0 .
```

Ejecutar:

```bash
docker run --rm -p 8000:8000 gitlab-cicd-devops-lab:1.0.0
```

Comprobar:

```bash
curl http://127.0.0.1:8000/health
```

---

## 🔐 Roadmap DevSecOps

- [x] Automated testing
- [x] Dependency security analysis
- [x] Docker build
- [ ] SAST
- [ ] Secret detection
- [ ] Container scanning
- [ ] Snyk
- [ ] OWASP Dependency-Check
- [ ] OWASP ZAP
- [ ] Nuclei
- [ ] Trivy
- [ ] Security gates
- [ ] DAST

---

## 🚀 Roadmap CI/CD

La evolución prevista es:

```text
TEST
 ↓
SECURITY
 ↓
BUILD
 ↓
PUSH
 ↓
DEPLOY
```

El objetivo final es disponer de un flujo automatizado de entrega de software desde el commit hasta el despliegue.

---

## 👨‍💻 Author

**Leslie León Sinclair**

DevOps / DevSecOps Engineer · SRE · Linux · Networking · Infrastructure

📧 koratsuki.nijuusan@gmail.com

💼 https://www.linkedin.com/in/leon-leslie/

🌐 https://www.sysadminsdecuba.com

---

## ⭐ Portfolio

This project is part of a broader DevOps / DevSecOps portfolio covering:

**Linux · Networking · Docker · Kubernetes · CI/CD · Terraform · OpenTofu · Ansible · DevSecOps · Observability · Infrastructure Automation**

---

> **Building reliable infrastructure. Automating operations. Securing the delivery lifecycle.**

> **Construyendo infraestructura confiable. Automatizando operaciones. Protegiendo el ciclo de entrega.**
