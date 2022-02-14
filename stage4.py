cells = input('Enter cells: ', )
cells = cells.replace("_"," ")
cells = list(cells)
cell = []
print("---------")
print("|" + " " + cells[0] +" " + cells[1] + " " + cells[2] + " " +"|")
print("|" + " " + cells[3] +" " + cells[4] + " " + cells[5] + " " +"|")
print("|" + " " + cells[6] +" " + cells[7] + " " + cells[8] + " " +"|")
print("---------")

position = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']

for ele in cells:
    cell.append(ele)
while True:
    c = input('Enter the coordinates: ', )
    d = c.split()
    e = d[0].isdigit() and d[1].isdigit()
    if e == False:
        print('You should enter numbers!')
    elif e == True:
        f = abs(int(d[0]))
        g = abs(int(d[1]))
        if f > 3 or g > 3:
            print('Coordinates should be from 1 to 3!')
        else:
            x = position.index(c)
            if cells[x] != ' ':
                print('This cell is occupied! Choose another one!')
            else:
                cell = cell[:x] + ['X'] + cell[x+1:]
                print("---------")
                print("|" + " " + cell[0] +" " + cell[1] + " " + cell[2] + " " +"|")
                print("|" + " " + cell[3] +" " + cell[4] + " " + cell[5] + " " +"|")
                print("|" + " " + cell[6] +" " + cell[7] + " " + cell[8] + " " +"|")
                print("---------")
                break 
