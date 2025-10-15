import random

GRID_SIZE = 10
SHIPS = {"Cruiser": 2,"Destroyer": 3, "Battleship": 4,"Aircraft Carrier": 5}

def create_grid():
    opponent_game_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]
    opponent_display_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]
    player_game_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]
    player_display_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]
    
    
    return opponent_game_grid, opponent_display_grid, player_game_grid, player_display_grid

def display_player_grid(player_display_grid):
    print()
    print("###############")
    print("Player 1")
    print("###############")
    for row_num, row in enumerate(player_display_grid):
        display_num = GRID_SIZE - 1 - row_num
        print(f"{display_num}" + " ".join(row))
    
    print(" " + " ".join(str(i) for i in range(GRID_SIZE)))

def display_opponent_grid(opponent_display_grid):
    print()
    print("###############")
    print("Player 2")
    print("###############")
    for row_num, row in enumerate(opponent_display_grid):
        display_num = GRID_SIZE - 1 - row_num
        print(f"{display_num}" + " ".join(row))
 
    print(" " + " ".join(str(i) for i in range(GRID_SIZE)))
 
def create_opponent_ship(opponent_game_grid):
    for ship, size in SHIPS.items():
        while True:
            y = random.randint(0, len(opponent_game_grid[0]) - 1)
            x = random.randint(0, len(opponent_game_grid) - 1)

            is_vertical = random.choice([True, False])

            if is_vertical:
                if x + size > GRID_SIZE:
                    continue

                if '~' not in [opponent_game_grid[x + i][y] for i in range(size)]:
                    continue

                for i in range(size):
                    opponent_game_grid[x + i][y] = ship[0]
            else:
                if y + size > GRID_SIZE:
                    continue

                if '~' not in [opponent_game_grid[x][y + i] for i in range(size)]:
                    continue

                for i in range(size):
                    opponent_game_grid[x][y + i] = ship[0]

            break 

# def display_test_grid(grid):
    # print("\n=== SHIP PLACEMENT TEST ===")
    # for row_num, row in enumerate(grid):
    #     display_num = GRID_SIZE - 1 - row_num
    #     print(f"{display_num} " + " ".join(row))
    # print("  " + " ".join(str(i) for i in range(GRID_SIZE)))
    # print("===========================\n") 

def create_player_ship(player_game_grid):
    for ship, size in SHIPS.items():
        while True:
            y = input("Enter the y coords for ship placement: ")
            x = input("Enter the x coords for ship placement: ")
            
            y = int(y)
            x = int(x)
            # try: 
            #     x_input = int(x)
            #     if not (0 <= x_input < GRID_SIZE):
            #         print("Please enter a value that is present on the grid.")
            #     continue
            # except ValueError:
            #     print("Please enter a numeric value.")
            #     continue
            diagonol = input("Would you like the ship to be vertical? (yes or no): ") 
            if diagonol == "yes":
                is_vertical = True
            
            if is_vertical:
                if x + size > GRID_SIZE:
                    continue

                if '~' not in [player_game_grid[x + i][y] for i in range(size)]:
                    continue

                for i in range(size):
                    player_game_grid[x + i][y] = ship[0]
                
                for row_num, row in enumerate(player_game_grid):
                    display_num = GRID_SIZE - 1 - row_num
                    print(f"{display_num} " + " ".join(row))
                print("  " + " ".join(str(i) for i in range(GRID_SIZE)))
                
            else:
                if y + size > GRID_SIZE:
                    continue

                if '~' not in [player_game_grid[x][y + i] for i in range(size)]:
                    continue

                for i in range(size):
                    player_game_grid[x][y + i] = ship[0]

                for row_num, row in enumerate(player_game_grid):
                    display_num = GRID_SIZE - 1 - row_num
                    print(f"{display_num} " + " ".join(row))
                print("  " + " ".join(str(i) for i in range(GRID_SIZE)))
                    
            break 
                
def player_offence(opponent_game_grid, opponent_display_grid):
    total_ships_cells = sum(SHIPS.values())
    hits = 0
    turn_number = 1
    
    while hits != total_ships_cells:
        print()
        print("###############")
        print(f"Turn {turn_number}: Player 1 Action")
        print("###############")
        x_coord = input("Enter the x coords: ")
        y_coord = input("Enter the y coords: ")
        print("###############")    
        try: 
            x_input = int(x_coord)
            y_input = int(y_coord)
            if not (0 <= x_input < GRID_SIZE and 0 <= y_input < GRID_SIZE):
                print("Please enter a value that is present on the grid.")
                continue
        except ValueError:
            print("Please enter a numeric value.")
            continue
        
        x = x_input
        y = GRID_SIZE - 1 - y_input
        if (0 <= x < len(opponent_game_grid) and 0 <= y < len(opponent_game_grid[0])):  
     
            if opponent_display_grid[y][x] == 'X' or opponent_display_grid[y][x] == 'M':
                print("You've already fired at this location. Try somewhere new!")
                continue
            
            elif (opponent_game_grid[y][x] != '~'):
                hits += 1
                print()
                print("###############")
                print("THAT'S A HIT!!!")
                print("###############")
                print()
                opponent_game_grid[y][x] = 'X'
                opponent_display_grid[y][x] = "X"
                turn_number += 1
            
            elif (opponent_game_grid[y][x] == '~'):
                opponent_game_grid[y][x] = 'M'
                opponent_display_grid[y][x] = 'M'
                print()
                print("###############")
                print("THAT'S A MISS!!!")
                print("###############")
                print() 
                turn_number += 1 
            
        for row_num, row in enumerate(opponent_display_grid):
            display_num = GRID_SIZE - 1 - row_num
            print(f"{display_num}" + " ".join(row))
        
        print(" " + " ".join(str(i) for i in range(len(opponent_display_grid[0]))))
            
    print("YOU WIN, ALL OF THE ENEMY HAS BEEN ELIMINATED.")


if __name__ == "__main__":
    print("Battleships")
    opponent_game_grid, opponent_display_grid, player_game_grid, player_display_grid = create_grid()
    # display_player_grid(player_display_grid)
    # display_opponent_grid(opponent_display_grid)
    # create_opponent_ship(opponent_game_grid)
    create_player_ship(player_game_grid)
    # display_test_grid(opponent_game_grid)
    # player_offence(opponent_game_grid, opponent_display_grid)