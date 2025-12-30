import sys

def calculate_fitness_level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Very Good"
    elif score >= 50:
        return "Good"
    else:
        return "Needs Improvement"


# Argument validation
if len(sys.argv) != 5:
    print("Usage: python fitness_app.py Name Steps Calories WorkoutTime")
    sys.exit(1)

name = sys.argv[1]          # string
steps = int(sys.argv[2])
calories = int(sys.argv[3])
workout_time = int(sys.argv[4])

fitness_score = (steps / 100) + (calories / 10) + workout_time
level = calculate_fitness_level(fitness_score)

print("----- Fitness Report -----")
print(f"Name            : {name}")
print(f"Steps Taken     : {steps}")
print(f"Calories Burned : {calories}")
print(f"Workout Time    : {workout_time} minutes")
print(f"Fitness Score   : {fitness_score:.2f}")
print(f"Fitness Level   : {level}")
