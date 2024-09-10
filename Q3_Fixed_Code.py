# This is a global variable that can be accessed and modified within functions
global_variable = 100  

# A dictionary with key-value pairs
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process numbers in a list
def process_numbers():
    global global_variable  # This tells Python that we are using the global variable

    local_variable = 5  # Initialise a local variable
    numbers = [1, 2, 3, 4, 5]  # List of numbers to modify

    # Loop until local_variable is greater than 0
    while local_variable > 0:
        if local_variable % 2 == 0:  # If the local variable is even
            numbers.remove(local_variable)  # We remove even numbers from the list
        local_variable -= 1  # Decrease the local variable by 1

    return numbers  # Return the modified list

# Call the function and print the results to verify
print(process_numbers())  # This should print the modified list after processing
