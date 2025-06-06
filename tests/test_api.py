from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_book_and_get_booking():
    # Create a booking
    data = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    }
    res = client.post("/book", json=data)
    assert res.status_code == 200
    # Fetch booking
    res = client.get("/bookings", params={"email": "test@example.com"})
    assert res.status_code == 200
    assert any(b["client_email"] == "test@example.com" for b in res.json())
