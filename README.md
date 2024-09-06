# About
This script creates a virtual obstacle course with random hurdles of varying heights. A character starts at position 1 and moves forward, jumping or climbing over hurdles as needed. The goal is to reach the end of the course.

# How it Works
The script sets up a course with a specified number of positions (default: 10).
Random hurdles are generated at some positions, with heights ranging from 1 to 3.
The character starts at position 1 and moves forward, checking for hurdles at each position.
If a hurdle is encountered, the character performs an action based on the hurdle height:
Height 1: Short jump
Height 2: Long jump
Height 3: Climb
No hurdle: Move forward
The character continues moving until reaching the end of the course.
# Usage
Save this script as obstacle_course.py (or any other name with a .py extension).
Run the script using Python: python obstacle_course.py
Watch the character navigate the obstacle course!
# Contributing
Feel free to modify or extend this script to create more interesting obstacle courses or character actions!
