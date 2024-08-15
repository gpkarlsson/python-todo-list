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
TO_DO_LIST = []
MENU_OPTIONS = ["View Tasks", "Add New Task", "Complete Task", "Exit"]
    # Display Menu
def displayMenu():
    
    # Get User Input
    # Handle Each Option
    # Loop Until Exit
    return
def addTask():
    #add task logic here
    newTask = input("Please add a task: ")
    TO_DO_LIST.append(newTask)
    return

def viewList():
    #display all tasks
    i = 0
    while i < len(TO_DO_LIST):
        print (TO_DO_LIST[i])
        i = i + 1
    return
def completeTask():
    #complete individual task
    removeTask = input("Please select which task to complete: ")
    TO_DO_LIST.remove(removeTask)

def main():
        userinput = input("Please Select Task: ").lower()
        if userinput == "view":
            viewList()
        elif userinput == "add":
            return addTask()
        # elif:
        #     userinput == "complete" 
        #     completeTask()
        
main()