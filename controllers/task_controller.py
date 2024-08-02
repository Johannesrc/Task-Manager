import logging

from repositories.task_repository import TaskRepository
from models.task import Task
from database.models import Session


class TaskController:

    def __init__(self):
        self.session = Session()
        self.repository = TaskRepository(self.session)

    def add_task(self, title, category, description, responsible, priority, estimated_time, due_date, notes):
        try:
            task = Task(title, category, description, responsible,
                        priority, estimated_time, due_date, notes)
            self.repository.add_task(task)
            logging.info(f'Task added: {title}')
        except Exception as e:
            logging.error(f'Error adding task: {str(e)}')
            raise

    def delete_task(self, task_id):
        try:
            self.repository.delete_task(task_id)
            logging.info(f'Task deleted: {task_id}')
        except Exception as e:
            logging.error(f'Error deleting task: {str(e)}')
            raise

    def list_tasks(self):
        try:
            return self.repository.get_all_tasks()
        except Exception as e:
            logging.error(f'Error listing tasks: {str(e)}')
            raise

    def update_task_status(self, task_id, status):
        try:
            self.repository.update_task_status(task_id, status)
            logging.info(f'Task status updated: {task_id} - {status}')
        except Exception as e:
            logging.error(f'Error updating task status: {str(e)}')
            raise

    def __del__(self):
        self.session.close()
