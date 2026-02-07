books=[]
members=[]
while True:
    print("---Library menu---")
    print("1. Add book")
    print("2. Update book")
    print("3. Remove book")
    print("4. Display books")
    print("5. Count books")
    print("6. Add member")
    print("7. Update member")
    print("8. Remove member")
    print("9. Display members")
    print("10. Search book")
    print("11. Borrow book")
    print("12. Return book")
    print("13. Exit")

    choice=input("Enter your choice:").strip()

    if(choice=="1"):
        title=input("enter book name:").strip().title()
        author=input("enter author name:").strip().title()
        books.append({"title":title,"author":author,"available":True})
        print("Book added!")
    elif(choice=="2"):
        title=input("enter the book name to update:").strip().title()
        for book in books:
            if book["title"].lower()==title.lower():
                new_author=input("enter a new author name:").strip().title()
                book["author"]=new_author
                print("Book updated")
                break    
        else:
            print("book not found")   
    elif(choice=="3"):
        title=input("Enter book name to remove:").strip().title()
        for book in books:
            if(book["title"].lower()==title.lower()):
                books.remove(book)
                print("Book removed")
                break
        else:
            print("book not found")
    elif(choice=="4"):
        if not books:
            print("no books stored!")
        for book in books:
            status="Available"if book["available"] else "Borrowed"
            print(f"\n {book['title']}|{book['author']}|Status:{status}")
    elif(choice=="5"):
        print(f"\n Total books:{len(books)}")
    elif (choice == "6"):
        name = input("Enter member name: ").strip().title()
        members.append(name)
        print("Member added!")
    elif (choice == "7"):
        name = input("Enter member name to update: ").strip().title()
        for i in range(len(members)):
            if members[i].lower() == name.lower():
                new_name = input("Enter new member name: ").strip().title()
                members[i] = new_name
                print("Member updated!")
                break
        else:
            print("Member not found!")
    elif (choice == "8"):
        name = input("Enter member name to remove: ").strip().title()
        for member in members:
            if member.lower() == name.lower():
                members.remove(member)
                print("Member removed!")
                break
        else:
            print("Member not found!")
    elif (choice == "9"):
        if not members:
            print("No members stored!")
        for member in members:
            print(f"👤 {member}")
    elif (choice == "10"):
        search=input("Enter a book title and author to search: ").strip().lower()
        found=False

        for book in books:
            title=book["title"].lower()
            author=book["author"].lower()

            if title.find(search) != -1 or author.find(search) != -1:
                status="Available" if book["available"] else "Borrowed"
                print(f"\n {book['title']} | {book['author']} | Status:{status}")
                found=True
        if not found:
            print("No matching book found!")

    elif choice == "11":   
        title = input("Enter book name to borrow: ").strip().title()
        for book in books:
            if book["title"].lower() == title.lower():
                if book["available"]:
                    book["available"] = False
                    print("Book borrowed successfully!")
                else:
                    print("Book already borrowed!")
                break
        else:
            print("Book not found!")


    elif choice == "12":   
        title = input("Enter book name to return: ").strip().title()
        for book in books:
            if book["title"].lower() == title.lower():
                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully!")
                else:
                    print("This book was not borrowed!")
                break
        else:
            print("Book not found!")
    elif choice == "13":
        print("Exiting... All the best!")
        break

    else:
        print("Invalid option! Try again.")
    
