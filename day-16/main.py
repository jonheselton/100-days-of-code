##!/usr/bin/python

import money_machine
import coffee_maker
import menu


def main():
    coffee_time = True
    machine = coffee_maker.CoffeeMaker()
    coffee_menu = menu.Menu()
    money = money_machine.MoneyMachine()
    while coffee_time:
        print('please select one of the following')
        print(coffee_menu.get_items())
        choice = input(' : ')
        if choice == 'report':
            machine.report()
            money.report()
        elif choice == 'off':
            print('Powering Off')
            return
        else:
            item = coffee_menu.find_drink(choice)
            for each in coffee_menu.menu:
                if each.name == item.name:
                    money.make_payment(each.cost)
                    drink_choice = each

            if machine.is_resource_sufficient(drink_choice):

                machine.make_coffee(drink_choice)


if __name__ == "__main__":
    main()
