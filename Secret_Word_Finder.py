def secret_word_finder():
    print("Secret Word Finder – Let's play with Binary Search!")
    
    word_list = ["apple", "banana", "cherry", "grape", "kiwi", 
                 "mango", "peach", "pear", "plum", "watermelon"]
    
    word_list.sort()  # Ensure list is sorted
    print("Here's the list of words:")
    print(word_list)

    print("\nChoose a secret word from the list and don’t tell me!")
    input("Press Enter when you're ready...")

    low = 0
    high = len(word_list) - 1
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        guess = word_list[mid]
        print("\n Is your word",guess,"?")
        feedback = input("Type 'Before', 'After', or 'Correct': ").strip().lower()
        attempts += 1

        if feedback == "correct":
            print("I found your secret word",guess,"in",attempts,"tries!")
            break
        elif feedback == "before":
            high = mid - 1
        elif feedback == "after":
            low = mid + 1
        else:
            print("Please enter a valid response: 'Before', 'After', or 'Correct'.")
            attempts -= 1  # Don't count invalid input

    else:
        print(" I couldn't guess it. Did you choose a word from the list?")

secret_word_finder()
