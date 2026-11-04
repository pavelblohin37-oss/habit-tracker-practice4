from fastapi import FastAPI

app = FastAPI(title="Habit Tracker API", version="0.2.0")


@app.get("/health")
def health():
    return {"status": "ok"}
