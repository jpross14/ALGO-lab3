from __future__ import annotations
from functools import total_ordering

import turtle


@total_ordering
class Point:
    def __init__(self, x: float, y: float):
        # DO NOT MODIFY
        self.x = x
        self.y = y

    def draw(self) -> None:
        # DO NOT MODIFY
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.dot(8, "black")

    def draw_to(self, that: Point) -> None:
        # DO NOT MODIFY
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.pensize(2)
        turtle.pencolor("black")
        turtle.goto(that.x, that.y)

    def __str__(self) -> str:
        # DO NOT MODIFY
        return f"({self.x}, {self.y})"
    
    def _is_valid_operand(self, that: object) -> bool:
        # DO NOT MODIFY
        return isinstance(that, Point)

    def __lt__(self, that: Point) -> bool:
        # use _is_valid_operand above to check if `that` is a Point and raise an error if it isn't a Point object
        if not self._is_valid_operand(that):
            raise TypeError("Operand must be Point object")
        return (self.y, self.x) < (that.y, that.x)

    def __eq__(self, that: Point) -> bool:
        # use _is_valid_operand above to check if `that` is a Point and raise an error if it isn't a Point object
        if not self._is_valid_operand(that):
            return False
        return self.x == that.x and self.y == that.y

    def slope_to(self, that: Point) -> float:
        # calculate the slope from this to that Point
        if self == that:
            return float('-inf')
        if self.x == that.x:
            return float('inf')
        if self.y == that.y:
            return 0.0
        return (that.y - self.y) / (that.x - self.x)
        # m = (y2 - y1) / (x2 - x1)
    
    @staticmethod
    def main():
        LENGTH = 800
        WIDTH = 600
        MARGIN = 50

        # Initialize turtle screen
        screen = turtle.Screen()
        screen.setup(LENGTH, WIDTH)

        # Transfer the point of origin to the bottom left
        screen.setworldcoordinates(-MARGIN, -MARGIN, LENGTH - MARGIN, WIDTH - MARGIN)
        turtle.hideturtle()

        # Create points
        p1 = Point(0, 0)
        p2 = Point(150, 200)

        # Draw points
        p1.draw()
        p2.draw()

        # Draw line between points
        p1.draw_to(p2)

        # Calculate slope (uncomment this if you have implemented slope_to)
        print("Slope between p1 and p2:", p1.slope_to(p2))

        # Keep the window open
        turtle.done()


# Example usage
if __name__ == "__main__":
    Point.main()
