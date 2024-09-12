def user_input():
    try:
        mass = float(input("Enter your weight in kilograms : "))
        height = float(input("Enter your height in meters : "))

    except ValueError:
        print("Error: Use float values only")
        exit()

    if mass <= 0 or height <= 0:
        print("Error : Invalid Input, Please Try Again")
        exit()

    return mass, height

def calculate_bmi(m, h):
    bmi = m / (h * h)

    if bmi < 18.5:
        category = "Underweight"
    
    elif bmi < 24.9:
        category = "Normal"
    
    elif bmi < 29.9:
        category = "Overweight"
    
    elif bmi > 30:
        category = "Obese"
    
    return bmi, category

def main():
    mass, height = user_input()
    bmi, category = calculate_bmi(mass, height)
    print(f"\nYour Weight : {mass:.2f} kg")
    print(f"Your Height : {height:.2f} m")
    print(f"Your BMI -->  {bmi:.2f}")
    print(f"You are  -->  {category}\n")
    

main()