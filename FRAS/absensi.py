import os  # accessing the os functions
import Recognize


# creating the title bar function

def title_bar():
    os.system('cls')  # for windows

    # title of the program

    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")


# creating the user main menu function

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "TEKAN TOMBOL Q UNTUK MENUTUP WEBCAM", 10 * "*")

    while True:
        try:
            choice = 1

            if choice == 1:
                RecognizeFaces()
                break
            elif choice == 2:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-2")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-2\n Try Again")
    exit


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def RecognizeFaces():
    Recognize.recognize_attendence()
    exit()


# ---------------main driver ------------------
mainMenu()
