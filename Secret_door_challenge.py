def secret_door_challenge():
    print("🚪 Secret Door Challenge – Find your door code in the list!")
    door_codes = [1001, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200]
    print("Available Door Codes:", door_codes)

    code = int(input("Enter your assigned door code: "))

    low = 0
    high = len(door_codes) - 1
    found = False

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

    if not found:
        print("❌ Access Denied. Code not found.")

secret_door_challenge()
