import random

people = []

with open('List_Names.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        people.append(line)
        

group_n = int(input('Number of groups: '))
l = [] #list for all groups (lists)
list = [] #single list
n = len(people) // group_n #How many people in one group
extra = len(people) % group_n 

for groups in range(group_n):
    for i in range(n):
        person = random.choice(people)
        list.append(person)
        people.remove(person)
    l.append(list)
    list = []
list_extra_number = []    
while len(people):
    person = random.choice(people)
    extra_in_list = random.randint(0, group_n - 1)
    if extra_in_list not in list_extra_number:
        l[extra_in_list].append(person)
        list_extra_number.append(extra_in_list)
        people.remove(person)


count = 1
print('\n')
with open('Groups.txt', 'w') as file:
    for h in l:
        print('Group_' + str(count) + ' --> ', h)
        h = str(h)
        file.write('Group_' + str(count) + ' --> ' + h + '\n')
        count+=1
        
pause = input()

