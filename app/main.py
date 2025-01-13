from fastapi import FastAPI

import crud
import models
import schemas
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int):
    return crud.get_teacher_by_id(teacher_id)


@app.get("/teachers/")
def get_all_teachers():
    return crud.get_all_teachers()


@app.get("/grades")
def get_student_grades_by_id(student_id: int | None = None):
    return crud.get_student_grades_by_id(student_id)


@app.post("/grades/")
def add_grade(grade: schemas.GradeCreate):
    new_grade = models.Grade(**grade.model_dump())
    crud.add_grade(new_grade)
    return new_grade


@app.post("/students/")
def add_student(student: schemas.StudentCreate):
    new_student = models.Student(**student.model_dump())
    crud.add_student(new_student)
    return new_student
