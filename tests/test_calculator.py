import sys
import os

# Add the parent directory (Midterm) to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 4) == 8

def test_divide():
    assert divide(6, 3) == 2
    assert divide(6, 0) == "Error: Division by zero"

