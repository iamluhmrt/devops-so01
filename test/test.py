import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to the guessing game" in response.json()["message"]

def test_guess_number_below_range():
    response = client.get("/guess/0")
    assert response.status_code == 200
    assert response.json()["message"] == "Please choose a number between 1 and 100."

def test_guess_number_above_range():
    response = client.get("/guess/101")
    assert response.status_code == 200
    assert response.json()["message"] == "Please choose a number between 1 and 100."

def test_guess_number_higher_or_lower():
    response = client.get("/guess/50")
    assert response.status_code == 200
    assert any(
        msg in response.json()["message"] for msg in [
            "Try a higher number!",
            "Try a lower number!",
            "Congratulations! You guessed it! A new number has been generated."
        ]
    )

def test_guess_exact_number_resets_game(monkeypatch):
    from src import main

    monkeypatch.setattr(main, "secret_number", 42)
    response = client.get("/guess/42")
    assert response.status_code == 200
    assert "Congratulations" in response.json()["message"]
