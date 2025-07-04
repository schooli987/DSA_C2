def robot_guess_book_id():
    print("Robot will guess your secret Book_id!")
    print("Choose a number between 1 and 100 (but don’t tell me)")

    input("Press Enter when you are ready")

    low=1
    high=100
    attempts=0

    while low<=high:
        mid=(low+high)//2
        print("Is your Book ID",mid,"?")
        feedback=input("Enter 'Too low','Too high',or 'correct':").strip().lower()
        attempts +=1

        if feedback== 'correct':
            print("Yay! I guessed it in" ,attempts ,"tries")
            break
        elif feedback == 'too low':
            low=mid+1
        elif feedback == 'too high':
            high =mid-1
        else:
            print("Please enter a valid response")
            attempts -= 1

robot_guess_book_id()
