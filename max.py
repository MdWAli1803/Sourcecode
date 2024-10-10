def find_max(arr):
    if not arr:
        return None  # Return None if the array is empty
    
    max_element = arr[0]  # Assume the first element is the max
    for num in arr:
        if num > max_element:
            max_element = num  # Update max_element if a larger number is found
            
    return max_element

# Example usage
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_value = find_max(array)
print(f"The maximum element in the array is: {max_value}")
