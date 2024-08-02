"""
Este módulo define los modelos de base de datos utilizando SQLAlchemy ORM.
Configura el modelo Task y inicializa la conexión a la base de datos.
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Task(Base):
    """
    Representa una tarea en la base de datos.

    Atributos:
        id (int): La clave primaria de la tarea.
        title (str): El título de la tarea.
        category (str): La categoría de la tarea.
        description (str): Una descripción de la tarea.
        responsible (str): La persona responsable de la tarea.
        priority (str): El nivel de prioridad de la tarea.
        estimated_time (int): El tiempo estimado para completar la tarea en horas.
        due_date (datetime): La fecha de vencimiento de la tarea.
        notes (str): Notas adicionales sobre la tarea.
        creation_date (datetime): La fecha y hora cuando se creó la tarea.
        completed (bool): Si la tarea está completada o no.
    """

    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    category = Column(String)
    description = Column(String)
    responsible = Column(String)
    priority = Column(String)
    estimated_time = Column(Integer)
    due_date = Column(DateTime)
    notes = Column(String)
    creation_date = Column(DateTime, default=datetime.utcnow)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', completed={self.completed})>"


# Configuración de la base de datos
engine = create_engine('sqlite:///tasks.db')
Base.metadata.create_all(engine)  # Crea las tablas
# Crea una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)  # Crea una fábrica de sesiones
