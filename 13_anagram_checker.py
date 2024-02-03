# Anagram Checker

# pseudo code
#
#       get letters in string 1 + 2
#       if letters in string 1 == 2
#           print True
#       else
#           print False


def get_letters(str1):
    letters_in_string = []

    for char in str1:
        if char.isalpha():
            letters_in_string.append(char)

    return letters_in_string


def are_anagrams(str1, str2):
    letters_in_str1 = get_letters(str1)
    letters_in_str2 = get_letters(str2)

    return sorted(letters_in_str1) == sorted(letters_in_str2)


def main():
    word1 = "listen"
    word2 = "silent"
    result1 = are_anagrams(word1, word2)
    print(f"{word1} / {word2} ")

    word3 = "hello"
    word4 = "world"
    result2 = are_anagrams(word3, word4)
    print(f"{word3} / {word4} ")

    return result1, result2


if __name__ == "__main__":
    results = main()


print("Result for the first test:", results[0])
print("Result for the first test:", results[1])
