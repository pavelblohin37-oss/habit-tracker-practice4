![CI/CD](https://github.com/pavelblohin37-oss/habit-tracker-practice4/actions/workflows/ci-cd.yml/badge.svg)

# Habit Tracker

Учебный проект: приложение для отслеживания полезных привычек.

- `backend/` — API на FastAPI (`/health`, `/habits`, `/habits/{id}/checkins`, `/habits/{id}/streak`) и тесты
- `web/` — статический фронтенд, сайт: https://habit-tracker-practice4.pages.dev
- `.github/workflows/ci-cd.yml` — CI/CD: jobs `lint` и `test` (Python 3.10–3.12) → job `deploy` на Cloudflare Pages

## Запуск backend локально

```bash
cd backend
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 8000        # http://127.0.0.1:8000/docs
pytest --cov=app
```

