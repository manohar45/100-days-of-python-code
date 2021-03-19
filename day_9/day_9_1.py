student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}
for score in student_scores:
  scores=student_scores[score]
  if(scores>=91 and scores<=100):
    student_grades[score]="Outstanding"
  elif(scores>=81 and scores<=90):
    student_grades[score]="Exceeds Expectations"
  elif(scores>=71 and scores<=80):
    student_grades[score]="Acceptable"
  elif(scores<=70):
    student_grades[score]="Fail"

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)





