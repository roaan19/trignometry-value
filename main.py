import math

# Welcome message
print("Welcome to the Trigonometric Function Calculator!")

# Ask user for angle in degrees
angle_degrees = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate trigonometric values
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = None

# Handle tangent separately to avoid undefined cases
try:
    tan_value = math.tan(angle_radians)
except:
    tan_value = "undefined"

# Print results
print(f"\nTrigonometric values for {angle_degrees}°:")
print("tan({angle_degrees}) =" ,(cos_value))
print("tan({angle_degrees}) =",(sin_value))
print("tan({angle_degrees}) = ",(tan_value))
