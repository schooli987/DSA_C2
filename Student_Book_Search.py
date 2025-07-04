def binary_search_book(book_ids,target_id):
    low=0
    high=len(book_ids)-1

    while low<=high:
        mid=(low+high)//2

        if book_ids[mid]==target_id:
            return mid
        elif book_ids[mid]<target_id:
            low=mid+1
        else:
            high=mid-1
    return -1 

book_ids=[101, 123, 145, 160, 172, 189, 201, 215, 230]

print("Available Book IDs: ",book_ids)
target=int(input("Enter the Book ID to Search for "))

result = binary_search_book(book_ids,target)

if result!=-1:
    print("Found at",result,"position in the list")
else:
    print(target,"not found") 
