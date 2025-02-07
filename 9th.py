# 9.i have one file which contain fidelity as text write class which calculate how many time fidelity is present
def count_occurrences(text, word):
    n = len(text)
    m = len(word)
    count = 0
    
    for i in range(n - m + 1):  # Loop through the text
        if text[i:i + m] == word:  # Compare substrings
            count += 1
            
    return count

# Read from a file
filename = "fidelity.txt"  # Change this to your actual file name

try:
    with open(filename, "r") as file:
        text = file.read()  # Read file content
    
    word = "fidelity"
    result = count_occurrences(text, word)
    
    print(f"Number of occurrences of '{word}':", result)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

     