import menu


def report():
    print(f"water: {menu.resources['water']}ml")
    print(f"milk: {menu.resources['milk']}ml")
    print(f"coffee: {menu.resources['coffee']}gms")
    print(f"Money: {menu.profit}")
