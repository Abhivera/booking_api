from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")

def convert_to_ist(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return IST.localize(dt)
    return dt.astimezone(IST)
