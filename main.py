# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    list_word = list(word)
    list_anagram = list(anagram)

    arranged_word = sorted(list_word)
    arranged_anagram = sorted(list_anagram)

    if arranged_word == arranged_anagram:
        return True
    else:
        return False

print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
print(find_anagram("laid", "dial"))
print(find_anagram("timber", "broken"))
print(find_anagram("wells", "swell"))

