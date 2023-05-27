


#----------------------------------------------------------------
#---------Function Packing, Unpacking Arguments *Arg-----
#-----------------------------------------------------------------



print(1,2,3,4) # 1 2 3 4

myList = [1,2,3,4]

print(myList) # [1, 2, 3, 4]
print(*myList) # 1 2 3 4

print("#" * 60) # ############################################################

def say_hello(*peoples) : # n1 , n2 , n3 , n4
    
    for name in peoples :
        print(f"Hello{name}")


say_hello("Salar" , "Raman" , "Gamel" , "Shergo" , "Lava") # # Hello Salar # Hello Raman # Hello Gamel # Hello Shergo # Hello Lava
say_hello("Salar" , "Raman" , "Gamel" ) # # Hello Salar # Hello Raman # Hello Gamel 

print("#" * 60) # ############################################################

# normal Way

def show_details(skill1 , skill2 , skill3 , skill4) :
    print(f"Hello Salar Your Skills is : ")
    print(f"{skill1}")
    print(f"{skill2}")
    print(f"{skill3}")
    print(f"{skill4}")

show_details("Html" , "Css" , "Js") # Hello Salar Your Skills is : Html , Css , Js
show_details("Html" , "Css" , "Js" , "python") # Hello Salar Your Skills is : Html , Css , Js , python

# packing and unpacking way

def show_details(name, *skills) :
    print(f"Hello {name} Your Skills is : ")
    for skill in skills :
        print(skill)

show_details("Html" , "Css" , "Js" , "Python") # Hello Salar Your Skills is : Html , Css , Js , python
show_details("Html" , "Css" , "Js" , "Python" , "Mashine Learning") # Hello Salar Your Skills is : Html , Css , Js , python , mashine Learning
show_details("Salar" , "Html" , "Css" , "Js" ,) # Hello Salar Your Skills is : Html , Css , Js 

