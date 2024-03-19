def remove_common_letters(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    for letter in name1:
        if letter in name2:
            name1 = name1.replace(letter, '', 1)
            name2 = name2.replace(letter, '', 1)

    return name1, name2

def count_remaining_letters(name1, name2):
    return len(name1) + len(name2)

def calculate_flames(remaining_letters):
    flames = ['Friend', 'Love', 'Affection', 'Marriage', 'Enemy', 'Sibling']
    index = (remaining_letters - 1) % len(flames)
    return flames[index]

# Start
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Remove common letters
name1, name2 = remove_common_letters(name1, name2)

# Count remaining letters
remaining_letters = count_remaining_letters(name1, name2)

# Calculate FLAMES
result = calculate_flames(remaining_letters)

# Print the relationship result
print("Relationship result between", name1, "and", name2, "is:", result)
# End
