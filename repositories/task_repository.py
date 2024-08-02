"""
Este módulo contiene la clase TaskRepository que maneja
las operaciones de base de datos para las tareas utilizando SQLAlchemy.
"""

from sqlalchemy.orm import Session
from database.models import Task as TaskModel
from datetime import datetime


class TaskRepository:
    """
    Maneja las operaciones de base de datos para las tareas.

    Esta clase proporciona métodos para añadir, eliminar, recuperar y actualizar tareas
    en la base de datos utilizando SQLAlchemy ORM.
    """

    def __init__(self, session: Session):
        """
        Inicializa el TaskRepository con una sesión de base de datos.

        Args:
            session (Session): Un objeto de sesión de SQLAlchemy.
        """
        self.session = session

    def add_task(self, task):
        """
        Añade una nueva tarea a la base de datos.

        Args:
            task: Un objeto Task que contiene los detalles de la tarea.
        """
        # Convierte el objeto Task a un TaskModel (modelo de SQLAlchemy)
        db_task = TaskModel(
            title=task.title,
            category=task.category,
            description=task.description,
            responsible=task.responsible,
            priority=task.priority,
            estimated_time=task.estimated_time,
            due_date=datetime.strptime(task.due_date, '%Y-%m-%d'),
            notes=task.notes
        )
        self.session.add(db_task)
        self.session.commit()

    def delete_task(self, task_id):
        """
        Elimina una tarea de la base de datos.

        Args:
            task_id (int): El ID de la tarea a eliminar.
        """
        task = self.session.query(TaskModel).filter_by(id=task_id).first()
        if task:
            self.session.delete(task)
            self.session.commit()

    def get_all_tasks(self):
        """
        Recupera todas las tareas de la base de datos.

        Returns:
            list: Una lista de todas las tareas en la base de datos.
        """
        return self.session.query(TaskModel).all()

    def update_task_status(self, task_id, status):
        """
        Actualiza el estado de una tarea.

        Args:
            task_id (int): El ID de la tarea a actualizar.
            status (str): El nuevo estado de la tarea ('completada' o 'pendiente').
        """
        task = self.session.query(TaskModel).filter_by(id=task_id).first()
        if task:
            task.completed = (status == 'completed')
            self.session.commit()
