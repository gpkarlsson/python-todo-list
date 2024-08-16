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
#TODO: Prevent users from being able to enter blank task

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
        
        print(f'Please enter a number between 1 and {len(TO_DO_LIST)}.')
        removeTask = int(input("Please select which task to complete: "))

        try:
            if int(removeTask):
                completedTask = TO_DO_LIST.pop(removeTask - 1)
                print(f"Task Completed: {completedTask}\n")
                print(f"Number of remaining tasks: {len(TO_DO_LIST)}\n")
                    
            elif removeTask == '':
                print('Please enter a number\n')
            else:
                print("Please enter a number\n")
        except IndexError:
            if len(TO_DO_LIST) < 1:
                print(f'Please enter a number between 1 and {len(TO_DO_LIST)}')
            else:
                #TODO: Add option for user to return to main menu
                #TODO: Handle behavior when all tasks removed -> return to main menu
                # if removeTask == 99:
                #     displayMenu()
                continue
    

# Exit the program
def exitProgram():
     print("goodbye")

# Main function handles user input to select menu options and input validation
def main():
        # print("\nPlease select an option by entering the corresponding number. \n") 
        displayMenu()
        enumTasks()
        while True:
            try:    
                menuChoice = int(input("\nPlease select an option by entering a number between 1 and 4:"))
            except ValueError:
                print("\nPlease enter a valid number between 1 and 4")
                continue
            #TODO: Refactor, checking if menuChoice is between 1 and 4 is redundant and can make code harder to maintain
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
                    if len(TO_DO_LIST) == 0:
                        print('To Do list is empty')
                    else:
                        completeTask()
                else:
                    if menuChoice == 4:
                        exitProgram()
                        break
main()


# #code review notes
# Code Review: Identifying Potential Bad Habits

#     Code Duplication:
#         ! Observation: There is some duplication in how you handle menu choices and validation within the main() function. Specifically, the checks for valid input (menuChoice < 1 and menuChoice > 4) could be combined or handled more efficiently.
#         TODO: Suggestion: Look for ways to reduce repetition by combining conditions or creating helper functions. This will make your code cleaner and easier to maintain.

#     Error Handling:
#         ! Observation: You’ve implemented try-except blocks for handling potential errors in both the main() and completeTask() functions, which is good practice. However, the logic within these blocks, particularly in completeTask(), could be refined.
#         TODO: Suggestion: Consider whether all possible user errors (e.g., entering an invalid number) are handled gracefully. Think about ways to streamline the error handling to avoid nested conditions and to provide clearer feedback to the user.

#     Function Responsibilities:
#         ! Observation: The completeTask() function does several things: enumerates tasks, handles user input, manages errors, and updates the task list. While it works, this function might be taking on too many responsibilities.
#         #TODO Suggestion: Break down the completeTask() function into smaller, more focused functions. For instance, separate the task enumeration from the task removal logic. This will make your code more modular and easier to debug.

#     Input Validation:
#         ! Observation: You’ve added input validation in the addTask() and completeTask() functions, which is great. However, there’s still room to enhance this, especially regarding empty input or out-of-range numbers.
#         #TODO Suggestion: Ensure that all user inputs are validated before processing. For example, in addTask(), prevent the addition of empty tasks. In completeTask(), ensure that the selected task number is valid before attempting to remove it.

#     Naming Conventions:
#         ! Observation: The names of your functions and variables are generally clear and descriptive, but there’s a mix of styles (e.g., TO_DO_LIST vs. menuChoice).
#         #TODO Suggestion: Stick to a consistent naming convention throughout your code. For example, use snake_case for variables and function names (e.g., to_do_list, menu_choice). Reserve all-uppercase names for constants.

#     Commenting and TODOs:
#         ! Observation: Your comments and TODOs are clear and helpful, which is a good habit. However, some comments (e.g., “# Loop through tasks assigning a number each task”) could be refined or removed if they simply restate what the code is doing.
#         #TODO Suggestion: Focus on writing comments that explain why you’re doing something, rather than what you’re doing. This makes the comments more valuable, especially when revisiting the code later.

#     Redundant or Unnecessary Conditions:
#         ! Observation: In completeTask(), there’s a condition that checks elif removeTask == '' which might not be necessary if you handle empty input earlier.
#         #TODO Suggestion: Review your conditional logic to ensure that all branches are necessary and relevant. Removing unnecessary checks will simplify your code and make it easier to follow.

#     User Experience Considerations:
#         ! Observation: The user experience in completeTask() could be improved, especially regarding feedback when an invalid task number is entered or when all tasks are completed.
#         #TODO Suggestion: Consider how the program flows from one state to another. For example, after a task is completed, you might want to return to the main menu automatically, rather than continuing within the completeTask() function.

# Overall Assessment:

# You’re doing an excellent job of building out the functionality of your to-do list program and implementing key Python practices. The areas identified above are common opportunities for improvement as you refine your skills. By focusing on reducing redundancy, refining function responsibilities, and enhancing user input handling, you’ll be able to write cleaner, more efficient, and more maintainable code.

# Keep experimenting and refining your approach—these habits will serve you well as your projects become more complex.