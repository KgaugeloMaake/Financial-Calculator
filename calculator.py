import math

print("\nThe simple calculator can be used to calulate investemnts in simple or compound interest. \nYou can also calculate a bond repayment\n")



def main_menu():
    option1 = int(input("\nWhat would you like to calculate?\n1.Investment\n2.Bond repayment\n"))
    if option1 ==1:

        principal = float(input("\nWhat is the amount of money you are depositing? (R) "))
        interest_rate = float(input("What is the interest rate? (%) "))
        years = float(input("How many years do you plan to invest for? "))

        type_of_intere = float(input("\nSimple or compound?\n1.Simple\n2.Compound?\n"))
        
        if interest_rate > 0:
            interest_rate /= 100
            if type_of_intere == 1:
                total_amount = principal * (1 + interest_rate * years) 
            else:
                total_amount = principal * math.pow(1 + interest_rate, years)


        print("\nYour total amount after {} years will be R{:.2f}".format(years, total_amount))
        exit_app()

    elif option1 == 2:
        present_value = float(input("\nWhat is the present value of the house?(R) "))
        interest_rate = float(input("What is the interest rate?(%) "))
        months = float(input("How many months do you plan to take to repay the bond? "))


        monthly_interest_rate = interest_rate / 100


        monthly_repayment = (present_value * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -months))


        print("\nYour monthly repayment will be R{:.2f}".format(monthly_repayment))
        exit_app()
  
    else:
        print("\nOption not available")
    exit_app()

def exit_app():
    answer = str(input("Do you still want to continue to? Yes or No\n"))
    if answer == "Yes\n":
        main_menu()
    elif answer == "No\n":
        print("\nThank you for using the app")
    else:
        print("\nOption is not available")
        main_menu()

main_menu()
        
    


    
