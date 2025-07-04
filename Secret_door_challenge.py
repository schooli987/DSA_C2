def secret_door_game():
    print("Think of a secret door number between 1 and 50")
    input("Press Enter when you're ready...")

    low = 1
    high = 50
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        print("Is the secret door",mid,"?")
        response = input("Enter 'Too low', 'Too high', or 'Correct': ").strip().lower()
        attempts += 1

        if response == "correct":
            print("Hooray! I found the secret door in", attempts,"tries!")
            break
        elif response == "too low":
            low = mid + 1
        elif response == "too high":
            high = mid - 1
        else:
            print("Please enter a valid response")

secret_door_game()
