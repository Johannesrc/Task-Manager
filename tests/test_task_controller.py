import unittest
from unittest.mock import Mock, patch
from controllers.task_controller import TaskController
from database.models import Task as TaskModel


class TestTaskController(unittest.TestCase):

    @patch('controllers.task_controller.Session')
    @patch('controllers.task_controller.TaskRepository')
    def setUp(self, mock_repo, mock_session):
        self.mock_repo = mock_repo.return_value
        self.mock_session = mock_session.return_value
        self.controller = TaskController()

    def test_add_task(self):
        self.controller.add_task(
            'Test Task', 'Test', 'Description', 'John', 'high', 2, '2023-08-01', 'Notes')
        self.mock_repo.add_task.assert_called_once()

    def test_delete_task(self):
        self.controller.delete_task(1)
        self.mock_repo.delete_task.assert_called_once_with(1)

    def test_list_tasks(self):
        mock_tasks = [Mock(spec=TaskModel), Mock(spec=TaskModel)]
        self.mock_repo.get_all_tasks.return_value = mock_tasks
        tasks = self.controller.list_tasks()
        self.assertEqual(tasks, mock_tasks)

    def test_update_task_status(self):
        self.controller.update_task_status(1, 'completed')
        self.mock_repo.update_task_status.assert_called_once_with(
            1, 'completed')


if __name__ == '__main__':
    unittest.main()
