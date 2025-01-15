#14 Given a string, count how many vowels (a, e, i, o, u) it contains.
# didnt understand btw
def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in "aeiou":
            count += 1
    return count

input_string = input("Enter a string: ")
print("Number of vowels:", count_vowels(input_string))