from pydantic import BaseModel, conint, Field, validator, field_validator
from datetime import date
from typing import Annotated
from .database import get_db
from . import models


class TeacherCreate(BaseModel):
    name: str
    last_name: str
    patronymic: str | None = None


class StudentCreate(BaseModel):
    name: str
    last_name: str
    patronymic: str | None = None
    date_of_birth: date


class GradeCreate(BaseModel):
    student_id: int
    teacher_id: int
    date: date
    mark: Annotated[int, Field(ge=2, le=5)]

    @field_validator("student_id")
    def validate_student_id(cls, value):
        db = next(get_db())  # Получаем сессию для проверки
        if db.query(models.Student.id).filter(models.Student.id == value).one_or_none() is None:
            raise ValueError(f"`student_id` {value} не найден в таблице `student`.")
        return value

    @field_validator("teacher_id")
    def validate_teacher_id(cls, value):
        db = next(get_db()) # Получаем сессию для проверки
        if db.query(models.Teacher.id).filter(models.Teacher.id == value).one_or_none() is None:
            raise ValueError(f"`teacher_id` {value} не найден в таблице `teacher`.")
        return value
