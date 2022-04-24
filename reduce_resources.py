import menu


def reduce_resources(choice):
    for item in menu.resources:
        menu.resources[item] -= menu.MENU[choice]["ingredients"][item]
