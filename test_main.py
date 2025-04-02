from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the guessing game!" in response.json()["message"]

def test_guess_low():
    response = client.get("/guess/0")
    assert response.status_code == 200
    assert "Please choose a number between 1 and 100." in response.json()["message"]

def test_guess_high():
    response = client.get("/guess/101")
    assert response.status_code == 200
    assert "Please choose a number between 1 and 100." in response.json()["message"]

def test_guess_valid():
    response = client.get("/guess/50")
    assert response.status_code == 200
    assert "Try" in response.json()["message"] or "Congratulations!" in response.json()["message"]
