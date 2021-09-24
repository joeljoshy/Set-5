import py1

print("Features")
print("1.Post \n2.Comment")
choice = input("Enter your choice : ")

if choice == '1':

    print("1.Get posts\n2.Get post based on the user\n3.Get post detail")
    p_choice = input("Enter your choice : ")
    if p_choice == '1':
        py1.get_posts()

    elif p_choice == '2':
        id = int(input("Enter id : "))
        print(py1.get_user(id))

    elif p_choice == '3':
        id = int(input("Enter id : "))
        print(py1.get_detail(id))

elif choice == '2':
    print("1.Get comments\n2.Get comments based on the post.")
    c_choice = input("Enter your choice : ")

    if c_choice == '1':
        py1.get_comments()

    elif c_choice == '2':
        id = int(input("Enter post id : "))
        py1.get_comment(id)