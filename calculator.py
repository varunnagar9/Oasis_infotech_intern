
def get_positie_float(prompt):
    """Prompts user for input and validates that it is apositive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <=0:
                print("Error: Value must be greater than zero. Please try again.\n")
            else:
                return value
        except ValueError:
            print("Error: Invaild input. Please enter a valid number.\n")
            

def calculate_bmi():
    print("=" * 35)
    print("   BODY MASS INDEX CALCULATOR   ")
    print("=" * 35)
    
    #Prompt user for weight (KG)
    weight = get_positie_float("Enter your weight in kilograms (kg): ")
    height_cm = get_positie_float("Enter your height in centimeters (cm): ")
                
    #Convert height from cm to meters
    height_m = height_cm / 100
    
    #Calculate BMI formula: weight / (height_m^2)
    bmi = weight / (height_m**2)
    
    #Classify the BMI result
    if bmi <18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Normal Weight"
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
        
    #Display results rounded to 2 decimal places
    print("\n" + "=" * 35)
    print(f"Height: {height_cm:.1f} cm | Weight: {weight:.1f} kg") 
    print(f"Your BMI: {bmi:2f}")
    print(f"Category: {category}")
    print("-" * 35)
    
if __name__== "__main__":
    calculate_bmi()