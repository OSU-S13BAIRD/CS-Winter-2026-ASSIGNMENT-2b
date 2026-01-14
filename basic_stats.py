# Author: Sam Baird
# GitHub username: OSU-S13BAIRD
# Date: 01/14/2026
# Description: A Taxicab class that represents a vehicle moving on a 2D grid,
#              tracking both its current position and total distance traveled.


class Taxicab:
    """
    A class representing a taxicab operating on a two-dimensional coordinate plane.
    
    The taxicab maintains its current location and records cumulative distance
    traveled through an odometer that increments with each movement.
    """

    def __init__(self, x_coord, y_coord):
        """
        Constructs a new Taxicab instance at specified coordinates.
        
        Parameters:
            x_coord: Initial horizontal position on the coordinate plane
            y_coord: Initial vertical position on the coordinate plane
        """
        self._x_coord = x_coord
        self._y_coord = y_coord
        self._odometer = 0

    def get_x_coord(self):
        """
        Retrieves the taxicab's current horizontal coordinate.
        
        Returns:
            The current x-coordinate value
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Retrieves the taxicab's current vertical coordinate.
        
        Returns:
            The current y-coordinate value
        """
        return self._y_coord

    def get_odometer(self):
        """
        Retrieves the total distance the taxicab has traveled.
        
        Returns:
            The cumulative odometer reading
        """
        return self._odometer

    def move_x(self, shift):
        """
        Shifts the taxicab's position along the horizontal axis.
        
        Parameters:
            shift: Distance to move (positive for rightward, negative for leftward)
        """
        self._x_coord += shift
        self._odometer += abs(shift)

    def move_y(self, shift):
        """
        Shifts the taxicab's position along the vertical axis.
        
        Parameters:
            shift: Distance to move (positive for upward, negative for downward)
        """
        self._y_coord += shift
        self._odometer += abs(shift)
