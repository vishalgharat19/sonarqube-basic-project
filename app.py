from calculator import (
    add,
    subtract,
    divide,
    get_item,
    calculate_average,
    run_command,
    insecure_hash,
    get_secret,
    old_calculation,
)

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Division:", divide(10, 5))

# Bug examples
numbers = [10, 20, 30]
print("Item:", get_item(numbers, 10))
print("Average:", calculate_average([]))

# Security examples
run_command("hello")
print("Hash:", insecure_hash("password123"))
print("Secret:", get_secret())

# Technical debt / code smell
print("Old calculation:", old_calculation(10, 5))
