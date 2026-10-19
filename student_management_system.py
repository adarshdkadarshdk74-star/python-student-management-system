import json
students= []

def menu():
    print("*"*100)
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Exit")
def save_students():
   with open("student.json","w") as file:
      json.dump(students,file)
try:
     with open("student.json","r") as file:
       students= json.load(file)
     if not isinstance(students, list):
        print("enter valid student name.")
        students=[]
     else:
        for name in students:
           if not isinstance(name,str):
              print("student data is invalid.")
              students=[]
              break
              
          
except FileNotFoundError:
      print("No saved records found. Starting with an empty list.") 
except json.JSONDecodeError:
    print("Invalid JSON data. Starting with an empty list.")
    students = []
    
while(True):
  menu()
  try:
      choice=int(input("Enter your choice(1 to 6): "))


      if choice==1:
        print("Add Student selected!")
        st_name=input("Enter your Name: ").strip().lower()
        if not st_name: 
            print("Enter valid input.")
        elif st_name.isdigit():
                print("Name cannot contain only numbers.")
        else:
           if st_name not in students:  
              students.append(st_name)
              save_students()
              print("Student added successfully!")
           else:
              print("Student already exists!")


      elif choice==2:
         print("View Students selected!")
         if students:
           i=1
           for j in students:
              print(f"{i}.{j}")
              i+=1
         else:
           print("No students available!")


      elif choice==3:
         print("Search Student selected!")
         if  students:
            search_name=input("Enter Student name to Search: ").strip().lower()
            if not search_name:
                  print("Enter a valid name!")
            else: 
               for k in students:
                   if search_name == k.lower():
                     print("Student found!")
                     break
               else:
                      print("student not found")                 
         else:
           print("No students available!")

      elif choice == 4:
        print("Update Student Selected!")

        if students:
            search_name = input("Enter Student name to Search: ").strip().lower()

            if not search_name:
                print("Enter valid name!")

            elif search_name in students:
                new_name = input("Enter new name to update: ").strip().lower()

                if not new_name:
                    print("Enter valid name!")

                elif new_name.isdigit():
                    print("Name cannot contain only numbers.")

                elif new_name in students and new_name != search_name:
                    print("Student name already exists!")

                else:
                    position = students.index(search_name)
                    students[position] = new_name
                    save_students()
                    print("Student updated successfully!")

            else:
                print("Student not found!")

        else:
            print("No students available!")
     
      elif choice==5:
          print("Delete Student Selected!") 
          if students:
            search_name=input("Enter Student name to Search: ").strip().lower()
            if not search_name:
                print("Enter a valid name!")
            elif search_name in students:
              positon_2=students.index(search_name)
              students.pop(positon_2)
              save_students()
              print("Student deleted successfully!")
            else:
                print("Student not found!")
          else:
             print("No students available!")


      elif choice==6:
        print("Exit selected!")
        break
      else:
         print("Enter valid input!")

  except ValueError:
          print("input invalid")