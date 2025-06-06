from app.database import SessionLocal, engine
from app import models
from datetime import datetime, timedelta
import pytz

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()
classes = [
    models.FitnessClass(name="Yoga", datetime=pytz.timezone("Asia/Kolkata").localize(datetime.now() + timedelta(days=1)), instructor="Alice", available_slots=10),
    models.FitnessClass(name="Zumba", datetime=pytz.timezone("Asia/Kolkata").localize(datetime.now() + timedelta(days=2)), instructor="Bob", available_slots=8),
    models.FitnessClass(name="HIIT", datetime=pytz.timezone("Asia/Kolkata").localize(datetime.now() + timedelta(days=3)), instructor="Charlie", available_slots=5),
]
db.add_all(classes)
db.commit()
db.close()
