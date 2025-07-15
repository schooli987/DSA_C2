def secret_door_challenge():
    print("🚪 Secret Door Challenge – Find your door code in the list!")

    # Step 1: Sorted list of door codes
    door_codes = [1001, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200]
    print("Available Door Codes:", door_codes)

    # Step 2: Ask student to enter their code
    code = int(input("Enter your assigned door code: "))

    # Step 3: Initialize search range
    low = 0
    high = len(door_codes) - 1
    found = False

    # Step 4: Start Binary Search loop
    while low <= high:
        mid = (low + high) // 2

        if door_codes[mid] == code:
            print(f"✅ Door code {code} found! Door unlocked.")
            found = True
            break
        elif door_codes[mid] < code:
            low = mid + 1
        else:
            high = mid - 1

    # Step 5: If not found
    if not found:
        print("❌ Access Denied. Code not found.")

# Run the game
secret_door_challenge()
