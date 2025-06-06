from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from typing import List
import logging

from app import models, schemas, crud
from app.database import engine, SessionLocal
from app.utils import convert_to_ist

models.Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Fitness Studio Booking API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/classes", response_model=List[schemas.FitnessClassResponse])
def read_classes(db: Session = Depends(get_db)):
    classes = crud.get_upcoming_classes(db)
    for c in classes:
        c.datetime = convert_to_ist(c.datetime)
    return classes

@app.post("/book", response_model=schemas.BookingResponse)
def book_class(booking: schemas.BookingRequest, db: Session = Depends(get_db)):
    return crud.create_booking(db, booking)

@app.get("/bookings", response_model=List[schemas.BookingResponse])
def get_bookings(email: str = Query(...), db: Session = Depends(get_db)):
    return crud.get_bookings_by_email(db, email)
