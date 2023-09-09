from random import randint
import array
array = []
rows = 9
cols = 9
count = 1
add = 1
check = 0
holder = 0

#game = [[0 for i in range(cols)] for j in range(rows)]
game = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]#test 2d array

#for i in range(cols):              #this loop adds random between 1 and 9 numbers into the game
#    for j in range(rows):
#        game[i][j] = randint(1,9)

for i in range(cols):#this is the loop going through columns
    array.clear()
    while count < 9:#this loop goes through all the rows except for the 0th row
        add = game[count-1][i]
        array.append(add)

        check = game[count][i]

        while check in array:
            holder = game[count][cols-1]
            game[count].insert(i,holder)
            game[count].pop(cols)
            check = holder

        
        count = count + 1
        
    print(array)
    count = 1

for rows in game:
    print(rows)
