import os

class Stack: #create all the required methods
    def __init__(self, maxitems):
        self.items = []
        self.maxitems = maxitems

        
    def push(self, item):
        if not self.full():
            self.items.append(item)
            print("The updated stacks are the following: ")
            for x in self.items:
                print("|",x,"|",end=' ')
          
        else:
            print("Stack is full")
            for x in self.items:
               print("|",x,"|",end=' ')
        
    def pop(self):
        if not self.empty():
            item = self.items.pop()
            print("The updated stacks are the following: ")
            for x in self.items:
                print("|",x,"|",end=' ')
        else:
            print("Stack is empty")

    def empty (self):
        return len(self.items) == 0
    
    def full(self):
        return len(self.items) == self.maxitems


def menu():
    stack = Stack(maxitems=5)

    while True:
        print("\n\nM_E_N_U")
        print("[A] Push item")
        print("[B] Pop item")
        print("[C] Quit")

        choice = input("Enter your choice: ")
    
        if choice == "A":
          item = input("Enter item to push: ") 
          os.system("cls")
          stack.push(item)

        elif (choice == "B"):
           os.system("cls")
           stack.pop()
        
        elif(choice == "C"):
            os.system("cls")
            print("EXIT SUCCESFUL")
            break
        
        else:
            os.system("cls")
            print("Invalid input! please try again: ")

menu()
