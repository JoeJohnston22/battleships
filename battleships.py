import random

GRID_SIZE = 10
SHIPS = {"Cruiser": 2,"Destroyer": 3, "Battleship": 4,"Aircraft Carrier": 5}

def create_grid():
    opponent_game_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]
    opponent_display_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]
    player_display_grid = [['~'] * GRID_SIZE for _ in range(GRID_SIZE)]
    
    
    return opponent_game_grid, opponent_display_grid, player_display_grid

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
    
# create_aircraft_carrier():       
# create_battleship():
# create_destroyer():
# create_cruiser():
    
def create_opponent_ship(opponent_game_grid):
    num_ship = 4
    ship = 's'
    
    for _ in range(num_ship):
        while True:
            y = random.randint(0, len(opponent_game_grid[0]) - 1)
            x = random.randint(0, len(opponent_game_grid) - 1)
            
            if opponent_game_grid[y][x] == '~':
                opponent_game_grid[y][x] = ship
                break
    # print(opponent_game_grid)
    
def player_offence(opponent_game_grid, opponent_display_grid):
    num_ships = 4
    turn_number = 1
    
    while num_ships > 0:
        print()
        print("###############")
        print(f"Turn {turn_number}: Player 1 Action")
        print("###############")
        x_coord = input("Enter the x coords: ")
        y_coord = input("Enter the y coords: ")
        print("###############")
        x = int(x_coord)
        y_input = int(y_coord)
        y = GRID_SIZE - 1 - y_input
        if (0 <= x < len(opponent_game_grid) and 0 <= y < len(opponent_game_grid[0])):  
        
            if (opponent_game_grid[y][x] == 's'):
                num_ships -= 1 
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
                opponent_display_grid[y][x] = "M"
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
    opponent_game_grid, opponent_display_grid, player_display_grid = create_grid()
    display_player_grid(player_display_grid)
    display_opponent_grid(opponent_display_grid)
    create_opponent_ship(opponent_game_grid)
    player_offence(opponent_game_grid, opponent_display_grid)