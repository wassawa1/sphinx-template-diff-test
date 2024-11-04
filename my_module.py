class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object with x and y coordinates.
        
        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

def disp(point):
    """
    Display the coordinates of a Point object.
    
    Args:
        point (Point): The Point object whose coordinates will be displayed.
        
    Returns:
        None: This function prints the coordinates of the point and does not return any value.
    """
    print(f"Point coordinates: ({point.x}, {point.y})")

# Example usage:
p = Point(3, 4)
disp(p)  # Output: Point coordinates: (3, 4)
