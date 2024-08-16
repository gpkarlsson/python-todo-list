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
    # print(MENU_OPTIONS)
    newMenu =('\n'.join(str(a)for a in MENU_OPTIONS))
    print(newMenu)


def addTask():
    #add task logic here
    newTask = input("Please add a task: ")
    TO_DO_LIST.append(newTask)
    print("Task Added")
    print(TO_DO_LIST)
    main()


def viewList():
    print('penis')
    print(TO_DO_LIST)
    main()


def completeTask():
    #complete individual task
    removeTask = input("Please select which task to complete: ")
    TO_DO_LIST.remove(removeTask)
    main()


def exit():
     print("OHHHHH MY GOD MY WIENER IS SOOOOO SMALL BROOOOOO")
     return


def main():
        # print("\nPlease select an option by entering the corresponding number. \n") 
        displayMenu()
        while True:
            userInput = int(input("\nPlease select an option by entering a number between 1 and 4:"))
            if userInput < 0:
                print("Please enter a number between 1 and 4")
            elif userInput > 4:
                print("Please enter a number between 1 and 4")
            else:
                if userInput == 1:
                    print('view')
                    viewList()
                elif userInput == 2:
                    print('add')
                    addTask()
                elif userInput == 3:
                    print('complete')
                    completeTask()
                else:
                    if userInput == 4:
                        print('exit')
                        exit()
                        break
main()