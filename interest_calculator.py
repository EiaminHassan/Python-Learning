principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than 0. Please try again.")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    rate = rate / (12 * 100)  # Convert annual rate to monthly and percentage to decimal
    # print(rate)
    if rate <= 0:
        print("Rate of interest must be greater than 0. Please try again.")

while time <= 0:
    time = float(input("Enter the time period:(in months) "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")


term1 = pow(1 + rate, time)
emi = (principle * rate * term1) / (term1 - 1)
print(f"The EMI for the given inputs is: {emi:.2f}")
print(f"The total amount paid over the period is: {emi * time:.2f}")
print(f"The total interest paid over the period is: {(emi * time) - principle:.2f}")