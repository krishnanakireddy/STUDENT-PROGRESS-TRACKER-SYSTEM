# mini project
print("-----------------------------------------")
print("     STUDENT PROGRESS TRACKER SYSTEM     ")
print("-----------------------------------------\n")

change = False

while not change:
    name = input("Enter Student Name: ")
    student_class = input("Enter Student Class: ").upper()
    roll_no = input("Enter Roll Number: ")
    loops = False

    while not loops:
        sub = int(input("\nEnter number of subjects: "))
        marks = []
        mark = 0
        total_marks = 0
        i = 0
        print("\n")
        
        while i < sub:
          mark = int(input(f"Enter marks for subject {i+1}:"))
          if mark < 0 or mark > 100:
            print("Invalid marks entered. Please enter marks between 0 and 100.")
          else:
            marks.append(int(mark))
            total_marks += int(mark)
            i = i + 1
    
        average = total_marks / sub
        percentage = (total_marks / (sub * 100)) * 100
        highest_mark = max(marks)
        lowest_mark = min(marks)

        if total_marks > 90:
          grade = "A"
        elif total_marks > 75:
          grade = "B"
        elif total_marks > 50:
          grade = "C"
        elif total_marks > 35:
          grade = "D"
        else:
          grade = "Fail"

        if grade == "A":
          remarks = "Excellent"
        elif grade == "B":
          remarks = "Very Good"
        elif grade == "C":
          remarks = "Good"
        elif grade == "D":
          remarks = "Needs Improvement"

        if mark < 35:
         result = "Fail"
         remarks = "Needs Improvement"
         grade = "Fail"
        else:
         result = "Pass"
        
        while True:
          print("\n-----------------------------------------")
          print("     STUDENT PROGRESS TRACKER SYSTEM     ")
          print("-----------------------------------------\n")

          print(f"Student Name      : {name}")
          print(f"Student Class     : {student_class}")
          print(f"Roll Number       : {roll_no}")
          print(f"Total Marks       : {total_marks}")
          print(f"Average Marks     : {average}")
          print(f"Percentage        : {percentage}%")
          print(f"Highest Mark      : {highest_mark}")
          print(f"Lowest Mark       : {lowest_mark}")
          print(f"Grade             : {grade}")
          print(f"Remarks           : {remarks}")
          print(f"Result            : {result}")
          print("\n")

          # Menu System
          print("Menu:")
          print("What do you want to do next?")
          print("1. Enter marks again")
          print("2. View report again")
          print("3. Enter the new student details")
          print("4. Save report to a text file and exit")
          print("5. Exit\n")

          option = input("Enter your choice: ")
          if option == '1':
              break
          elif option == '2':
              continue
          elif option == '3':
              loops = True
              break
          elif option == '4':
              filename = f"{name.replace(' ')}.txt"
              with open(filename, 'w') as file:
                  file.write("-----------------------------------------\n")
                  file.write("     STUDENT PROGRESS TRACKER SYSTEM     \n")
                  file.write("-----------------------------------------\n\n")
                  file.write(f"Student Name      : {name}\n")
                  file.write(f"Student Class     : {student_class}\n")
                  file.write(f"Roll Number       : {roll_no}\n")
                  file.write(f"Total Marks       : {total_marks}\n")
                  file.write(f"Average Marks     : {average}\n")
                  file.write(f"Percentage        : {percentage}%\n")
                  file.write(f"Highest Mark      : {highest_mark}\n")
                  file.write(f"Lowest Mark       : {lowest_mark}\n")
                  file.write(f"Grade             : {grade}\n")
                  file.write(f"Remarks           : {remarks}\n")
                  file.write(f"Result            : {result}\n")
              print(f"Report saved to {filename}")
              change = True
              loops = True
              break
          elif option == '5':
              change = True
              loops = True
              break
          else:
              print("Invalid option. Please try again.\n") 
          print("\n")