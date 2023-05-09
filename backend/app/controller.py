from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database import get_db
from fastapi import FastAPI, Depends, HTTPException
from datetime import datetime
from typing import List
from .database import SessionLocal, engine

from app.security import validate_token, reusable_oauth2

router = APIRouter()

# CREATE coefficients
@router.post("/coefficients/", response_model=schemas.Coefficients, status_code=status.HTTP_201_CREATED)
def create_coefficients(coefficients: schemas.CoefficientsCreate, db: Session = Depends(get_db)):
    db_coefficients = models.Coefficients(**coefficients.dict())
    db.add(db_coefficients)
    db.commit()
    db.refresh(db_coefficients)
    return {"status": "success", "coefficients": db_coefficients}

# READ coefficients
@router.get("/coefficients/", response_model=List[schemas.Coefficients])
def read_coefficients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    coefficients = db.query(models.Coefficients).offset(skip).limit(limit).all()
    return coefficients

# READ coefficients by ID
@router.get("/coefficients/{coefficients_id}", response_model=schemas.Coefficients)
def read_coefficient(coefficients_id: int, db: Session = Depends(get_db)):
    db_coefficients = db.query(models.Coefficients).filter(models.Coefficients.id == coefficients_id).first()
    if db_coefficients is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coefficients not found")
    return db_coefficients

# UPDATE coefficients by ID
@router.put("/coefficients/{coefficients_id}", response_model=schemas.Coefficients)
def update_coefficients(coefficients_id: int, coefficients: schemas.CoefficientsUpdate, db: Session = Depends(get_db)):
    db_coefficients = db.query(models.Coefficients).filter(models.Coefficients.id == coefficients_id).first()
    if db_coefficients is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coefficients not found")
    for field, value in coefficients:
        setattr(db_coefficients, field, value)
    db.commit()
    db.refresh(db_coefficients)
    return db_coefficients

# DELETE coefficients by ID
@router.delete("/coefficients/{coefficients_id}", response_model=schemas.Coefficients)
def delete_coefficients(coefficients_id: int, db: Session = Depends(get_db)):
    db_coefficients = db.query(models.Coefficients).filter(models.Coefficients.id == coefficients_id).first()
    if db_coefficients is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coefficients not found")
    db.delete(db_coefficients)
    db.commit()
    return db_coefficients

# CREATE teacher
@router.post("/teachers/", response_model=schemas.Teacher, status_code=status.HTTP_201_CREATED)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = models.Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return {"status": "success", "teacher": db_teacher}

# READ teachers
@router.get("/teachers/", response_model=List[schemas.Teacher])
def read_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teachers = db.query(models.Teacher).offset(skip).limit(limit).all()
    return teachers

# READ teacher by ID
@router.get("/teachers/{teacher_id}", response_model=schemas.Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    return db_teacher

# UPDATE teacher by ID
@router.put("/teachers/{teacher_id}", response_model=schemas.Teacher)
def update_teacher(teacher_id: int, teacher: schemas.TeacherUpdate, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    for field, value in teacher:
        setattr(db_teacher, field, value)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# DELETE teacher by ID
@router.delete("/teachers/{teacher_id}", response_model=schemas.Teacher)
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    if db_teacher is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found")
    db.delete(db_teacher)
    db.commit()
    return db_teacher

# CREATE class
@router.post("/class/", response_model=schemas.Class, status_code=status.HTTP_201_CREATED)
def create_class(class_: schemas.ClassCreate, db: Session = Depends(get_db)):
    db_class = models.Class(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return {"status": "success", "class": db_class}

# READ all classes
@router.get("/class/", response_model=List[schemas.Class])
def read_classes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classes = db.query(models.Class).offset(skip).limit(limit).all()
    return classes

# READ class by ID
@router.get("/class/{class_id}", response_model=schemas.Class)
def read_class(class_id: int, db: Session = Depends(get_db)):
    db_class = db.query(models.Class).filter(models.Class.id == class_id).first()
    if db_class is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")
    return db_class

# UPDATE class by ID
@router.put("/class/{class_id}", response_model=schemas.Class)
def update_class(class_id: int, class_: schemas.ClassUpdate, db: Session = Depends(get_db)):
    db_class = db.query(models.Class).filter(models.Class.id == class_id).first()
    if db_class is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")
    for field, value in class_.dict(exclude_unset=True).items():
        setattr(db_class, field, value)
    db.commit()
    db.refresh(db_class)
    return db_class

# DELETE class by ID
@router.delete("/class/{class_id}", response_model=schemas.Class)
def delete_class(class_id: int, db: Session = Depends(get_db)):
    db_class = db.query(models.Class).filter(models.Class.id == class_id).first()
    if db_class is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Class not found")
    db.delete(db_class)
    db.commit()
    return db_class

# CREATE salary
@router.post("/salary/", response_model=schemas.Salary, status_code=status.HTTP_201_CREATED)
def create_salary(salary: schemas.SalaryCreate, db: Session = Depends(get_db)):
    db_salary = models.Salary(update_day=datetime.now(), **salary.dict())
    db.add(db_salary)
    db.commit()
    db.refresh(db_salary)
    return {"status": "success", "salary": db_salary}

# READ salaries
@router.get("/salary/", response_model=List[schemas.Salary])
def read_salaries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    salaries = db.query(models.Salary).offset(skip).limit(limit).all()
    return salaries

# READ salary by ID
@router.get("/salary/{salary_id}", response_model=schemas.Salary)
def read_salary(salary_id: int, db: Session = Depends(get_db)):
    db_salary = db.query(models.Salary).filter(models.Salary.id == salary_id).first()
    if db_salary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Salary not found")
    return db_salary

# UPDATE salary by ID
@router.put("/salary/{salary_id}", response_model=schemas.Salary)
def update_salary(salary_id: int, salary: schemas.SalaryUpdate, db: Session = Depends(get_db)):
    db_salary = db.query(models.Salary).filter(models.Salary.id == salary_id).first()
    if db_salary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Salary not found")
    for field, value in salary:
        setattr(db_salary, field, value)
    db_salary.update_day = datetime.now()
    db.commit()
    db.refresh(db_salary)
    return db_salary

# DELETE salary by ID
@router.delete("/salary/{salary_id}", response_model=schemas.Salary)
def delete_salary(salary_id: int, db: Session = Depends(get_db)):
    db_salary = db.query(models.Salary).filter(models.Salary.id == salary_id).first()
    if db_salary is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Salary not found")
    db.delete(db_salary)
    db.commit()
    return db_salary


