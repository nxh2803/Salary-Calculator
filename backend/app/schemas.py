from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from typing import Union

class CoefficientsBase(BaseModel):
    degree: str
    update_day: Optional[datetime] = datetime.now()
    coefficients_salary: int

class CoefficientsCreate(CoefficientsBase):
    pass

class CoefficientsUpdate(BaseModel):
    degree: Optional[str]
    update_day: Optional[datetime]
    coefficients_salary: Optional[int]
    
class Coefficients(CoefficientsBase):
    class Config:
        orm_mode = True

class TeacherBase(BaseModel):
    full_name: str
    date_of_birth: datetime
    phone: str
    email: str
    address: str
    degree: Optional[str] = None

class TeacherCreate(TeacherBase):
    pass

class TeacherUpdate(BaseModel):
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class Teacher(TeacherBase):
    teacher_id: int

    class Config:
        orm_mode = True

class ClassBase(BaseModel):
    subject: str
    num_students: int
    num_lessons: Optional[int] = None
    classroom: Optional[bool] = True
    teacher_id: int

class ClassCreate(ClassBase):
    pass

class ClassUpdate(BaseModel):
    num_students: Optional[int]
    num_lessons: Optional[int]
    classroom: Optional[bool]

class Class(ClassBase):
    class_id: int
    teacher: Optional[Teacher] = None

    class Config:
        orm_mode = True

class SalaryBase(BaseModel):
    salary: float

class SalaryCreate(SalaryBase):
    pass

class SalaryUpdate(BaseModel):
    salary: float
    update_day: datetime

class Salary(SalaryBase):
    update_day: datetime

    class Config:
        orm_mode = True

