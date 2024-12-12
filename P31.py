#Program 31

import mysql.connector

def initialize_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='19181',  
            database='todo_list'
        )
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INT AUTO_INCREMENT PRIMARY KEY,
                description TEXT NOT NULL,
                deadline DATE,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()

def add_task(description, deadline=None):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='19181',
            database='todo_list'
        )
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (description, deadline, completed)
            VALUES (%s, %s, %s)
        ''', (description, deadline, False))
        conn.commit()
        conn.close()
        print("Task added successfully!")
    except mysql.connector.Error as err:
        print(f"Error adding task: {err}")

def view_tasks():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='19181',
            database='todo_list'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()
        
        if tasks:
            for task in tasks:
                completed = "Completed" if task[3] else "Pending"
                print(f"ID: {task[0]} | Task: {task[1]} | Deadline: {task[2]} | Status: {completed}")
        else:
            print("No tasks available.")
    except mysql.connector.Error as err:
        print(f"Error viewing tasks: {err}")

def mark_task_completed(task_id):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='19181',
            database='todo_list'
        )
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tasks
            SET completed = %s
            WHERE id = %s
        ''', (True, task_id))
        conn.commit()
        conn.close()
        print("Task marked as completed!")
    except mysql.connector.Error as err:
        print(f"Error marking task completed: {err}")

def delete_task(task_id):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='19181',
            database='todo_list'
        )
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tasks WHERE id = %s
        ''', (task_id,))
        conn.commit()
        conn.close()
        print("Task deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error deleting task: {err}")

def menu():
    while True:
        print("\nWelcome to the Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Save Tasks to Text File")
        print("6. Exit")
        
        try:
            choice = int(input("Please choose an option: "))
            
            if choice == 1:
                description = input("Enter task description: ")
                deadline = input("Enter task deadline (YYYY-MM-DD): ")
                add_task(description, deadline)
            
            elif choice == 2:
                view_tasks()
            
            elif choice == 3:
                task_id = int(input("Enter task ID to mark as completed: "))
                mark_task_completed(task_id)
            
            elif choice == 4:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            
            elif choice == 5:
                save_tasks_to_text()
            
            elif choice == 6:
                print("Exiting Task Manager.")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")


def save_tasks_to_text():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='19181',
            database='todo_list'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        conn.close()

        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(f"ID: {task[0]}, Description: {task[1]}, Deadline: {task[2]}, Completed: {'Yes' if task[3] else 'No'}\n")

        print("Tasks saved to tasks.txt")
    except mysql.connector.Error as err:
        print(f"Error saving tasks to text file: {err}")


if __name__ == "__main__":
    initialize_db()
    menu()