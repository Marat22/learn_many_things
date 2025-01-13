from typing import Type

import models
from app.models import Teacher, Grade
from database import get_db

db = next(get_db())


def get_teacher_by_id(teacher_id: int) -> Type[Teacher]:
    return db.query(models.Teacher).where(models.Teacher.id == teacher_id).one()


def get_all_teachers() -> list[Type[Teacher]]:
    return db.query(models.Teacher).all()


def get_student_grades_by_id(student_id: int) -> list[Type[Grade]]:
    return db.query(models.Grade).where(models.Grade.student_id == student_id).all()


def add_grade(grade: Grade) -> None:
    db.add(grade)
    db.commit()
    db.refresh(grade)


def add_student(student: models.Student) -> None:
    db.add(student)
    db.commit()
    db.refresh(student)
