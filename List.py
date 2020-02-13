#Creating a list of students
students =["Leroy", "Sospeter", "Collins", "Nyaroo",]
print(students)

#creating an empty list
#Indexing
print (students[1])
#displays the second students in the list
print (students[0])
#displays the first the student in the list
print (students[-4:-1])
#displays the fourth student starting form the back of the list upto to the second last student in the list
print (students[2])
#displays the third student in the list 

students[3] ="Anyona"
students[2]="Omboto"
students[1]= "Teddy"
print(students)

#loop through the list
for student in students:
   print(student)
#check if item exists 
if "Leroy" in students:
  print("Leroy is there")
#methods 
print(len(students))
students.append("Grace")
print(students)
students.insert(2,"Gladys")
print(students)
# pop () remove the specified index
students.pop(2)
print(students)
#clear() method empties the list:
students.clear()
print(students)
#copy() Make a copy of a list 
students = students.copy()
print(students)