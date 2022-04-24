import menu


def check_resources(selected_value):
    is_sufficient=True
    for item in menu.MENU[selected_value]["ingredients"]:
        if menu.resources[item] < menu.MENU[selected_value]["ingredients"][item]:
            is_sufficient = False
    if not is_sufficient:
        print("Sorry there are not enough resources")
    return is_sufficient
