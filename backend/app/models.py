from .database import Base
from sqlalchemy import Date, Column, String, Boolean, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True, index=True)
    subject = Column(String, nullable=False)
    num_students = Column(Integer, nullable=False)
    num_lessons = Column(Integer, nullable=True)
    classroom = Column(Boolean, nullable=False, default=True)
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))
    
    teacher = relationship('Teacher', back_populates='owner')

class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    address = Column(String, nullable=False)
    degree = Column(String, ForeignKey('coefficients.degree'))
    
    owner = relationship('Class', back_populates='teacher')
    wage = relationship('Coefficients', back_populates='coefficients')
    
class Coefficients(Base):
    __tablename__ = 'coefficients'
    degree = Column(String, primary_key=True, unique=True)
    update_day = Column(DateTime, primary_key=True)
    coefficients_salary = Column(Integer, nullable=False)
    
    coefficients = relationship('Teacher', back_populates='wage')
    
class Salary(Base):
    __tablename__ = 'salary'
    update_day = Column(DateTime, primary_key=True)
    salary = Column(Float, nullable=False)