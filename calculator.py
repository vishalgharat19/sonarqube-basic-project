import os
import subprocess
import hashlib
import pickle


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    # BUG: division by zero is not handled
    return a / b


def get_item(items, index):
    # BUG: possible IndexError
    return items[index]


def calculate_average(numbers):
    # BUG: empty list causes ZeroDivisionError
    return sum(numbers) / len(numbers)


def run_command(user_input):
    # VULNERABILITY: command injection
    return os.system("echo " + user_input)


def execute_command(user_input):
    # VULNERABILITY: shell command constructed from user input
    return subprocess.call(user_input, shell=True)


def insecure_hash(password):
    # SECURITY HOTSPOT: MD5 is unsuitable for passwords
    return hashlib.md5(password.encode()).hexdigest()


def load_data(data):
    # SECURITY HOTSPOT / VULNERABILITY: unsafe deserialization
    return pickle.loads(data)


def get_secret():
    # SECURITY HOTSPOT: hard-coded credential/secret
    password = "SuperSecretPassword123"
    return password


def old_calculation(a, b):
    # CODE SMELL / TECHNICAL DEBT: duplicated/unnecessary logic
    result = a + b
    return result


def very_long_function(a, b, c, d, e):
    # CODE SMELL: unnecessarily complicated function
    result = a + b
    result = result * c
    result = result - d
    result = result / e
    result = result + 10
    result = result * 2
    result = result - 5
    result = result + 100
    return result
