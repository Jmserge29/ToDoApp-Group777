from task_model import TaskModel

def main():
    task1 = TaskModel("Estudiar para el examen")
    print(f"Tarea creada: {task1.get_task_name()}")
    task.set_done()
    print(f"Tarea Completada: {task.is_done()}")
    task.remove_task()
    print(f"Tarea Elimina: {task.get_task_name()}")

if __name__ == "__main__":
    main()

