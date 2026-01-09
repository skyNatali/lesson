from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from config import Base

class Student(Base):
    """Модель студента"""
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)  # Для soft delete
    
    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"

class Course(Base):
    """Модель курса"""
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    duration_hours = Column(Integer, default=40)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<Course(id={self.id}, title={self.title})>"

class Enrollment(Base):
    """Модель записи студента на курс"""
    __tablename__ = "enrollments"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, nullable=False)
    course_id = Column(Integer, nullable=False)
    enrolled_at = Column(DateTime(timezone=True), server_default=func.now())
    completed = Column(Boolean, default=False)
    
    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"
