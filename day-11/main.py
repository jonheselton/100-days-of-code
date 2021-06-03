import random


def deal(nr_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choices(cards, k=nr_cards)
    return cards


def check_hand(hand):
    hand_value = sum(hand)
    if hand_value > 21 and max(hand) < 11:
        return 'bust'
    elif 11 in hand and hand_value > 21:
        return hand_value - 10
    elif hand_value == 21 and len(hand) == 2:
        return 'black jack'
    else:
        return hand_value


def action():
    choice = input('(h)it or (s)tay')
    if choice == 'h':
        return True
    elif choice == 's':
        return False
    else:
        print('Invalid choice, try again')
        return action()


def main():
    player_hand = deal(2)

    result = check_hand(player_hand)
    if result == 'bust':
        print(result)
        return
    elif result == 'black jack':
        print(result)
        return
    else:
        print('you have {}'.format(result))
        print(player_hand)
        hit = action()

    while hit:
        player_hand += deal(1)
        result = check_hand(player_hand)
        if result == 'bust':
            print(result)
            return
        else:
            print('you have {}'.format(result))
            print(player_hand)
            hit = action()

    dealer_hand = deal(2)
    result = check_hand(dealer_hand)
    if result == 'black jack':
        print('The dealer got {}'.format(result))
        return
    else:
        if result >= 17:
            # stay
            hit = False
        else:
            hit = True

    while hit:
        dealer_hand += deal(1)
        result = check_hand(dealer_hand)
        if result == 'bust':
            print('Dealer Busts, You Win!')
            return
        else:
            if result >= 17:
                # stay
                hit = False
            else:
                hit = True
    print('You have {}'.format(player_hand))
    print('The dealer has {}'.format(dealer_hand))
    if sum(player_hand) > sum(dealer_hand):
        print('You Won!')
    else:
        print('You Lose!')


if __name__ == "__main__":
    main()
