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


# Loop through tasks assigning a number each task 
def enumTasks():
    for index, newTask in enumerate(TO_DO_LIST):
        print(f"{index + 1}. {newTask}")


# Display Menu
def displayMenu():
    print(('\n'.join(str(a)for a in MENU_OPTIONS)))


# Add a new task
def addTask():
    newTask = input("Please add a task: ")
    TO_DO_LIST.append(newTask)
    print(f"\nTask Added:\n{newTask}")


# View current to do list
def viewList():
    if len(TO_DO_LIST) == 0:
        print("List is empty")
    else:
        # print("\n".join(str(b)for b in TO_DO_LIST))
        enumTasks()


# Complete a task (remove from list)
def completeTask():
    enumTasks()
    while True:
        removeTask = int(input("Please select which task to complete: "))
        if int(removeTask):
            TO_DO_LIST.pop(removeTask - 1)
            print(f"Task Completed: {removeTask}")
            displayMenu()
        else:
            print("Please enter a number\n")
        break
    


# Exit the program
def exitProgram():
     print("goodbye")

# Main function handles input and input validation
#TODO: handle type checking, currently entering non number breaks program
def main():
        # print("\nPlease select an option by entering the corresponding number. \n") 
        displayMenu()
        while True:
            menuChoice = int(input("\nPlease select an option by entering a number between 1 and 4:"))
            if menuChoice < 1:
                print("Please enter a number between 1 and 4")
            elif menuChoice > 4:
                print("Please enter a number between 1 and 4")
            else:
                if menuChoice == 1:
                    viewList()
                elif menuChoice == 2:
                    addTask()
                elif menuChoice == 3:
                    completeTask()
                else:
                    if menuChoice == 4:
                        exitProgram()
                        break
main()