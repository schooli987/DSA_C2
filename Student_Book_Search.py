import random

def book_id_search_challenge():
    print("Welcome to the Book ID Finder Challenge!")

    # Step 1: Generate a large sorted list of random Book IDs
    book_ids = sorted(random.sample(range(1000, 9999), 100))  # 100 unique IDs between 1000–9999

    # Step 2: Display available Book IDs
    print("Available Book IDs:\n", book_ids)

    # Step 3: Ask student for the Book ID to search
    try:
        target = int(input("\nEnter the Book ID you want to search for: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Step 4: Binary Search Logic
    low = 0
    high = len(book_ids) - 1
    found = False

    while low <= high:
        mid = (low + high) // 2
        if book_ids[mid] == target:
            print(f"Book ID {target} found at position {mid} in the list!")
            found = True
            break
        elif book_ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Step 5: If not found
    if not found:
        print("Book ID not found in the list.")

# Run the search
book_id_search_challenge()
