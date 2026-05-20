l=[]
while (True):
    print("""
          1.Add element
          2.Remove element
          3.Display element
          4.Display first three elements
          5.Display last three elements
          6.print
          7.Exit""")
    ch=int(input("Enter your choice:"))
    if ch==1:
        e=input("Enter element to be added:")
        l.append(e)
    elif ch==2:
        if l.count==0:
            print("List is empty")
        else:
            e=input("Enter element to be removed:")
            l.remove(e)
    elif ch==3:
        e=input("Enter element to be searched:")
        if e in l:
            print("Element found at index",l.index(e))
        else:
            print("Element not found")
    elif ch==4:
        print("The first three elememts are:",l[:3])
    elif ch==5:
        print("The last three elements are:",l[-3:])
    elif ch==6:
        print("the elements in the list are:",l)
    elif ch==7:
        exit() 