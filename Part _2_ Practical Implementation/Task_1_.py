# AI-suggested code (using GitHub Copilot):

def sort_list_of_dicts_ai(list_of_dicts_ai, key):
    
    return sorted(list_of_dicts_ai, key=lambda x: x[key])      
 
# Manual code implementation :

def sort_list_of_dicts_manual(data, key):
    """Sort a list of dictionaries by a specific key using manual implementation"""
    # Using bubble sort for educational purposes
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# Example usage
sample_data = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 22}
]

# Test both implementations
print("AI Version:", sort_list_of_dicts_ai(sample_data.copy(), 'age'))
print("Manual Version:", sort_list_of_dicts_manual(sample_data.copy(), 'age'))

# Analysis :
# The AI-suggested code uses a lambda function to sort the list of dictionaries based on the specified key. 
# The manual implementation using itemgetter might be more efficient for large lists because itemgetter is implemented in C and can be faster than a lambda. 
# However, for small lists, the difference is negligible. 
# The AI version is perfectly acceptable and reduces development time.
