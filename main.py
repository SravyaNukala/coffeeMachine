import menu
import report
import choice

items = list(menu.MENU.keys())


while True:
    select=input(f"what would you like to have? {items}: ")
    if select == "off":
        print("Have a Nice Day")
        exit(0)

    elif select == "report":
        report.report()

    elif select in items:
        choice.choice(select)

    else:
        print(f"Please select from {items}")

