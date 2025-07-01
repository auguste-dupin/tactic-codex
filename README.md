# Tactic CRM

This repository contains a minimal full-stack CRM with two modes: **Studio** for prototyping and **Live** for production. The backend uses FastAPI with SQLAlchemy and the frontend is a simple React app with Tailwind CSS. Docker Compose is provided for local development. Configuration is managed via environment variables loaded from `.env` using Pydantic settings.

## Requirements
- Docker and Docker Compose

## Quick Start

1. Copy `.env.example` to `.env` and adjust settings if necessary.
2. Run `docker-compose up --build` to start both services.
3. Visit `http://localhost:3000` for the frontend and `http://localhost:8000/docs` for the API docs.

If Docker is not available, you can run the API directly:

```bash
pip install -r backend/requirements.txt
uvicorn app.main:app --reload --app-dir backend
```

### Environment
Application settings are read from `.env` using Pydantic. Copy `.env.example` and adjust values such as `MODE` and `DATABASE_URL` to switch between Studio and Live configurations.

### Modes
Switch between `STUDIO` and `LIVE` by changing the `MODE` variable in `.env`. Studio mode uses SQLite while Live mode can be configured for PostgreSQL by setting `DATABASE_URL`.

## Project Structure
```
backend/   # FastAPI app
frontend/  # React app
```

This is a starting point for further development. Add additional modules and features as needed.
