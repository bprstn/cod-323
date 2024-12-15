# Name: Brian Preston
# Module: 10
# This Tkinter application has been enhanced with several features for a To-Do List.
# Modifications include:
# - Setting up dynamic event bindings to accommodate both Mac (uses Button-2) and Windows/Linux (uses Button-3) for right-click deletion of tasks. I needed to do this becasue the code would not allow me to delete it with a right click on my macbook
# - Customizing the UI with predefined tasks and color schemes of violet red and lime green.( My favorites!)
# - Adding a menu item for proper application exit.
# - Providing instructions within the application on how to delete tasks.
import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        if not tasks:
            self.tasks = ["Wake up at 7 am drink water", "Make coffee at 8 am"]
        else:
            self.tasks = tasks

        self.tasks_canvas = tk.Canvas(self)
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.title("Preston-ToDo")  # Changed title
        self.geometry("300x400")

        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas_frame = self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="n")
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        # Instruction label
        instruction = tk.Label(self.tasks_frame, text="Right-click on a task to delete it", bg="white", fg="black", pady=10)
        instruction.pack(side=tk.TOP, fill=tk.X)

        # Use Button-3 for Windows/Linux, Button-2 for Mac
        right_click_button = "<Button-2>" if self.tk.call('tk', 'windowingsystem') == 'aqua' else "<Button-3>"

        # Create initial task labels
        for task_text in self.tasks:
            task = tk.Label(self.tasks_frame, text=task_text, pady=10, bg="violet red", fg="lime green")
            task.bind(right_click_button, self.remove_task)  # Change to right mouse button
            task.pack(side=tk.TOP, fill=tk.X)

        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)

        # Add menu for exiting
        menu = tk.Menu(self)
        self.config(menu=menu)
        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.destroy)

        self.colour_schemes = [{"bg": "violet red", "fg": "lime green"}, {"bg": "lime green", "fg": "violet red"}]

    def add_task(self, event=None):
        task_text = self.task_create.get(1.0, tk.END).strip()
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10, bg="violet red", fg="lime green")
            right_click_button = "<Button-2>" if self.tk.call('tk', 'windowingsystem') == 'aqua' else "<Button-3>"
            new_task.bind(right_click_button, self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)
            self.tasks.append(new_task)
        self.task_create.delete(1.0, tk.END)

    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(task)
            task.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)

    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        my_scheme_choice = self.colour_schemes[task_style_choice]
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1
            self.tasks_canvas.yview_scroll(move, "units")

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()













