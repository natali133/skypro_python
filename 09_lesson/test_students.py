import pytest
from sqlalchemy.orm import Session
from db import SessionLocal, Student


@pytest.fixture
def db_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def test_add_student(db_session: Session):
    # Добавление студента
    new_student = Student(first_name="Ann", last_name="Grig")
    db_session.add(new_student)

    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"Error during commit: {e}")
        print(f"Data causing error: {new_student.first_name}, {new_student.last_name}")
        assert False, f"Commit failed: {e}"

    # Проверка, что студент добавлен
    student = db_session.query(Student).filter_by(first_name="Ann", last_name="Grig").first()
    assert student is not None

    # Удаление тестового студента
    db_session.delete(student)
    db_session.commit()


def test_update_student(db_session: Session):
    # Добавление студента
    new_student = Student(first_name="Ann", last_name="Grig")
    db_session.add(new_student)
    db_session.commit()

    # Изменение студента
    student = db_session.query(Student).filter_by(first_name="Ann", last_name="Grig").first()
    student.first_name = "Ron"
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"Error during commit: {e}")
        print(f"Data causing error: {student.first_name}, {student.last_name}")
        assert False, f"Commit failed: {e}"

    # Проверка, что студент изменен
    updated_student = db_session.query(Student).filter_by(first_name="Ron", last_name="Doe").first()
    assert updated_student is not None

    # Удаление тестового студента
    db_session.delete(updated_student)
    db_session.commit()


def test_delete_student(db_session: Session):
    # Добавление студента
    new_student = Student(first_name="Natali", last_name="Smith")
    db_session.add(new_student)
    db_session.commit()

    # Удаление студента
    student = db_session.query(Student).filter_by(first_name="Natali", last_name="Smith").first()
    db_session.delete(student)
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"Error during commit: {e}")
        print(f"Data causing error: {student.first_name}, {student.last_name}")
        assert False, f"Commit failed: {e}"

    # Проверка, что студент удален
    deleted_student = db_session.query(Student).filter_by(first_name="Natali", last_name="Smith").first()
    assert deleted_student is None