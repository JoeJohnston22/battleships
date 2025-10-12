import random

def create_grid():
    width = int(input("Declare the width of the grid: "))
    height = int(input("Declare the height of the grid: "))

    opponent_game_grid = [['~' for _ in range(width)] for _ in range(height)]
    opponent_display_grid = [['~' for _ in range(width)] for _ in range(height)]
    player_display_grid = [['~' for _ in range(width)] for _ in range(height)]
    
    
    return opponent_game_grid, opponent_display_grid, player_display_grid, width

def display_player_grid(player_display_grid, width):
    print()
    print("###############")
    print("Player 1")
    print("###############")
    print(" " + " ".join(str(i) for i in range(width)))
    for row_num, row in enumerate(player_display_grid):
        print(f"{row_num} " + " ".join(row))

def display_opponent_grid(opponent_display_grid, width):
    print()
    print("###############")
    print("Player 2")
    print("###############")
    print(" " + " ".join(str(i) for i in range(width)))
    for row_num, row in enumerate(opponent_display_grid):
        print(f"{row_num} " + " ".join(row))

def create_opponent_ship(opponent_game_grid, width):
    num_ship = 4
    ship = 's'
    
    print(" " + " ".join(str(i) for i in range(width)))

    for _ in range(num_ship):
        while True:
            y = random.randint(0, len(opponent_game_grid[0]) - 1)
            x = random.randint(0, len(opponent_game_grid) - 1)
            
            if opponent_game_grid[y][x] == '~':
                opponent_game_grid[y][x] = ship
                break

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
        y = int(y_coord)
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
                
        print("\n   " + " ".join(str(i) for i in range(len(opponent_display_grid[0]))))  
        for row_num, row in enumerate(opponent_display_grid):
            print(f"{row_num}  " + " ".join(row))  
    print("YOU WIN, ALL OF THE ENEMY HAS BEEN ELIMINATED.")


if __name__ == "__main__":
    print("Battleships")
    opponent_game_grid, opponent_display_grid, player_display_grid, width = create_grid()
    display_player_grid(player_display_grid, width)
    display_opponent_grid(opponent_display_grid, width)
    create_opponent_ship(opponent_game_grid, width)
    player_offence(opponent_game_grid, opponent_display_grid)