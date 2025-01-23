def sort(width, height, length, mass):
    
    # Calculate if the package is bulky (while using the ternary operator as the instructions specified)
    isBulky = True if ((width * height * length) >= 1_000_000 | max(width, height, length) >= 150) else False

    # Calculate if the package is heavy
    isHeavy = (mass >= 20)

    # Determine the stack using a match statement
    match (isBulky, isHeavy):
        case (True, True):
            return "REJECTED"
        case (True, False) | (False, True):
            return "SPECIAL"
        case (False, False):
            return "STANDARD"

# Example usage
print(sort(100, 100, 100, 25))  # Output: "SPECIAL"
print(sort(200, 200, 200, 10))  # Output: "SPECIAL"
print(sort(200, 200, 200, 25))  # Output: "REJECTED"
print(sort(50, 50, 50, 10))     # Output: "STANDARD"
