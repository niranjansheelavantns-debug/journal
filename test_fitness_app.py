from fitness_app import fitness_report

def test_fitness_report():
    expected_output = (
        "----- Fitness Report -----\n"
        "Name            : Niranjan\n"
        "Steps Taken     : 7000\n"
        "Calories Burned : 400\n"
        "Workout Time    : 30 minutes\n"
        "Fitness Score   : 140.00\n"
        "Fitness Level   : Excellent"
    )

    result = fitness_report("Niranjan", 7000, 400, 30)
    assert result == expected_output
