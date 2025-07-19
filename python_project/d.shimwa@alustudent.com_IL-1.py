def get_valid_input(prompt, allow_digits=False):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty. Please try again.")
            continue
        if not allow_digits and not any(c.isalpha() for c in value):
            print("Input must contain letters. Please try again.")
            continue
        return value
    
# Ask for Student info
name = get_valid_input("Enter your name: ")
cohort = get_valid_input("Enter your cohort: ", allow_digits=True)
faculty = get_valid_input("Enter your faculty: ")
intake = get_valid_input("Enter your intake: ", allow_digits=True)

# Collecting student information with validation
print(f"Name: {name}")
print(f"Cohort: {cohort}")
print(f"Faculty: {faculty}")
print(f"Intake: {intake}")

# This script collects student and assignment information with validation
def get_assignment_category(prompt):
    while True:
        value = input(prompt).strip()
        if value.lower() not in ["formative", "summative"]:
            print("Category must be 'Formative' or 'Summative'. Please try again.")
            continue
        return value.capitalize()

def get_weight(prompt):
    while True:
        value = input(prompt).strip()
        try:
            weight = float(value)
            if weight <= 0:
                print("Weight must be greater than 0. Please try again.")
                continue
            return weight
        except ValueError:
            print("Weight must be a numeric value. Please try again.")

def get_grade(prompt):
    while True:
        value = input(prompt).strip()
        try:
            grade = float(value)
            if not (0 <= grade <= 100):
                print("Grade must be between 0 and 100. Please try again.")
                continue
            return grade
        except ValueError:
            print("Grade must be a numeric value. Please try again.")

# Initialize totals
formative_total = 0
summative_total = 0

# Set maximums
FORMATIVE_MAX = 60
SUMMATIVE_MAX = 40

while True:
    assignment_name = get_valid_input("Enter assignment name: ")
    assignment_category = get_assignment_category("Enter assignment category (Formative/Summative): ")
    weight = get_weight("Enter assignment weight: ")
    grade = get_grade("Enter obtained grade: ")

    weighted_grade = (grade / 100) * weight

    if assignment_category == "Formative":
        if formative_total + weighted_grade > FORMATIVE_MAX:
            print(f"Formative total cannot exceed {FORMATIVE_MAX}. Assignment not added.")
        else:
            formative_total += weighted_grade
    elif assignment_category == "Summative":
        if summative_total + weighted_grade > SUMMATIVE_MAX:
            print(f"Summative total cannot exceed {SUMMATIVE_MAX}. Assignment not added.")
        else:
            summative_total += weighted_grade

    print(f"Assignment Name: {assignment_name}")
    print(f"Assignment Category: {assignment_category}")
    print(f"Weight: {weight}")
    print(f"Obtained Grade: {grade}")
    print(f"Weighted Grade: {weighted_grade:.2f}")
    print(f"Formative Total: {formative_total:.2f} / {FORMATIVE_MAX}")
    print(f"Summative Total: {summative_total:.2f} / {SUMMATIVE_MAX}")

    more = input("Do you want to add another assignment? (yes/no): ").strip().lower()
    if more != "yes":
        break

print("Final Formative Total:", formative_total)
print("Final Summative Total:", summative_total)

# Calculate GPA
total_overall_grade = formative_total + summative_total
gpa = (total_overall_grade / 100) * 5
print(f"Total Overall Grade: {total_overall_grade:.2f} / 100")
print(f"GPA: {gpa:.2f} / 5")