def hello():
    print("Hello, user!")
    
    #a function named pack() that takes accepts three arguments,  and returna a single list with the
def pack(a, b, c):
    return [a, b, c]

#a function called eat_lunch(.) that takes a single argument, a list of strings, and returns a single string

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("my lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat  { my_list[0]}")
            else:
                print(f"Then I eat {my_list[i]}")
                
hello()
print(pack("a", "b", "c"))
print(pack(1,2,3)) 
eat_lunch([])
eat_lunch(["noodles"])
eat_lunch(["noodles", "rice", "chicken"])
               