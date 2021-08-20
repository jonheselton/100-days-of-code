##!/usr/bin/python

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


def main():
    user_1 = User('001', 'Jon')
    user_2 = User('002', 'Carl')
    user_1.follow(user_2)
    print(user_1.following)


if __name__ == "__main__":
    main()
