def secret_door_challenge():
    print("🚪 Secret Door Challenge – Color Code Access")

    # Step 1: Sorted list of door colors (strings)
    door_colors = ['Amber', 'Blue', 'Emerald', 'Gold', 'Indigo', 'Orange', 'Scarlet', 'Violet']
    print("Available Door Colors:", door_colors)

    # Step 2: Take input from user
    code = input("Enter your assigned door color: ").strip().capitalize()

    # Step 3: Initialize binary search bounds
    low = 0
    high = len(door_colors) - 1
    found = False

    # Step 4: Binary Search loop
    while low <= high:
        mid = (low + high) // 2
        if door_colors[mid] == code:
            print(f"✅ Door '{code}' found! Access granted.")
            found = True
            break
        elif door_colors[mid] < code:
            low = mid + 1
        else:
            high = mid - 1

    # Step 5: Not found condition
    if not found:
        print("❌ Invalid color. Access denied.")

# Run the challenge
secret_door_challenge()

