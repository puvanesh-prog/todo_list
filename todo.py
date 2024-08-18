import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="todo_list_db"
    )

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task(s)")
    print("2. Delete task(s)")
    print("3. View tasks")
    print("4. Total tasks")
    print("5. Exit")

def add_tasks():
    db = connect_db()
    cursor = db.cursor()
    task_count = int(input("How many tasks would you like to add (up to 5)? "))
    if task_count < 1 or task_count > 5:
        print("You can add between 1 to 5 tasks at a time.")
    else:
        for _ in range(task_count):
            task = input("Enter the task: ")
            cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
            db.commit()
            print(f"Task '{task}' added.")
    cursor.close()
    db.close()

def delete_tasks():
    db = connect_db()
    cursor = db.cursor()
    task_numbers = input("Enter the task numbers to delete (separated by spaces): ")
    task_numbers = list(map(int, task_numbers.split()))
    
    for task_number in task_numbers:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_number,))
        db.commit()
        print(f"Task with ID '{task_number}' deleted.")
    cursor.close()
    db.close()

def view_tasks():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, task FROM tasks ORDER BY id ASC")
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for idx, task in tasks:
            print(f"{idx}. {task}")
    cursor.close()
    db.close()


def total_tasks():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]
    print(f"Total number of tasks: {total}")
    cursor.close()
    db.close()

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_tasks()
        elif choice == '2':
            delete_tasks()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            total_tasks()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()