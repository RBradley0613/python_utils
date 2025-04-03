import statistics
import os

_students_dict = {
    'Joe'       :[50, 60, 70],
    'Schmoe'    :[99, 97, 98],
    'Bob'       :[80, 82, 81]
}

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def PrintMenu():
    clear_screen()
    print("Main Menu")
    print("1)\tEnter New Grades")
    print("2)\tRemove Student")
    print("3)\tStudent Average Grades")
    print("4)\tExit")


if __name__ == "__main__":
    run = True
    while(run):
        PrintMenu()
        resp = input("Enter 1-4: ")

        match resp:
            case "1":
                name = input("\nEnter student name:")
            
                grade = input("Enter a new grade: ")
                if name in _students_dict:
                    _students_dict[name].append(int(grade))
                else:
                    _students_dict[name] = [int(grade)]

            case "2":
                print("todo: Remove Student")
                print(_students_dict)
                name = input("\nStudent name to remove: ")
                if name in _students_dict:
                    _students_dict.pop(name)
                else:
                    print("The name", name, "was not found.")
                    input("Press a key to continue.")

            case "3":
                clear_screen()
                print("Current grades:")
                for student in _students_dict:
                    gradeList = _students_dict[student]

                    #only get a mean if there is more than one value ... OR ELSE!
                    if len(gradeList) > 1:
                        mean = statistics.mean(_students_dict[student])
                    else:
                        mean = _students_dict[student]
                    print(student, "\t:\t", 
                          "AVG:",mean, "\t",
                          _students_dict[student])
                input("Press any key to continue.")

            case "4":
                print("\nExiting.  Have a nice day.")
                run = False
                continue
            case _:
                print("Please select a valid option (1-4)")
                input("Press any key to continue.")
