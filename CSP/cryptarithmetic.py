from itertools import permutations

def solve_cryptarithm(words, result):
    # Get all unique letters in the words and result
    letters = set(''.join(words + [result]))

    # Generate all possible permutations of numbers from 0 to 9 for the letters
    perm_length = len(letters)
    perm_range = range(10)
    permutations_gen = permutations(perm_range, perm_length)

    # Test each permutation
    for permutation in permutations_gen:
        # Map each letter to a number in the permutation
        letter_map = dict(zip(letters, permutation))

        # Evaluate the words and the result using the current letter map
        word_values = [int(''.join(str(letter_map[c]) for c in word)) for word in words]
        result_value = int(''.join(str(letter_map[c]) for c in result))

        # If the sum of the word values equals the result value, return the letter map
        if sum(word_values) == result_value:
            return letter_map

    # If no solution is found, return None
    return None

# Example usage
words = ["TWO","TWO"]
result = "FOUR"
letter_map = solve_cryptarithm(words, result)

if letter_map:
    print(letter_map)
else:
    print('No solution found.')
