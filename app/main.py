from fastapi import FastAPI

app = FastAPI(
    title="GitLab CI/CD DevOps Lab",
    description="Demo API for DevOps and DevSecOps CI/CD automation",
    version="1.1.0",
)


@app.get("/")
def root():
    return {
        "message": "GitLab CI/CD DevOps Lab v1.1",
        "status": "ok",
        "version": "1.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

