from sqlalchemy import Column, DATE, Integer, String, BIGINT, VARCHAR
from database import Base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column, Session
from sqlalchemy import create_engine, Integer, String, ForeignKey

# print(Base.classes.keys()) #this will print all the automaped tables

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

# Teacher = Base.classes.teacher
# Student = Base.classes.student
# Grade = Base.classes.grade
# Course = Base.classes.course

# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String, index=True)