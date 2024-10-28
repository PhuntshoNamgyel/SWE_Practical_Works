## Step 1: Open and Read a Text File

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Test the function
content = read_file('sample.txt')
print(content[:100])  # Print the first 100 characters


## Step 2: Count the Number of Lines

def count_lines(content):
    # Split the content by newline characters to get each line
    # The number of lines is the length of the resulting list
    return len(content.split('\n'))

# Test the function
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")


## Step 3: Count Words
def count_words(content):
    return len(content.split())

# Test the function
num_words = count_words(content)
print(f"Number of words: {num_words}")


## Step 4: Find the Most Common Word
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# Test the function
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")


## Step 5: Calculate Average Word Length

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

# Test the function
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")


## Step 6: Count Unique Words

def count_unique_words(content):
    # Convert all words to lowercase for case-insensitivity and split them
    words = content.lower().split()
    # Use a set to store unique words, as sets automatically handle duplicates
    unique_words = set(words)
    return len(unique_words)  # Return the count of unique words

# Test the function
num_unique_words = count_unique_words(content)
print(f"Number of unique words: {num_unique_words}")


## Step 7: Find the Longest Word

def find_longest_word(content):
    # Split content into words and find the word with the maximum length
    longest_word = max(content.split(), key=len)
    return longest_word  # Return the longest word

# Test the function
longest_word = find_longest_word(content)
print(f"Longest word: '{longest_word}'")


## Step 8: Count Occurrences of a Specific Word (Case-Insensitive)

def count_specific_word(content, target_word):
    # Split content into lowercase words and convert target_word to lowercase
    words = content.lower().split()
    target_word = target_word.lower()
    # Count occurrences of target_word in the list of words
    return words.count(target_word)

# Test the function
target_word = "Esports"
specific_word_count = count_specific_word(content, target_word)
print(f"The word '{target_word}' appears {specific_word_count} times")


## Step 9: Calculate Percentage of Words Longer Than Average Length

def percentage_longer_than_average(content):
    # Split content into words
    words = content.split()
    # Calculate the average word length using the function defined earlier
    avg_length = average_word_length(content)
    # Count how many words are longer than the average length
    longer_than_avg_count = sum(1 for word in words if len(word) > avg_length)
    # Calculate the percentage of words longer than the average length
    return (longer_than_avg_count / len(words)) * 100

# Test the function
percentage_longer = percentage_longer_than_average(content)
print(f"Percentage of words longer than average length: {percentage_longer:.2f}%")


## Step 10: Combine Everything into a Main Function

def analyze_text(filename, target_word=None):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    num_unique_words = count_unique_words(content)
    longest_word = find_longest_word(content)
    percentage_longer = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Longest word: '{longest_word}'")
    print(f"Percentage of words longer than average length: {percentage_longer:.2f}%")
    
    if target_word:
        specific_word_count = count_specific_word(content, target_word)
        print(f"The word '{target_word}' appears {specific_word_count} times")

# Run the analysis function
analyze_text('sample.txt', target_word="Esports")
