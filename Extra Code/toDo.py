import matplotlib.pyplot as plt

todo_task = [
    "week 1 : class",
    "week 2 : class",
    "week 3 : class"
]
task_status = [
    "incomplete",
    "incomplete",
    "incomplete"
]

def addTask():
    task = input("Enter the Task : ")
    if task.strip() == "":
        print("Enter the Task !")
    else:
        todo_task.append(task)
        task_status.append("incomplete")
        print("Task added Successfully.")
    
def updateTask():
    task_num = int(input("Enter the Task Number : "))
    task_status[task_num - 1] = "complete"
    print("Task Updates Successfully")

def viewTask():
    if len(todo_task) == 0:
        print("No Task Found !")
    else:
        print("Task Listed Below")
        for i,(task, status) in enumerate(zip(todo_task, task_status), 1):
            print(f"{i}, ==> {task}, ==> {status}")

def visualize():
    categories = ["complete", "incomplete"]
    counts = [task_status.count("complete"), task_status.count("incomplete")]
    plt.bar(categories, counts)
    plt.title("Task Graph")
    plt.xlabel("Task Status")
    plt.ylabel("Counts")
    plt.show()

def main():
    menu = int(input("Enter the Activity : "))
    if menu == 1:
        addTask()
    elif menu == 2:
        updateTask()
    elif menu == 3:
        viewTask()
    elif menu == 4:
        visualize()
    else:
        print("No menu selected .")
    
if __name__ == "__main__":
    while True:
        print("1. Enter 1 for addTask ")
        print("2. Enter 1 for updateTask ")
        print("3. Enter 1 for viewTask ")
        print("4. Enter 1 for visualizeTask ")
        main()