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
        print(k, v)
        if not v >= drink['ingredients'][k]:
            print('not enough ' + k)
            return machine_menu(supplies)

    return make_drink(drink, supplies)


def make_drink(drink, supplies):
    if drink == coffees['cappuccino']:
        print('make a cappuccino')
    elif drink == coffees['espresso']:
        print('make an espresso')
    elif drink == coffees['latte']:
        print('make a latte')
    else:
        print('invalid choice')


# TODO-1 insert coins
# TODO-2 make change
# TODO-3 subtract used resouurces
# TODO-4 implement while loop to keep the machine on
coffees = data.MENU
current_supplies = data.resources

def main():

    choice = machine_menu(current_supplies)


if __name__ == "__main__":
    main()
