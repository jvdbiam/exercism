"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time_left = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_left 
    

# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time. 

    :param number_of_layers: int - #layers you want to make.
    :return: int - how much time it takes to create 'numbers_of_layers' derived from 'PREPARATION_TIME'.

    Function that takes the amount of layers lasagna you want to make as
    an argument and returns how many minutes you need to prepare the layers
    based on the `PREPARATION_TIME`.
    """
    preparation_time = PREPARATION_TIME * number_of_layers
    return preparation_time
    

def elapsed_time_in_minutes(number_of_layers, elapsed_baking_time):
    """Calculate elpased cooking time.

    :param number_of_layers: int - the amount of layers you have created.
    :param elapsed_baking_time: int - baking time already elapsed.
    :return: int - the total elpased cooking time (in minutes).

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    elapsed_time = elapsed_baking_time + (number_of_layers * PREPARATION_TIME)
    return elapsed_time


#  (you can copy and then alter the one from bake_time_remaining.)
