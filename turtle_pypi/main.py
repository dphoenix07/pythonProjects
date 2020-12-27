# Day 16 of 100 Days of Code with Python Notes

# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
#
# # Tap into methods
# timmy.shape("turtle")
# timmy.color("cyan2")
# timmy.forward(100)
#
# my_screen = Screen()
# # Print my_screen attribute 'canvheight'
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

# Build a pokedex with pokemon names and type
from prettytable import PrettyTable
table = PrettyTable()

# Populate table
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])

# Change table style to make the columns left align
table.align = "l"

print(table)



