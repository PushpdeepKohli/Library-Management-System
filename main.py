BorrowerList = ['Alex']
BookBorrowList = ['Guliver travels']
available_books = ['Malgudi Days','Let us c']

facultyName = ['Alex','Smith','Aryan','Sahil']
facultyId = [2544,2545,2546,2547]
facultyPass = [123,124,125,126]

studentName = ['Alex','Smith','Aryan','Sahil']
studentId = [2600,2601,2602,2603]
studentPass= [123,123,123,123]


class LibraryFaculty:
    def __init__(self,name):
        self.name = name
        print(f'''Welcome {self.name} you can now access following actions ''')
        print("1. Check the borrower's list ")
        print("2. Check the books borrowed ")
        print("3. Add a borrower ")
        print("4. Show available books ")
        print("5. Return of book")
        print("6. Show Borrower's request ")
        print("7. Raise an issue to administrator")
        print("8. Add a student ")
        print("9. See student queries")

class Student:
    def __init__(self,name):
        self.name = name
        print(f'''Welcome {self.name} you can now access following actions ''')
        print("1. Check availability of a book ")
        print("2. Request to borrow a book")
        print("3. Raise an issue to faculty")

class CustomError(Exception):
    pass

class passError(CustomError):
    pass

class idError(CustomError):
    pass

class invalidValue(CustomError):
    pass

class FacultyNotRegistered(CustomError):
    pass

class WrongPassword(CustomError):
    pass

class StudentNotRegistered(CustomError):
    pass

class alreadyExist(CustomError):
    pass

def checkAvailability(n):
    for item in available_books:
        if(item.lower() == n.lower()):
            return True
    else:
        return False

def checkId(id,list):
    for item in list:
        if(id== item):
            # idIndex = facultyId.index(item)
            return list.index(item)+1
    else:
        return False

def checkPass(number,list):
    for item in list:
        if(number== item):
            return list.index(item)+1
    else:
        return False



if __name__ == "__main__" :

    while True:
        
        print("-------Welcome to Library-------")
        print("Type 1 to login as library faculty")
        print("Type 2 to login as student")
        login_choice = int(input("Choice: "))
        try:
                if (login_choice==1):
                    id = int(input("Enter your Id: "))
                    if(checkId(id,facultyId)):
                        
                        password = int(input("Enter your password: "))
                        if(checkPass(password,facultyPass)):
                            if(checkId(id,facultyId)==checkPass(password,facultyPass)):
                                name = facultyName[facultyId.index(id)]
                                while (True):

                                    faculty = LibraryFaculty(name)
                                    faculty_choice = int(input("Choose : "))
                                    if(faculty_choice == 1):
                                        print(BorrowerList)
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break

                                    elif (faculty_choice == 2):
                                        print(BookBorrowList)
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break
                                    elif (faculty_choice == 3):
                                        
                                        j = input(f"enter book name : ")
                                        if(checkAvailability(j)):
                                            print("Available")
                                            f = input("enter name of student: ")

                                            BorrowerList.append(f)
                                            available_books.remove(j)
                                            BookBorrowList.append(j)
                                            print("Book borrowed successfully")
                                            quit = input("PRESS q to logout else press enter for another selection : ")
                                            if(quit.lower()=='q'):
                                                break
                                            
                                        else:
                                            print("Not Available")
                                        
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break

                                    elif (faculty_choice == 4):
                                        print(available_books)
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break

                                    elif (faculty_choice == 5):
                                        f = input("enter name of student as per records: ")
                                        g= input("enter id of student as per records: ")
                                        j = input("Enter book returned: ")
                                        BorrowerList.remove(f)
                                        BookBorrowList.remove(j)
                                        available_books.append(j)
                                        with open ("book-borrow-req-admin","a") as a:
                                            a.write(f"Student id- {g} student name- {f} student book {j}")
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break
                                    
                                    elif (faculty_choice == 6):
                                        with open("book-borrow-request.txt","r") as f:
                                            g= f.read()
                                        print(g)
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break

                                    elif(faculty_choice==7):
                                        issue = input("Enter your issue: ")
                                        with open ("faculty-doubt.txt","a") as f:
                                            f.write(f"Issue- {issue} \nName of faculty- {name} \nFaculty ID- {id}")
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break

                                    elif(faculty_choice==8):
                                        add_name= input("Enter name: ")
                                        add_id = int(input("Enter user id alloted (numeric only): "))
                                        if(add_id in studentId):
                                            raise alreadyExist
                                        else:                                                                                                                       
                                            add_pass= int(input("Enter password (numeric only):"))
                                            
                                            print("Successfully sent to Admin will be activated within 24 hours !!!")
                                            with open("new-student-id.txt","a") as f:
                                                f.write(f"Student Name - {add_name} StudentID - {add_id} StudentPass - {add_pass} \n")
                                            quit = input("PRESS q to logout else press enter for another selection : ")
                                            if(quit.lower()=='q'):
                                                break


                                    elif(faculty_choice==8):
                                        with open("student-doubt.txt","r") as f:
                                            print(f.read) 
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break  

                                        
                                    else:
                                        raise invalidValue            
                                            
                               
                        
                            else:
                                raise WrongPassword
                        else:
                            raise WrongPassword
                    else:
                        raise FacultyNotRegistered
                    
                    
                elif (login_choice==2):
                    id = int(input("Enter your Id: "))
                    if(checkId(id,studentId)):
                        password = int(input("Enter your password: "))
                        if(checkPass(password,studentPass)):
                            if(checkId(id,studentId)==checkPass(password,studentPass)):
                                name = studentName[studentId.index(id)]
                                while True:
                                    student1 = Student(name)
                                    student_choice= int(input("Chose: "))
                                    if(student_choice==1):
                                        book = input("Enter name of book: ")
                                        if(checkAvailability(book)):
                                            print("Available")
                                        else:
                                            print("Not Available")
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break
                                    elif(student_choice==2):
                                        book_re = input("enter book name : ")
                                        
                                        if(checkAvailability(book_re)):
                                        
                                            with open("book-borrow-request.txt","a") as f:
                                                f.write(f"Book name- {book_re}, Student name- {name}, Student ID- {id}\n")
                                            print("Request sent to faculty Successfully!")
                                                           
                                        else:
                                            print("Not Available")
                                       
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break
                                           
                                    elif(student_choice==3):
                                        issue = input("Enter your issue: ")
                                        with open ("student-doubt.txt","a") as f:
                                            f.write(f"Issue- {issue} \nName of Student- {name} \nStudent ID- {id}")
                                        quit = input("PRESS q to logout else press enter for another selection : ")
                                        if(quit.lower()=='q'):
                                            break
                                       
                            else:
                                raise WrongPassword
                        else:
                            raise WrongPassword
                    else:
                        raise StudentNotRegistered

                        
                else:
                    raise invalidValue


        except invalidValue:
            print("Invalid Choice!!!")
        except FacultyNotRegistered:
            print("Faculty not registered with our system try contacting administrator!!!")
        except WrongPassword:
            print("Invalid Password!!!")
        except StudentNotRegistered:
            print("Student not registered with our system try contacting faculty!!!")
        except alreadyExist:
            print("user id exists")
        except Exception as e :
            print("Numeric Password and UserID only")
        except alreadyExist:
            print("user id exists")

        quit = input("PRESS q to end application else press enter for another login: ")
        if(quit.lower()=='q'):
            break
