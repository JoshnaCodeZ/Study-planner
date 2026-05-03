from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, StudyPlan
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/add")
def add_plan(subject: str, hours: int):
    db: Session = SessionLocal()

    new_plan = StudyPlan(subject=subject, hours=hours)
    db.add(new_plan)
    db.commit()

    return {"message": "Plan added successfully"}


@app.get("/plans")
def get_plans():
    db: Session = SessionLocal()
    
    plans = db.query(StudyPlan).all()
    
    return plans
