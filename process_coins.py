def process_coins():
    print("Please insert coins:")
    total = int(input("How many quarters? ")) * 0.25 + \
            int(input("How many dimes? ")) * 0.1 + \
            int(input("How many nickles? ")) * 0.05 + \
            int(input("How many cents? ")) * 0.01
    return total
