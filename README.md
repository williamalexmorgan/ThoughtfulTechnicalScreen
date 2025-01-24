# ThoughtfulTechnicalScreen

# Package Sorting Function

This program categorizes packages into three categories: **STANDARD**, **SPECIAL**, and **REJECTED**, based on their dimensions and weight.

## Categorization Rules
1. **Bulky**: A package is considered bulky if:
   - Its volume (width × height × length) is at least 1,000,000 cm³
   - Its dimensions are 150 cm or greater.

2. **Heavy**: A package is considered heavy if its weight is over 20 kg.

3. **Categories**:
   - **REJECTED**: The package is both bulky and heavy.
   - **SPECIAL**: The package is either bulky or heavy.
   - **STANDARD**: The package is neither bulky nor heavy.

## How to Use
1. Include the `sort` function in your Python program.
2. Call the function with the following parameters:
   - `width`: Width of the package in centimeters.
   - `height`: Height of the package in centimeters.
   - `length`: Length of the package in centimeters.
   - `mass`: Mass of the package in kilograms.

3. The function returns a string indicating the category:
   - `"STANDARD"`
   - `"SPECIAL"`
   - `"REJECTED"`

## Example
```python
print(sort(100, 100, 100, 25))  # Outputs: "SPECIAL"
print(sort(200, 200, 200, 10))  # Outputs: "SPECIAL"
print(sort(200, 200, 200, 25))  # Outputs: "REJECTED"
print(sort(50, 50, 50, 10))     # Outputs: "STANDARD"
