import tkinter as tk
import matplotlib.pyplot as plt
 
root = tk.Tk()
root.title("Simple student Marks Display")
root.geometry("500x500")


subjects = ["English", "Maths", "Science"]
marks={}

input_frame = tk.Frame(root)
input_frame.grid(row=1, column=0)

for subject in subjects:
    marks[subject]= tk.IntVar(value=0)

for i,subject in enumerate(subjects):
    tk.Label(input_frame, text=f"Mark of {subject}").grid(row=i, column=0)
    tk.Entry(input_frame, textvariable=marks[subject]).grid(row=i, column=1)


def gradeFinding(mark):
    if mark >= 80:
        return "A"
    elif mark <80 and mark >=60:
        return "B"
    elif mark <60 and mark >=50:
        return "C"
    else:
        return "D"


def generateReport():
    # print(marks["English"].get())
    # print(marks["Maths"].get())
    # print(marks["Science"].get())

    total_marks = 0
    result_text = ""
    
    # print("Till Here")
    for subject in subjects:
        total_marks+=float(marks[subject].get())
        result_text +=f"Marks of {subject} {gradeFinding(marks[subject].get())} = {marks[subject].get()} \n"
    
    result_text+=f"Total Marks = {total_marks}"
    result_label.config(text=result_text)
    # print(total_marks)

    
    
    mark = [marks["English"].get(), marks["Maths"].get(), marks["Science"].get()]
    plt.bar(subjects, mark)
    plt.title("Student Marks Graph")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()

tk.Button(input_frame, text="Generate Report", command=generateReport).grid(row=4, column=0)
result_label=tk.Label(input_frame, text="Result")
result_label.grid(row=5, column=0)

root.mainloop()