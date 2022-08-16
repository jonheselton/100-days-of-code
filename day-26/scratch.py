##!/usr/bin/python
list = [1,2,3,4,5,6]
new_list = [n+1 for n in list]
#print(new_list)
import random
names = ['alex', 'beth', 'roger', 'todd', 'ralph', 'linda', 'jessica', 'sarah']
# long_names = [n.upper() for n in names if len(n) > 4]
# print(long_names)
students = {name:random.randint(1,100) for name in names}
#print(students)
passed_students = {key:value for (key, value) in students.items() if int(value) > 50}
print(passed_students)
def main():
    pass

if __name__ == "__main__":
    main()
    
    