from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return db.query(models.Teacher).where(models.Teacher.id == teacher_id).one()


@app.get("/teachers/")
def get_all_teachers(db: Session = Depends(get_db)):
    return db.query(models.Teacher).all()


@app.get("/grades")
def get_student_grades(student_id: int | None = None, teacher_id: int | None = None, db: Session = Depends(get_db)):
    return db.query(models.Grade).where(models.Grade.student_id == student_id).all()


@app.post("/grades/")
def add_grade(grade: schemas.GradeCreate, db: Session = Depends(get_db)):
    new_grade = models.Grade(**grade.model_dump())
    db.add(new_grade)
    db.commit()
    db.refresh(new_grade)
    return new_grade


@app.post("/students/")
def add_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
