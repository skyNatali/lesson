import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
from models import Student, Course, Enrollment, Base
from config import engine, SessionLocal

# Фикстура для создания таблиц перед тестами
@pytest.fixture(scope="session", autouse=True)
def create_tables():
    """Создание таблиц перед запуском тестов"""
    Base.metadata.create_all(bind=engine)
    yield
    # После всех тестов можно удалить таблицы (опционально)
    # Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session():
    """Фикстура для работы с сессией БД"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture
def cleanup_data(db_session):
    """Фикстура для очистки данных после теста"""
    yield
    # Очищаем данные после каждого теста
    db_session.query(Enrollment).delete()
    db_session.query(Course).delete()
    db_session.query(Student).delete()
    db_session.commit()

class TestDatabaseOperations:
    """Тесты для операций с базой данных"""
    
    def test_add_student(self, db_session, cleanup_data):
        """Тест добавления новой сущности (студента)"""
        # 1. Создаем нового студента
        new_student = Student(
            name="Иван Иванов",
            email="ivan@example.com",
            age=22
        )
        
        # 2. Добавляем в БД
        db_session.add(new_student)
        db_session.commit()
        db_session.refresh(new_student)
        
        # 3. Проверяем, что студент добавлен
        assert new_student.id is not None
        assert new_student.name == "Иван Иванов"
        assert new_student.email == "ivan@example.com"
        assert new_student.age == 22
        assert new_student.is_active == True
        assert new_student.is_deleted == False
        
        # 4. Проверяем, что студент существует в БД
        student_from_db = db_session.query(Student).filter_by(id=new_student.id).first()
        assert student_from_db is not None
        assert student_from_db.name == "Иван Иванов"
        
        print(f"✅ Студент добавлен: ID={new_student.id}, Имя={new_student.name}")
    
    def test_update_student(self, db_session, cleanup_data):
        """Тест изменения существующей сущности (студента)"""
        # 1. Сначала создаем студента для теста
        student = Student(
            name="Мария Петрова",
            email="maria@example.com",
            age=21
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        student_id = student.id
        print(f"Создан студент для обновления: ID={student_id}")
        
        # 2. Обновляем данные студента
        db_session.query(Student).filter_by(id=student_id).update({
            "name": "Мария Сидорова",
            "age": 22,
            "email": "maria.sidorova@example.com"
        })
        db_session.commit()
        
        # 3. Получаем обновленного студента
        updated_student = db_session.query(Student).filter_by(id=student_id).first()
        
        # 4. Проверяем изменения
        assert updated_student is not None
        assert updated_student.name == "Мария Сидорова"
        assert updated_student.email == "maria.sidorova@example.com"
        assert updated_student.age == 22
        
        print(f"✅ Студент обновлен: ID={student_id}, Новое имя={updated_student.name}")
    
    def test_delete_student_soft_delete(self, db_session, cleanup_data):
        """Тест удаления сущности с использованием soft delete"""
        # 1. Создаем студента для теста
        student = Student(
            name="Алексей Смирнов",
            email="alex@example.com",
            age=23
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        student_id = student.id
        print(f"Создан студент для удаления: ID={student_id}")
        
        # 2. Выполняем soft delete (помечаем как удаленного)
        db_session.query(Student).filter_by(id=student_id).update({
            "is_deleted": True,
            "is_active": False
        })
        db_session.commit()
        
        # 3. Проверяем, что студент помечен как удаленный
        deleted_student = db_session.query(Student).filter_by(id=student_id).first()
        assert deleted_student is not None  # Запись все еще существует
        assert deleted_student.is_deleted == True
        assert deleted_student.is_active == False
        
        # 4. Проверяем, что в активных студентах его нет
        active_student = db_session.query(Student).filter_by(
            id=student_id, 
            is_deleted=False,
            is_active=True
        ).first()
        assert active_student is None
        
        print(f"✅ Soft delete выполнен: ID={student_id}, is_deleted={deleted_student.is_deleted}")
    
    def test_delete_student_hard_delete(self, db_session, cleanup_data):
        """Тест полного удаления сущности из БД"""
        # 1. Создаем студента для теста
        student = Student(
            name="Елена Кузнецова",
            email="elena@example.com",
            age=24
        )
        db_session.add(student)
        db_session.commit()
        db_session.refresh(student)
        
        student_id = student.id
        print(f"Создан студент для полного удаления: ID={student_id}")
        
        # 2. Получаем студента перед удалением
        student_before_delete = db_session.query(Student).filter_by(id=student_id).first()
        assert student_before_delete is not None
        
        # 3. Удаляем студента полностью
        db_session.query(Student).filter_by(id=student_id).delete()
        db_session.commit()
        
        # 4. Проверяем, что студента больше нет в БД
        student_after_delete = db_session.query(Student).filter_by(id=student_id).first()
        assert student_after_delete is None
        
        print(f"✅ Hard delete выполнен: ID={student_id} удален полностью")
    
    def test_add_course(self, db_session, cleanup_data):
        """Дополнительный тест: добавление курса"""
        # 1. Создаем курс
        new_course = Course(
            title="Python для начинающих",
            description="Изучение основ Python",
            duration_hours=40
        )
        
        # 2. Добавляем в БД
        db_session.add(new_course)
        db_session.commit()
        db_session.refresh(new_course)
        
        # 3. Проверяем
        assert new_course.id is not None
        assert new_course.title == "Python для начинающих"
        assert new_course.duration_hours == 40
        assert new_course.is_active == True
        
        print(f"✅ Курс добавлен: ID={new_course.id}, Название={new_course.title}")
    
    def test_enroll_student_to_course(self, db_session, cleanup_data):
        """Дополнительный тест: запись студента на курс"""
        # 1. Создаем студента и курс
        student = Student(
            name="Дмитрий Волков",
            email="dmitry@example.com",
            age=25
        )
        course = Course(
            title="SQLAlchemy Advanced",
            description="Продвинутое использование SQLAlchemy",
            duration_hours=30
        )
        
        db_session.add_all([student, course])
        db_session.commit()
        db_session.refresh(student)
        db_session.refresh(course)
        
        # 2. Записываем студента на курс
        enrollment = Enrollment(
            student_id=student.id,
            course_id=course.id
        )
        
        db_session.add(enrollment)
        db_session.commit()
        db_session.refresh(enrollment)
        
        # 3. Проверяем запись
        assert enrollment.id is not None
        assert enrollment.student_id == student.id
        assert enrollment.course_id == course.id
        assert enrollment.completed == False
        
        print(f"✅ Запись на курс: Студент ID={student.id} → Курс ID={course.id}")
    
    def test_unique_email_constraint(self, db_session, cleanup_data):
        """Тест проверки уникальности email (негативный сценарий)"""
        # 1. Создаем первого студента
        student1 = Student(
            name="Ольга Новикова",
            email="olga@example.com",
            age=22
        )
        db_session.add(student1)
        db_session.commit()
        
        # 2. Пытаемся создать второго студента с тем же email
        student2 = Student(
            name="Ольга Другая",
            email="olga@example.com",  # Тот же email!
            age=23
        )
        db_session.add(student2)
        
        # 3. Ожидаем ошибку уникальности
        with pytest.raises(IntegrityError):
            db_session.commit()
        
        db_session.rollback()  # Откатываем транзакцию
        
        print("✅ Проверка уникальности email: ошибка IntegrityError поймана")

if __name__ == "__main__":
    # Создаем таблицы перед запуском тестов
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы. Запустите тесты командой: pytest test_database.py -v")
