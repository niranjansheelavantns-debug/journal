def calculate_fitness_level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Very Good"
    elif score >= 50:
        return "Good"
    else:
        return "Needs Improvement"


def fitness_report(name, steps, calories, workout_time):
    fitness_score = (steps / 100) + (calories / 10) + workout_time
    level = calculate_fitness_level(fitness_score)

    return (
        "----- Fitness Report -----\n"
        f"Name            : {name}\n"
        f"Steps Taken     : {steps}\n"
        f"Calories Burned : {calories}\n"
        f"Workout Time    : {workout_time} minutes\n"
        f"Fitness Score   : {fitness_score:.2f}\n"
        f"Fitness Level   : {level}"
    )
