import menu


def enough_money(choice, total):
    if total >= menu.MENU[choice]["cost"]:
        change = total - menu.MENU[choice]["cost"]
        if change > 0:
            print(f"Take your change: {round(change, 3)}")
        menu.profit += menu.MENU[choice]["cost"]
        print(f"Enjoy your {choice}")
        return True
    else:
        print(f"Sorry that's not enough money. Cost of {choice} is {menu.MENU[choice]['cost']}. Your Money Refunded")
        return False
