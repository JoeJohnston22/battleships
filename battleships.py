import random

def create_grid():
    width = int(input("Declare the width of the grid: "))
    height = int(input("Declare the height of the grid: "))

    grid = [['~' for _ in range(width)] for _ in range(height)]

    # print("   " + " ".join(str(i) for i in range(width)))

    # for row_num in range(height):
    #     print(f"{row_num}  " + " ".join(["~"] * width))
    
    return grid, width
        

def create_ship(grid, width):
    num_ship = 4
    ship = 's'
    
    print("   " + " ".join(str(i) for i in range(width)))

    for _ in range(num_ship):
        while True:
            x = random.randint(0, len(grid) - 1)
            y = random.randint(1, len(grid[0]) - 1)
            
            if grid[y][x] == '~':
                grid[y][x] = ship
                break
            
    for row_num, row in enumerate(grid):
        print(f"{row_num}  " + " ".join(row))
        

def ouch(grid):
    num_ships = 4
    while num_ships > 0:
        x_coord = input("Enter the x coords: ")
        y_coord = input("Enter the y coords: ")
        x = int(x_coord)
        y = int(y_coord)
        # print(grid)
        if (0 <= x < len(grid) and 0 <= y < len(grid[0])):  
        
            if (grid[y][x] == 's'):
                num_ships -= 1 
                print("THAT'S A HIT!!!") 
                grid[y][x] = 'X'
                # for row in grid:
                #     print(" ".join(row))
            
            elif (grid[y][x] == '~'):
                grid[y][x] = 'M'
                print("THAT'S A MISS!!!")
                # for row in grid:
                #     print(" ".join(row))   

        print("\n   " + " ".join(str(i) for i in range(len(grid[0]))))  
        for row_num, row in enumerate(grid):
            print(f"{row_num}  " + " ".join(row))  
        
    print("YOU WIN, ALL OF THE ENEMY HAS BEEN ELIMINATED.")


if __name__ == "__main__":
    print("Battleships")
    grid, width = create_grid()
    create_ship(grid, width)
    ouch(grid)