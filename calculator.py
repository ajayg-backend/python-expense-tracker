import json

def analyze_expenses(expenses):

    total = 0
    home_total = 0
    above_300 = 0

    highest_amount = expenses[0]["amount"]
    highest_item = expenses[0]["item"]

    for expense in expenses:

        amount = expense["amount"]
        category = expense["category"]
        item = expense["item"]

        total += amount

        if category == "home":
            home_total += amount

        if amount > 300:
            above_300 += 1

        if amount > highest_amount:
            highest_amount = amount
            highest_item = item

try:
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
except:
    expenses = []

while True:
    print("\nExpense Tracker PRO")
    print("1 Add Expense")
    print("2 Show Report")
    print("3 Delete Expense")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        item = input ("item name: ")
        amount = int(input("amount: "))
        category = input("category")

        expense = {
            "item": item,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        with open("expenses.json", "w") as f:
            json.dump(expenses, f)
        print("Expense added!")

    elif choice == "2":

        total = 0 
        home_total = 0
        travel_total = 0
        personal_total = 0

        highest = 0
        highest_item = ""

        for expense in expenses:

            amount = expense["amount"]
            category = expense["category"]
            item = expense["item"]

            total += amount

            if category == "home" :
                home_total += amount

            elif category == "travel":
                travel_total += amount

            elif category == "personal":
                personal_total += amount

            if amount > highest:
                highest = amount
                highest_item = item

        print("total:", total)
        print("home total:", home_total)
        print("travel total:", travel_total)
        print("personal total:", personal_total)
        print("highest item:", highest_item)

        print("\nExpense Graph")

        print("home      :", "▊" * (home_total // 10))
        print("travel    :", "▊" * (travel_total // 10))
        print("personal  :", "▊" * (personal_total // 10))

    
 
    elif choice ==  "3":
        for i, expense in enumerate(expenses):
            print(i, expense["item"], expense["amount"])

        index = int(input("enter index to delete: "))

        if index < len(expenses):
            expenses.pop(index)
            print("Expense deleted")

        elif choice == "4":
            print("Goodbye")
            break

    
       

