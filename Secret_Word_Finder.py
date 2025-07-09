def secret_word_finder_from_text():
    print("Secret Word Finder")
    
    # Get sentence input
    sentence = input("Enter a sentence or paragraph: ").lower()
    words = sorted(sentence.split())  # Sort the words for binary search
    
    # Display sorted word list (optional for debugging)
    print("Sorted words:", words)

    # Get the word to search
    target = input("Enter the secret word to find: ").strip().lower()

    # Binary Search
    low = 0
    high = len(words) - 1

    while low <= high:
        mid = (low + high) // 2
        if words[mid] == target:
            print("✅ Secret word found!")
            return
        elif words[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print("❌ Secret word not found.")

# Run the game
secret_word_finder_from_text()
