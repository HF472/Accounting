import pandas as pd
import csv
import sys


"""This program is to calculate montly accounting, take income subtract expenses
leave money for taxes, how to much to pay yourself and save to a csv file"""

def print_menu():
    #create a menu
    print(30 * "-" , "MENU" , 30 * "-")
    print(6 * "-", "Both programs offer savings and investment functions", 6 * "-")
    print("1. Business accounting")
    print("2. Paycheck accounting")
    print("3. Exit")

def get_month():
    months =["January","Feburary","March","April", "May", "June", "July", "August",
     "September", "October", "Novemeber","December"]
    month = input("Enter the month you wish to do your calculatons for: ").title()
    if month not in months:
        print("Not a known month")
        month = input("Enter the month you wish to do your calculatons for: ").title()
    if len(month) > 4:
        month = month[:3]
        return month
    else:
        return month

def monthly_income():
    #Get monthly income, convert to float
    income = input("Enter the amount of money you made this month: ")
    income = float(income)
    return income

def expenses():
    #Ask user for expenses until 0 is entered
    print("Enter the amount montly expenses one by one, when done enter 0 to end")
    total_exp = 0.0
    while True:
        try:
            monthly_exp = input(":$ ")
            monthly_exp = float(monthly_exp)
        except ValueError:
            print("You must enter a number ")
            monthly_exp = float(input(":$ "))
        total_exp += monthly_exp
        if monthly_exp == 0:
            break
    print(f"Total amount of expenses:$ {total_exp}")
    return total_exp


def cal_taxes(my_income, my_expenses):
    #tax rate can be changed to what ever the user needs
    keep_for_taxes = 0.0
    tax_rate = 0.30
    get_diff_taxRate = input("Is your tax rate 30% enter y/n: ")
    if get_diff_taxRate == 'n':
        tax_rate = input("Enter tax rate like so (0.25): ")
        tax_rate = float(tax_rate)
    after_exp = my_income - my_expenses
    keep_for_taxes = after_exp * tax_rate
    return keep_for_taxes

def pay_to_you(taxes, income, expenses):
    """take amount for taxes and subtract from the amount after expenses"""
    difference = income - expenses
    payment = difference - taxes
    return payment

def print_pandas(month,my_income,my_expenses,taxes,pay_check):
    """create a data frame with a dictionary and pass returned values from functions"""
    data = pd.DataFrame({'Month': [month], 'Income': [my_income], 'Expenses': [my_expenses],
     'left for taxes': [taxes], 'pay check': [pay_check]})
    print (data)
    return data

def write_to_csv(data):
    #write to csv file, mode 'a' allows the data to be saved instead of over written
    data.to_csv ('ble_expenses.csv',index=False, encoding='utf-8', mode='a')

def savings(pay):
    """Ask for additional expenses if not a business expense and calculate whats
    left for savings"""
    new_expenses = 0.0
    additional_expenses = input("Do you have any additional expenses? enter y/n ").lower()
    if additional_expenses == 'y' or  additional_expenses == 'yes':
        print("Enter 0 if there are no more additional expenses ")
        while True:
            try:
                other_exp = input(":$ ")
                other_exp = float(other_exp)
            except ValueError:
                print("You must enter a number ")
                other_exp = float(input(":$ "))
            new_expenses += other_exp
            if other_exp == 0:
                break
        left_over = pay - new_expenses
        print(f"You have {left_over} left after the additional expenses")
        return left_over
    elif additional_expenses == 'n' or  additional_expenses == 'no':
        print(pay)

def invest_save(savings):
    """Ask how to much to invest if any left over"""
    investOrSave = input("Do you want to save all of the money or invest? (enter invest or save) ").lower()
    if investOrSave == 'invest':
        percentage = input("It's recommneded to invest between 10 to 20% (enter in decimal ex. 0.10): ")
        percentage = float(percentage)
        amountToInvest = savings * percentage
        print(amountToInvest)
    else:
        print(f"You are saving {savings} and chose not to invest")

"""This portion of the program will to be for opton 2 on the menu for people with regular
    pay checks and no added business expenses"""

def your_paycheck_amount():
    #Get monthly income, convert to float
    income = input("Enter the amount of money you made this month: ")
    income = float(income)
    return income

def user_monthly_expenses():
    #Ask user for expenses until 0 is entered
    print("Enter the amount montly expenses one by one, when done enter 0 to end")
    total_exp = 0.0
    while True:
        try:
            monthly_exp = input(":$ ")
            monthly_exp = float(monthly_exp)
        except ValueError:
            print("You must enter a number ")
            monthly_exp = float(input(":$ "))
        total_exp += monthly_exp
        if monthly_exp == 0:
            break
    print(f"Total amount of expenses:$ {total_exp}")
    return total_exp

def after_expenses(income, expenses):
    """take amount for taxes and subtract from the amount after expenses"""
    difference = income - expenses
    return difference



loop = True
while loop:
    print_menu()
    choice = int(input("Enter a choice [1-3] "))
    if choice == 1:
        month = get_month()
        my_income = monthly_income()
        my_expenses = expenses()
        taxes = cal_taxes(my_income, my_expenses)
        pay_check = pay_to_you(taxes, my_income,my_expenses)
        df = print_pandas(month,my_income,my_expenses,taxes,pay_check)
        write_to_csv(df)
        continue_to_saving = input("Do you wish to contiune to calculate savings? ")
        if continue_to_saving == 'y' or continue_to_saving == 'yes':
            after_new_expenses = savings(pay_check)
            invest_save(after_new_expenses)
        else:
            print("Ending Program")
            sys.exit()
        loop = False
    elif choice == 2:
        reg_paycheck = your_paycheck_amount()
        monthly_expenses = user_monthly_expenses()
        amount_leftOver = after_expenses(reg_paycheck,monthly_expenses)
        invest_save(amount_leftOver)
        loop = False
    elif choice == 3:
        sys.exit()
