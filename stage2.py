data = input()
print("---------")
print("|", data[0],data[1],data[2],"|")
print("|", data[3],data[4],data[5],"|")
print("|", data[6],data[7],data[8],"|")
print("---------")



''' another way
cells = input("Enter cells: ")
DASHES = "-" * 9
print(DASHES)
for row in range(3):
	rowstr = list(cells[3 * row : 3 * row + 3])
	print(f'| {" ".join(rowstr)} |')
print(DASHES)'''
'''
