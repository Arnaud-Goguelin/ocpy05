class Rectangle:
    """
    Represents a geometric rectangle and provides methods to calculate its area and perimeter.

    Attributes:
        width (int | float): The width of the rectangle, it must be a positive number.
        length (int | float): The length of the rectangle, it must be a positive number.
    """

    def __init__(self, width: int | float, length: int | float) -> None:
        self.width = self.__validate_side(width)
        self.length = self.__validate_side(length)

    @property
    def width(self) -> int | float:
        """Getter for width"""
        return self._width

    @width.setter
    def width(self, value):
        """setter for width"""
        self._width = self.__validate_side(value)

    @property
    def length(self) -> int | float:
        """Getter for length"""
        return self._length

    @length.setter
    def length(self, value):
        """setter for length"""
        self._length = self.__validate_side(value)

    @staticmethod
    def __validate_side(value: int | float) -> int | float:
        """Validates that a given value is a positive number."""
        if not isinstance(value, (int, float)):
            raise TypeError("Side must be a number")
        if value <= 0:
            raise ValueError("Side must be greater than 0")
        return value

    # use method to respect exercise, yet @property should be easier
    def calculate_area(self) -> int | float:
        """Calculates the area of the rectangle."""
        return self.width * self.length

    def calculate_perimeter(self) -> int | float:
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.length)

    def __str__(self) -> str:
        return (f"Rectangle with width = {self.width}, length = {self.length}, "
                f"perimeter = {self.calculate_perimeter()}, and area = {self.calculate_area()}.")


if __name__ == "__main__":
    try:
        rectangle = Rectangle(5, 3)  # 5:width & 3:length
        print("Width:", rectangle.width)
        print("Length:", rectangle.length)
        print("Area:", rectangle.calculate_area())
        print("Perimeter:", rectangle.calculate_perimeter())
        print(rectangle.__str__())
    except (ValueError, TypeError) as error:
        print("An error happened:")
        print(error)
