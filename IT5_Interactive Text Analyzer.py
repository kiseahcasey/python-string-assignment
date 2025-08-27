#SATURINAS, KISEAH CASEY G.
#IT5L(2770)
def reverse_sentence(sentence):
    return sentence[::-1]

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)

def check_palindrome(sentence):
    cleaned = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned == cleaned[::-1]

def find_and_replace(sentence):
    find_word = input("Enter the word to find: ")
    replace_word = input("Enter the replacement word: ")
    return sentence.replace(find_word, replace_word)

def format_title(sentence):
    return sentence.title()

def split_into_words(sentence):
    return sentence.split()

def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def swap_case(sentence):
    return sentence.swapcase()


# Main program
sentence = input("Enter a sentence: ")

while True:
    print("\nChoose an operation:")
    print("0. Enter a new sentence")
    print("1. Reverse the sentence")
    print("2. Count vowels")
    print("3. Check if palindrome")
    print("4. Find and replace a word")
    print("5. Format (title case)")
    print("6. Split into words")
    print("7. Word frequency counter")
    print("8. Swap case")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        sentence = input("Enter a new sentence: ")
    elif choice == "1":
        print("Reversed:", reverse_sentence(sentence))
    elif choice == "2":
        print("Vowel count:", count_vowels(sentence))
    elif choice == "3":
        print("Palindrome?" , "Yes" if check_palindrome(sentence) else "No")
    elif choice == "4":
        sentence = find_and_replace(sentence)
        print("Updated sentence:", sentence)
    elif choice == "5":
        print("Title case:", format_title(sentence))
    elif choice == "6":
        print("Words:", split_into_words(sentence))
    elif choice == "7":
        print("Word frequencies:", word_frequency(sentence))
    elif choice == "8":
        print("Swap case:", swap_case(sentence))
    elif choice == "9":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
