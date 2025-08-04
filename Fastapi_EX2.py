from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    Grade: int

students = [
    Student(id=1, name="Kariem khaled", Grade=5),
    Student(id=2, name="Ahmed ghonime", Grade=3)
]

@app.get("/Students/")
def read_students():
    return students

@app.post("/Students/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student

@app.put("/Students/{student_id}")
def update_student(student_id: int, new_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = new_student
            return new_student
    return {"error": "Student not found"}

@app.delete("/Students/{student_id}")
def Delete_students(student_id:int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {'Message' : 'Student had deleted from Data Base'}
    return {'Error' : 'Student id not found'}
