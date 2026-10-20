
tasks_list = []

def add_task():
    task_id = 0
    for dict in tasks_list:
        for id in dict:
            if dict[id] > id:
                task_id = id
    
    task_title = input("Укажите название задачи: ")
    task_status = input("Укажите название задачи(todo/done): ").lower()

    if task_status != "todo":
        return f"Название {task_status} не подходит"
    if task_status != "done":
        return f"Название {task_status} не подходит"
    
    task_priority = input("Укажите приоритетность задачи(low/medium/high): ").lower
    if task_priority != "low":
        return f"Название {task_priority} не подходит"
    if task_priority != "medium":
        return f"Название {task_priority} не подходит"
    if task_priority != "high":
        return f"Название {task_priority} не подходит"
    
    tasks_list.append(task = {"id": task_id, "title": task_title, "task_status": task_status, "task_priority": task_priority})