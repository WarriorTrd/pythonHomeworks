class task():
    def __init__(self,Task_ID,Title,Description,Due_Date,Status):
        self.Task_ID=Task_ID
        self.Title=Title
        self.Description=Description
        self.Due_Date=Due_Date
        self.Status=Status
    def add_task(self):
        with open("task.txt","a") as file:
            file.write(f"{self}\n")
        print("Task added successfully!")
    def view_all_tasks(self):
        with open("task.txt","r") as file:
            records = file.readlines()
            print("Task Records:{records}")
        if not records:
            print("No task records found.")
    def update_task(self):
        new=int(input("enter the id of the task you want to update: "))
        with open("task.txt","r") as file:
            for line in file:
                data=line.strip().split(", ")
                if data[0]==new:
                    Task_ID=input("Enter Task ID: ")
                    Title=input("Enter Title: ")    
                    Description=input("Enter Description: ")
                    Due_Date=input("Enter Due Date: ")  
                    Status=input("Enter Status: ")
                    task1=task(Task_ID,Title,Description,Due_Date,Status)
                    task1.add_task()
                else:
                    print("Task not found")
    def delete_task(self):
        new=int(input("enter the id of the task you want to delete: "))
        tasks=[]
        deleted=False
        with open("task.txt","r") as file:
            for line in file:
                data=line.strip().split(", ")
                if data[0]==new:
                    tasks.append(f"{Task_ID}, {Title}, {Description}, {Due_Date}, {Status}\n")
                    deleted=True
                else:
                    tasks.append(line)
        if deleted:
            with open("task.txt","w") as file:
                file.writelines(tasks)
            print("Task deleted successfully!")
        else:
            print("Task not found.")
    def filter_task(self):
        new=input("enter the status of the task you want to filter: ")
        with open("task.txt","r") as file:
            for line in file:
                data=line.strip().split(", ")
                if data[4]==new:
                    print(data)
                else:
                    print("Task not found")




option=int(input("""Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit"""))    
if option==1:
    Task_ID=input("Enter Task ID: ")
    Title=input("Enter Title: ")    
    Description=input("Enter Description: ")
    Due_Date=input("Enter Due Date: ")  
    Status=input("Enter Status: ")
    task1=task(Task_ID,Title,Description,Due_Date,Status)
    task1.add_task()
elif option==2:
    task.view_all_tasks()  
elif option==3:
    task.update_task()
elif option==4:
    task.delete_task()
elif option==5:
    task.filter_task()  
elif option==6:
    with open("task.txt","w") as file:
        file.write(f"{task}\n")                  

elif option==8:
    print("Goodbye!")   
    quit()


            