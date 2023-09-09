from random import randint
import array

rows, cols = (9, 9)
game = [[0 for i in range(cols)] for j in range(rows)]

occur = 0
ind = 0
dump = []
isin = 0

#This Section Takes care of the rows

for i in range(cols):              #this loop adds random between 1 and 9 numbers into the game
    for j in range(rows):
        game[i][j] = randint(1,9)

for j in range(cols): #The following code 
    
    dump.clear()
        
    for i in range(cols): #this loop copies the first row to a dump list
        dump.append(game[j][i])

    #Start of Loop that ensures that a row is correct
    for i in range(cols):
        occur = dump.count(dump[i])     #counts the number of occurences of the number at index i
        ind = dump.index(dump[i])       #finds the first occurence of this number

        if occur == 1:
            True
        else: #this makes sure that a number only occurs once in a row
            while occur > 1:
                isin = randint(1,9)
                if isin in dump:
                    isin = randint(1,9)
                else:
                    dump[ind] = isin
                    occur = occur-1
        #End of Loop

    for i in range(cols):
        game[j][i] = dump[i]


#This Section Takes Care of the Columns
array = []
count = 1
add = 1
check = 0
holder = 0

for i in range(cols):#this is the loop going through columns
    array.clear()
    while count < cols:#this loop goes through all the rows except for the 0th row
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

print("")
print("Solution") 
for rows in game:
    print(rows)




