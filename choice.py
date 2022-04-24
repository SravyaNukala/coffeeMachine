import check_resources
import process_coins
import enough_money
import reduce_resources


def choice(select):
    check_value = check_resources.check_resources(select)
    if check_value:
        total = process_coins.process_coins()
        enough_amount = enough_money.enough_money(select, total)
        if enough_amount:
            reduce_resources.reduce_resources(select)
