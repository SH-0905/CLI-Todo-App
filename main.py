TODO_FILE = "todo.txt"

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def add_task(taskList):
    task = input("Add task: ")
    taskList.append(task)

def view_tasks(taskList):
    for i, task in enumerate (taskList, 1):
        print(f'{i}. {task}')

def mark_task(taskList):
    try:
        task = int(input("Mark task: "))
        if taskList[task-1].startswith('DONE -- '):
            taskList[task-1] = taskList[task-1].replace('DONE -- ', "")
        else:
            taskList[task-1] = f'DONE -- {taskList[task-1]}'
    except IndexError:
        print("Invalid Selection.")

def delete_task(taskList):
    try:
        task = int(input("Delete task: "))
        taskList.pop(task-1)
        return taskList
    except IndexError:
        print("Invalid Selection.")

def save_tasks(taskList):
    with open(TODO_FILE, "w") as file:
        for task in taskList:
            file.write(f'{task}\n')

def main():
    taskList = load_tasks()
    while True:
        option = input("""
        ----------------Todo App-----------------------
        1. Add Task
        2. View Tasks
        3. Toggle Task Status
        4. Delete Task
        5. Save & Quit
        Please Select an Option: """)
        if option == '1':
            add_task(taskList)
        elif option == '2':
            view_tasks(taskList)
        elif option == '3':
            mark_task(taskList)
        elif option == '4':
            taskList = delete_task(taskList)
        elif option == '5':
            save_tasks(taskList)
            break
        else:
            print("Invalid Selection.")

if __name__ == "__main__":
    main()