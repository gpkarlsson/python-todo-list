#TODOLIST
    # Users can add, view, complete and remove tasks
    # program will loop
    
#FEATURES
    # List Management
    # Looping - while loop
    # Conditionals - if elif else
    # Input Validation

#STEPS
    # Initialize empty list
    
#ENHANCEMENTS
    # Remove item from list
    #

  # Get User Input
    # Handle Each Option
    # Loop Until Exit
TO_DO_LIST = []
MENU_OPTIONS = ["1. View Tasks", "2. Add New Task", "3. Complete Task", "4. Exit"]
    
    # Display Menu
def displayMenu():
    print(MENU_OPTIONS)

def addTask():
    #add task logic here
    newTask = input("Please add a task: ")
    TO_DO_LIST.append(newTask)
    print("Task Added")
    print(TO_DO_LIST)
    main()
    
def viewList():
    # display all tasks
    # i = 0
    # while i < len(TO_DO_LIST):
    #     print(TO_DO_LIST[i])
    #     i = i + 1
    #     break
    # return
    print(MENU_OPTIONS)
    for newMenu in MENU_OPTIONS:
        print(newMenu, end=',')
    main()

def completeTask():
    #complete individual task
    removeTask = input("Please select which task to complete: ")
    TO_DO_LIST.remove(removeTask)
    main()

def exit():
     print("later nerd")
     return


def main():
        displayMenu() 
        userInput = int(input("Please Select Task: "))
        if userInput < 0:
            print("Please enter a number between 1 and 4")
        elif userInput > 4:
            print("Please enter a number between 1 and 4")
            if userInput == 1:
                viewList()
            elif userInput == 2:
                addTask()
            elif userInput == 3:
                completeTask()
        

main()