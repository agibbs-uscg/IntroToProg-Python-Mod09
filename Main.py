# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# AGibbs, 13JUN20, Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as E  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as I

else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
emplst = []
filename = "C:\_PythonClass\Assignment09\Mod09Listings\EmployeeData.txt"

lstFileData = P.FileProcessor.read_data_from_file(filename)
for row in lstFileData:
    emplst.append(E(row[0], row[1], row[2].strip()))

# Show user a menu of options
while (True):
    I.EmployeeIO.print_menu_items()
    # Get user's menu option choice
    strChoice = I.EmployeeIO.input_menu_options()
    # Show user current data in the list of employee objects
    if strChoice.strip() == '1':
        I.EmployeeIO.print_current_list_items(emplst)
    # Let user add data to the list of employee objects
    elif strChoice == '2':
        emp_input = I.EmployeeIO.input_employee_data()
        emplst.append(emp_input) #adds new data to list
        print(emp_input)
    # let user save current data to file
    elif strChoice == '3':
        P.FileProcessor.save_data_to_file(filename, emplst)
        print("Your Data Was Saved.")
    # Let user exit program
    elif strChoice == '4':
        break

    else:print("Please enter a number between 1 and 4") #in case user does not enter 1-4

# Main Body of Script  ---------------------------------------------------- #