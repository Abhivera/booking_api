from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status

def get_upcoming_classes(db: Session):
    return db.query(models.FitnessClass).order_by(models.FitnessClass.datetime).all()

def create_booking(db: Session, booking: schemas.BookingRequest):
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking.class_id).first()

    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No available slots")

    new_booking = models.Booking(**booking.dict())
    fitness_class.available_slots -= 1
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def get_bookings_by_email(db: Session, email: str):
    return db.query(models.Booking).filter(models.Booking.client_email == email).all()
