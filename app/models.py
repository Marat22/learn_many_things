from sqlalchemy import Column, DATE, BIGINT, VARCHAR
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import mapped_column

from database import Base


class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(BIGINT, primary_key=True, nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)
    patronymic = Column(VARCHAR(50))


class Student(Base):
    __tablename__ = "student"

    id = Column(BIGINT, primary_key=True, nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    last_name = Column(VARCHAR(50), nullable=False)
    patronymic = Column(VARCHAR(50))
    date_of_birth = Column(DATE, nullable=False)


class Course(Base):
    __tablename__ = "course"

    id = Column(BIGINT, primary_key=True, nullable=False)
    course_name = Column(VARCHAR(50), nullable=False)


class Grade(Base):
    __tablename__ = "grade"

    id = Column(BIGINT, primary_key=True, nullable=False)
    student_id = mapped_column(BIGINT, ForeignKey("student.id"))
    teacher_id = mapped_column(BIGINT, ForeignKey("teacher.id"), nullable=False)
    date = Column(DATE, nullable=False)
    mark = Column(Integer, nullable=False)
