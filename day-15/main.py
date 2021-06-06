##!/usr/bin/python

import data


# create menu, order, power off, or report
def machine_menu(supplies):
    print('Welcome to my coffee machine!')
    choice = input('Please choose from this list\n (c)appuccino, (e)spresso, (l)atte : ')
    if choice == 'report':
        return report(supplies)
    elif choice == 'off':
        print('Powering off...')
        return exit()
    elif choice == 'l':
        return check_supplies_for_drink(supplies, coffees['latte'])
    elif choice == 'e':
        return check_supplies_for_drink(supplies, coffees['espresso'])
    elif choice == 'c':
        return check_supplies_for_drink(supplies, coffees['cappuccino'])


def report(supplies):
    print(supplies)
    return supplies


# check supplies
def check_supplies_for_drink(supplies, drink):
    for k, v in drink['ingredients'].items():
        if v > supplies[k]:
            print('not enough ' + k)
            return machine_menu(supplies)
    return get_money(drink, supplies)


def get_money(drink, supplies):
    total_inserted = float(0)
    for k, v in coins.items():
        coins[k] = float(input('insert {} : '.format(k)))
    total_inserted += coins['nickel'] * .05
    total_inserted += coins['dime'] * .10
    total_inserted += coins['quarter'] * .25
    if total_inserted >= drink['cost']:
        print('returning {}'.format(total_inserted - float(drink['cost'])))
        return make_drink(drink, supplies)
    else:
        print('not enough cash money, returning coins')
        return supplies


def make_drink(drink, supplies):
    if drink == coffees['cappuccino']:
        print('make a cappuccino')
        remaining_supplies = {key: supplies[key] - coffees['cappuccino']['ingredients'].get(key, 0) for key in supplies}
        return remaining_supplies
    elif drink == coffees['espresso']:
        remaining_supplies = {key: supplies[key] - coffees['espresso']['ingredients'].get(key, 0) for key in supplies}
        print('make an espresso')
        return remaining_supplies
    elif drink == coffees['latte']:
        remaining_supplies = {key: supplies[key] - coffees['latte']['ingredients'].get(key, 0) for key in supplies}
        print('make a latte')
        return remaining_supplies
    else:
        print('invalid choice')


coffees = data.MENU
coins = data.coins


def main():
    current_supplies = data.resources
    keep_going = True

    while keep_going:
        current_supplies = machine_menu(current_supplies)




if __name__ == "__main__":
    main()
