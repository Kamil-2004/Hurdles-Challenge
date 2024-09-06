logo = """



.   .            . .            .--..         . .                   
|   |            | |           :    |         | |                   
|---|.  . .--..-.| | .-. .--.  |    |--. .-.  | | .-. .--. .-.. .-. 
|   ||  | |  (   | |(.-' `--.  :    |  |(   ) | |(.-' |  |(   |(.-' 
'   '`--`-'   `-'`-`-`--'`--'   `--''  `-`-'`-`-`-`--''  `-`-`| `--'
._.'     

"""
print(logo)



import random

# Functions to simulate character actions
def move():
    print(f"Position {position}: Moving forward")

def short_jump():
    print(f"Position {position}: Short jump over a small hurdle")

def long_jump():
    print(f"Position {position}: Long jump over a large hurdle")

def climb():
    print(f"Position {position}: Climbing over a very tall hurdle")

def at_goal():
    return position > total_positions

# Function to determine the type of action based on hurdle height
def jump(hurdle_height):
    if hurdle_height == 1:
        short_jump()
    elif hurdle_height == 2:
        long_jump()
    elif hurdle_height == 3:
        climb()
    else:
        move()

# Environment setup
total_positions = 10  # Total number of positions in the course
hurdles = {i: random.randint(1, 3) for i in range(1, total_positions) if random.choice([True, False])}

# Print the hurdle setup
print(f"Hurdles setup (Position: Height): {hurdles}")

# Starting the simulation
position = 1

while not at_goal():
    if position in hurdles:
        jump(hurdles[position])
    else:
        move()
    position += 1  # Move to the next position

print("Reached the goal!")
