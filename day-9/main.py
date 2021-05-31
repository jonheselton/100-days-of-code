#!/usr/bin/env python
from art import logo


def compare_bids(bid_list):
    max_bidder = ''
    max_bid = 0
    for k, v in bid_list.items():
        if v >= max_bid:
            max_bid = v
            max_bidder = k
    return {max_bidder:max_bid}


another_bidder = True
bids = {}
while another_bidder:
    print(logo)
    name = input('What is your name? ')
    bid = float(input('what is your bid?'))
    bids[name] = bid
    if input('is there another bidder y/n? ') == 'n':
        another_bidder = False
print(bids)
print(compare_bids(bids))
