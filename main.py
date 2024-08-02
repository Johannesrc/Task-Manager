"""
Este módulo proporciona una interfaz de línea de comandos interactiva para el sistema de gestión de tareas.

Utiliza la biblioteca inquirer para crear un menú interactivo y opciones para añadir, eliminar, listar y actualizar tareas.
"""

import inquirer
from controllers.task_controller import TaskController
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# TODO: Implementar la funcionalidad para mostrar la información de las tareas en tablas bien formateadas.

# TODO: Añadir una opción para cambiar el estado de una tarea directamente desde el menú principal.


def add_task():
    """
    Función para añadir una nueva tarea.
    Solicita al usuario los detalles de la tarea y la añade a la base de datos.
    """
    questions = [
        inquirer.Text('title', message="Task title"),
        inquirer.Text('category', message="Category"),
        inquirer.Text('description', message="Description"),
        inquirer.Text('responsible', message="Responsible"),
        inquirer.List('priority', message="Priority",
                      choices=['low', 'medium', 'high']),
        inquirer.Text('estimated_time', message="Estimated time (hours)"),
        inquirer.Text('due_date', message="Due date (YYYY-MM-DD)"),
        inquirer.Text('notes', message="Notes")
    ]
    answers = inquirer.prompt(questions)
    controller = TaskController()
    controller.add_task(**answers)
    print('Task added successfully!')
    logging.info('Task added successfully')

# TODO: Implementar la funcionalidad para cambiar el estado de una tarea.


def delete_task():
    """
    Función para eliminar una tarea existente.
    Solicita al usuario el ID de la tarea a eliminar y la borra de la base de datos.
    """
    questions = [
        inquirer.Text('task_id', message="Task ID to delete")
    ]
    answers = inquirer.prompt(questions)
    controller = TaskController()
    controller.delete_task(answers['task_id'])
    print('Task deleted successfully!')
    logging.info('Task deleted successfully')


def list_tasks():
    """
    Función para listar todas las tareas.
    Recupera todas las tareas de la base de datos y las muestra al usuario.
    """
    try:
        controller = TaskController()
        tasks = controller.list_tasks()
        # TODO: Formatear la salida de las tareas en una tabla bien estructurada.
        for task in tasks:
            print(task)
        logging.info('Tasks listed successfully')
    except Exception as e:
        print(f'Error listing tasks: {str(e)}')
        logging.error(f'Error listing tasks: {str(e)}')


def update_task_status():
    """
    Función para actualizar el estado de una tarea.
    Solicita al usuario el ID de la tarea y el nuevo estado, y actualiza la
    tarea en la base de datos.
    """
    questions = [
        inquirer.Text('task_id', message="Task ID"),
        inquirer.List('status', message="New status",
                      choices=['pending', 'completed'])
    ]
    answers = inquirer.prompt(questions)
    try:
        controller = TaskController()
        controller.update_task_status(answers['task_id'], answers['status'])
        print('Task status updated successfully!')
        logging.info(f'Task status updated: {
                     answers["task_id"]} - {answers["status"]}')
    except Exception as e:
        print(f'Error updating task status: {str(e)}')
        logging.error(f'Error updating task status: {str(e)}')


def main() -> int:
    """
    Función principal que muestra el menú interactivo y maneja la lógica
    principal del programa.

    Returns:
        int: Código de salida del programa (0 para salida exitosa).
    """

    actions = [
        inquirer.List('action', message="What do you want to do?", choices=[
            'Add Task', 'Delete Task', 'List Tasks', 'Update Task Status', 'Exit'
        ])
    ]

    while True:
        # Muestra el menú principal y obtiene la elección del usuario
        answer = inquirer.prompt(actions)

        # Ejecuta la acción correspondiente según la elección del usuario
        match answer['action']:
            case 'Add Task':
                add_task()
            case 'Delete Task':
                delete_task()
            case 'List Tasks':
                list_tasks()
            case 'Update Task Status':
                update_task_status()
            case 'Exit':
                break

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
