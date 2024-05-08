"""Functions used in preparing Guido's gorgeous lasagna.
 
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
 
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(cooked_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - cooked_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate how many minutes it takes to cook layers.
    :param number_of_layers: int - number of layers you want to cook.
    :return: int - total preparation time in minutes (number of layers multiplied to PREPARATION_TIME)
    Function that takes number of layers you want to cook as
    an argument and returns how many minutes it takes to prepare layers of lasagna based on 'PREPARATION_TIME'.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, eclapsed_bake_time):
    """Calculate total number of minutes you've been cooking lasagna.
    :param number_of_layers: int - number of layers of lasagna
    :param eclapsed_bake_time: int - eclapsed cooking time.
    :return: int - total time eclapsed (in minutes) preparing and cooking.
 
    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return number_of_layers * PREPARATION_TIME + eclapsed_bake_time
