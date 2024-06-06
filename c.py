import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        self.tasks_frame = tk.Frame(self.root)
        self.tasks_frame.pack(fill=tk.BOTH, expand=1)
        
        self.scrollbar = tk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(self.tasks_frame, yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE, font='normal 15')
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(fill=tk.X)
        
        self.task_entry = tk.Entry(self.entry_frame, font='normal 15')
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=1, padx=10, pady=10)
        
        self.add_button = tk.Button(self.entry_frame, text="Add Task", font='normal 15', command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(fill=tk.X)
        
        self.edit_button = tk.Button(self.buttons_frame, text="Edit Task", font='normal 15', command=self.edit_task)
        self.edit_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.delete_button = tk.Button(self.buttons_frame, text="Delete Task", font='normal 15', command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
        
    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            current_task = self.tasks[selected_task_index]
            new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to edit.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")
        
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
