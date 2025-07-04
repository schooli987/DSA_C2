def crack_the_vault():
    codes = list(range(1000, 2000, 25))  # Sorted list of possible codes
    print("The robot will try to guess your secret 4-digit code.")
    print("Choose a secret code from this list:\n",codes)
    input("Press Enter when you're ready...")

    low = 0
    high = len(codes) - 1
    attempts = 0

    while low <= high:
        mid = (low + high) // 2
        guess = codes[mid]
        print("Robot's guess:",guess)
        response = input("Enter 'Too low', 'Too high', or 'Correct': ").strip().lower()
        attempts += 1

        if response == "correct":
            print("Vault cracked in",attempts,"tries! Code:" ,guess)
            break
        elif response == "too low":
            low = mid + 1
        elif response == "too high":
            high = mid - 1
        else:
            print("Invalid input. Please respond with 'Too low', 'Too high', or 'Correct'.")

crack_the_vault()
