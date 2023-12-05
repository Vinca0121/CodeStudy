# Function to remove consecutive duplicate letters
def remove_duplicates(string):
    deduped_string = ''
    for char in string:
        if len(deduped_string) == 0 or char != deduped_string[-1]:
            deduped_string += char
    return deduped_string

# Read the number of data sets
num_datasets = int(input())

# Process each data set
for _ in range(num_datasets):
    # Read each string
    input_string = input().strip()
    
    # Remove consecutive duplicates
    result = remove_duplicates(input_string)
    
    # Print the deduped string
    print(result)
