'''Imagine we have a grid with a width and height that have been stored in memory. Each
	tile on the grid is numbered, starting at tile 1 in the top left corner. Write a
	program that, given a tile number, returns “edge” or “inside” depending on whether or
	not the tile is at the edge of the grid or not.

Test Suite: too big to put in here, just draw it!
width: 5, height: 6
		1	2	3	4	5
		6	7	8	9	10
		11	12	13	14	15
		16	17	18	19	20
		21	22	23	24	25
		26	27	28	29	30
For instance, 7 is inside, while 20 is edge '''

height = int(input("The height of the array?"))
width = int(input("The width of the array?"))
tile = int(input("Enter a tile value:"))

# well, let's calculate the tile's position first
# the row number
tileRow = (tile - 1) // width + 1
# the column number
tileColumn = (tile - 1) % width + 1
# if the above formulas do not make sense, plug in some numbers

# if it's on the first or last row, or the first or last column
# it's an edge
if tileRow == 1 or tileRow == height or tileColumn == 1 or tileColumn == width:
	print("What an edgy tile!")
else:
	print("This is an inside tile")