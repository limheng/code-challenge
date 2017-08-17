# Compress String with character and its count.
# Example: "aaabbba" -> compress -> "a3b3a1”

orig = 'aaaabbbcaaabbc'

new = ''
reps = 0
letter = orig[0]

for char in orig:
    if letter == char:
        reps += 1
    else:
        new += letter + str(reps)
        letter = char
        reps = 1

new += letter + str(reps)

print(new)
