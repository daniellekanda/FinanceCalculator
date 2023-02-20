#This program alllows users to access 2 different finance calculators (bond and investment)
#users can input data and run their own caculations on the findings. 

import math

#welcome message explaining the finance calculator
print(" ")
print("Welcome to the finance calculator! \nChoose either 'investment' or 'bond' from the menu below to proceed:")
print(" ") 
print("investment: to calculate the amount of interest you'll earn on your investment. \nbond: to calculate the amount you'll have to pay on a home loan")
print(" ")

#requests user to choose if they want 'bond' or 'investment' calculator
calc_type = input("Which finance calculator do you want to access? Type 'investment' or 'bond' to choose: ")

#converts user input to lowercase and checks they have chosen 'investment' or 'bond' if not user is prompted to resubmit their choice
while calc_type.lower() != "investment" and calc_type.lower() != "bond":
    print(" ")
    print("You have entered an incorrect option. Please try again")
    calc_type = input("Please enter either 'investment' or 'bond' to choose the right calculator: ")   
if calc_type.lower() == "investment" or "bond":      
    print(f"You chose the {calc_type.lower()} calculator.")
    print(" ")

#User has chosen 'investment' calculator. This sections requests user to submit data needed for the investment calculation. 
#Requests user choose either simple or compound interests
#Then prints a message with all user data and the total earned from the investment for either simple interest or compound interest. 
if calc_type.lower() == "investment":
    investment_deposit = int(input("How much money are you depositing?: "))
    investment_interest_rate = int(input("What is your interest rate?: "))
    investment_years = int(input("How many years do you plan to invest?: "))
    print(" ")
    interest = input("Do you want simple interests [S] or compound interest [C]: ")
    print(" ")
    if interest.upper() == "S":
        simple_interest = investment_deposit * (1 + (investment_interest_rate / 100) * investment_years)
        print(" ")
        print(f"""You chose simple interest. The amount of interest you will earn on your deposit of £{investment_deposit} over {investment_years} years
        with an interest rate of {investment_interest_rate}% is £{simple_interest}""")
    elif interest.upper() == "C": 
        compound_interest = (investment_deposit * math.pow((1 + (investment_interest_rate / 100)), investment_years))
        print(f"""You chose compound interests. The amount of interest you will earn with your deposit of £{investment_deposit} over {investment_years} years
        with an interest rate of {investment_interest_rate}% is £{round(compound_interest, 2)}.""")
        print(" ")

#User chose bond calculator. 
#This sections requests user submits data to a bond repayment calculation plan. 
# prints message presenting user data and the total amount for bond repayment. 
if calc_type.lower() == "bond":
    bond_house_value = int(input("What is the present value of your house?: "))
    bond_annual_interest_rate = int(input("What is your interest rate?: "))
    bond_monthly_interests_rate = bond_annual_interest_rate / 12
    bond_monthly_interests_rate_calc = bond_monthly_interests_rate / 100
    bond_months_to_pay = int(input("How many months do you plan to take to repay the bond?: "))
    bond_repayment_equation = (bond_monthly_interests_rate_calc * bond_house_value) / (1 - (1 + bond_monthly_interests_rate_calc) ** (-1 * bond_months_to_pay))
    print(" ") 
    print(f"""For a property valued at £{bond_house_value} with an interests rate of {bond_annual_interest_rate}% with 
    a payback scheme of {bond_months_to_pay} months the amount to be paid back each month is: £{round(bond_repayment_equation, 2)}. """)
    print(" ")


