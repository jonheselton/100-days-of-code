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
        check_supplies_for_drink(supplies, coffees['latte'])
    elif choice == 'e':
        check_supplies_for_drink(supplies, coffees['espresso'])
    elif choice == 'c':
        check_supplies_for_drink(supplies, coffees['cappuccino'])


def report(supplies):
    print(supplies)


# check supplies
def check_supplies_for_drink(supplies, drink):
    for k, v in supplies.items():
        if not v >= drink['ingredients'][k]:
            print('not enough ' + k)
            return machine_menu(supplies)

    return make_drink(drink, supplies)


def make_drink(drink, supplies):
    if drink == coffees['cappuccino']:
        print('make a cappuccino')
        remaining_supplies = {key: supplies[key] - coffees['cappuccino']['ingredients'].get(key, 0) for key in supplies}
        print(remaining_supplies)
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


# TODO-1 insert coins
# TODO-2 make change
# TODO-3 subtract used resources
# TODO-4 implement while loop to keep the machine on
coffees = data.MENU
current_supplies = data.resources


def main():
    global current_supplies
    print(machine_menu(current_supplies))


if __name__ == "__main__":
    main()
