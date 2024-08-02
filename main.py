"""
Este módulo proporciona una interfaz de línea de comandos interactiva para el sistema de gestión de tareas.
Utiliza la biblioteca inquirer para crear un menú interactivo y tabulate para mostrar las tareas en formato de tabla.
"""

import inquirer
from controllers.task_controller import TaskController
import logging
from tabulate import tabulate

# Configuración de logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def add_task():
    """
    Función para añadir una nueva tarea.
    Solicita al usuario los detalles de la tarea y la añade a la base de datos.
    """
    questions = [
        inquirer.Text('title', message="Título de la tarea"),
        inquirer.Text('category', message="Categoría"),
        inquirer.Text('description', message="Descripción"),
        inquirer.Text('responsible', message="Responsable"),
        inquirer.List('priority', message="Prioridad",
                      choices=['baja', 'media', 'alta']),
        inquirer.Text('estimated_time', message="Tiempo estimado (horas)"),
        inquirer.Text('due_date', message="Fecha de vencimiento (YYYY-MM-DD)"),
        inquirer.Text('notes', message="Notas")
    ]
    answers = inquirer.prompt(questions)
    controller = TaskController()
    controller.add_task(**answers)
    print('¡Tarea añadida con éxito!')
    logging.info('Tarea añadida con éxito')


def delete_task():
    """
    Función para eliminar una tarea existente.
    Solicita al usuario el ID de la tarea a eliminar y la borra de la base de datos.
    """
    questions = [
        inquirer.Text('task_id', message="ID de la tarea a eliminar")
    ]
    answers = inquirer.prompt(questions)
    controller = TaskController()
    controller.delete_task(answers['task_id'])
    print('¡Tarea eliminada con éxito!')
    logging.info('Tarea eliminada con éxito')


def list_tasks():
    """
    Función para listar todas las tareas.
    Recupera todas las tareas de la base de datos y las muestra al usuario en formato de tabla.
    """
    try:
        controller = TaskController()
        tasks = controller.list_tasks()
        table_data = []
        for task in tasks:
            table_data.append([
                task.id,
                task.title,
                task.category,
                task.responsible,
                task.priority,
                task.due_date,
                "Completada" if task.completed else "Pendiente"
            ])
        headers = ["ID", "Título", "Categoría", "Responsable",
                   "Prioridad", "Fecha de vencimiento", "Estado"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        logging.info('Tareas listadas con éxito')
    except Exception as e:
        print(f'Error al listar las tareas: {str(e)}')
        logging.error(f'Error al listar las tareas: {str(e)}')


def update_task_status():
    """
    Función para actualizar el estado de una tarea.
    Solicita al usuario el ID de la tarea y el nuevo estado, y actualiza la tarea en la base de datos.
    """
    questions = [
        inquirer.Text('task_id', message="ID de la tarea"),
        inquirer.List('status', message="Nuevo estado",
                      choices=['pendiente', 'completada'])
    ]
    answers = inquirer.prompt(questions)
    try:
        controller = TaskController()
        controller.update_task_status(answers['task_id'], answers['status'])
        print('¡Estado de la tarea actualizado con éxito!')
        logging.info(f'Estado de la tarea actualizado: {
                     answers["task_id"]} - {answers["status"]}')
    except Exception as e:
        print(f'Error al actualizar el estado de la tarea: {str(e)}')
        logging.error(f'Error al actualizar el estado de la tarea: {str(e)}')


def main() -> int:
    """
    Función principal que muestra el menú interactivo y maneja la lógica principal del programa.

    Returns:
        int: Código de salida del programa (0 para salida exitosa).
    """
    actions = [
        inquirer.List('action', message="¿Qué deseas hacer?", choices=[
            'Añadir Tarea', 'Eliminar Tarea', 'Listar Tareas', 'Actualizar Estado de Tarea', 'Salir'
        ])
    ]

    while True:
        # Muestra el menú principal y obtiene la elección del usuario
        answer = inquirer.prompt(actions)

        # Ejecuta la acción correspondiente según la elección del usuario
        if answer['action'] == 'Añadir Tarea':
            add_task()
        elif answer['action'] == 'Eliminar Tarea':
            delete_task()
        elif answer['action'] == 'Listar Tareas':
            list_tasks()
        elif answer['action'] == 'Actualizar Estado de Tarea':
            update_task_status()
        elif answer['action'] == 'Salir':
            break

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
