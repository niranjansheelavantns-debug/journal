import sys
from fitness_app import calculate_fitness_level, main

def test_calculate_fitness_level():
    assert calculate_fitness_level(95) == "Excellent"
    assert calculate_fitness_level(75) == "Very Good"
    assert calculate_fitness_level(55) == "Good"
    assert calculate_fitness_level(30) == "Needs Improvement"


def test_fitness_app_output(capsys, monkeypatch):
    test_args = [
        "fitness_app.py",
        "Niranjan",
        "8000",
        "500",
        "30"
    ]

    monkeypatch.setattr(sys, "argv", test_args)

    main()

    captured = capsys.readouterr().out

    assert "Name            : Niranjan" in captured
    assert "Steps Taken     : 8000" in captured
    assert "Calories Burned : 500" in captured
    assert "Workout Time    : 30 minutes" in captured
    assert "Fitness Level   : Very Good" in captured
