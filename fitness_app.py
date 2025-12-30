def calculate_fitness_level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Very Good"
    elif score >= 50:
        return "Good"
    else:
        return "Needs Improvement"


# Taking user input
name = input("Enter Name: ")
steps = int(input("Enter Steps Taken: "))
calories = int(input("Enter Calories Burned: "))
workout_time = int(input("Enter Workout Time (minutes): "))

fitness_score = (steps / 100) + (calories / 10) + workout_time
level = calculate_fitness_level(fitness_score)

print("\n----- Fitness Report -----")
print(f"Name            : {name}")
print(f"Steps Taken     : {steps}")
print(f"Calories Burned : {calories}")
print(f"Workout Time    : {workout_time} minutes")
print(f"Fitness Score   : {fitness_score:.2f}")
print(f"Fitness Level   : {level}")
