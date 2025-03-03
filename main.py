from fastapi import FastAPI
from database import update_score, get_score, reset_score
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Додаємо CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # або замість "*" вкажи конкретний домен, якщо потрібно
    allow_credentials=True,
    allow_methods=["*"],  # дозволяємо всі HTTP методи (GET, POST і т.д.)
    allow_headers=["*"],  # дозволяємо всі заголовки
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Clicker Game API"}

@app.post("/click/")
def click(user_id: int, username: str):
    new_score = update_score(user_id, username, 1)
    return {"score": new_score}

@app.get("/score/")
def score(user_id: int):
    current_score = get_score(user_id)
    return {"score": current_score}

@app.post("/reset/")
def reset(user_id: int):
    reset_score(user_id)
    return {"message": "Score reset!"}
