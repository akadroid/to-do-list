# Danny Huynh

#user: danny
#password: huynh

import tkinter as tk
import json

class Task:
    def __init__(self, var, checkbtn, labels, index):
        self.var = var
        self.checkbtn = checkbtn
        self.checkbtn['command'] = lambda: self.select_task()
        self.labels = labels
        self.index = index

    def select_task(self):
        if self.var.get() == 1:
            for i in self.labels:
                i['bg'] = 'spring green'
        else:
            for i in self.labels:
                i['bg'] = 'white'

# Login Screen
class Login_Screen(tk.Frame):
    def __init__(self, container, passwords):
        super().__init__(container)
        self.container = container
        self.passwords = passwords
        
        self.username_label = tk.Label(self, text='username')
        self.username_var = tk.StringVar()
        self.username_box = tk.Entry(self, textvariable = self.username_var)
        
        self.password_label = tk.Label(self, text='password')
        self.password_var= tk.StringVar()
        self.password_box = tk.Entry(self, textvariable= self.password_var, show="*")
        
        self.login_button = tk.Button(self, text="Login", command=self.pass_check)
        
        self.username_label.pack()
        self.username_box .pack()
        self.password_label.pack()
        self.password_box.pack()
        self.login_button.pack()
        
        self.pack()
        
    def pass_check(self):
        if self.password_var.get() == self.passwords[self.username_var.get()]:
            username = self.username_var.get()
            print("Deez Nuts")
            self.destroy()

            app = Application(self.container, username)


# Main Application
class Application(tk.Frame):
    def __init__(self, container, username):
        super().__init__(container)
        self.container = container
        self.username = username
        self.items = []
        self.counter = 0
        
        self.file = open("todolist.json", "r")
        self.x = self.file.readline()
        self.list = json.loads(self.x)
        self.file.close()

        self.initialize_main()
        self.pack()

    def initialize_main(self):
        def run():
            self.main = Main(self, self.list, self.items, self.username)
            self.button = Buttons(self, self.list, self.main, self.items, self.username)

            self.main.pack()
            self.button.pack(pady='10')
            
        if self.counter == 0:
            self.counter += 1
            run()
        else:
            self.main.destroy()
            self.button.destroy()
            run()

#Add, edit, sort, delete buttons
class Buttons(tk.Frame):
    def __init__(self, container, user_list, main, items, username):
        super().__init__(container)
        self.container = container
        self.user_list = user_list
        self.main = main
        self.items = items
        self.username = username

        self.add = tk.Button(self, text='add', command=self.add_window)
        self.delete = tk.Button(self, text='delete', command=self.delete_task)
        self.edit = tk.Button(self, text='edit', command=self.add_window)
        self.sort = tk.Button(self, text='sort', command=self.add_window)
        self.save = tk.Button(self, text='save', command=self.save_task)

        self.add.pack(side='left', ipadx='10', ipady='3')
        self.delete.pack(side='left', ipadx='10', ipady='3')
        self.edit.pack(side='left', ipadx='10', ipady='3')
        self.sort.pack(side='left', ipadx='10', ipady='3')
        self.save.pack(side='left', ipadx='10', ipady='3')

    def add_window(self):
        def add_confirm():
            self.tasklist = []
            self.tasklist.extend([self.task_var.get(), self.desc_var.get(), self.date_var.get(), self.status_var.get(), self.priority_var.get()])
            self.user_list[self.username].append(self.tasklist)
            self.container.initialize_main()

        self.win = tk.Toplevel()
        self.win.geometry("400x250")
        
        self.task_var = tk.StringVar()
        self.desc_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.status_var = tk.StringVar()
        self.priority_var = tk.StringVar()

        self.task_label = tk.Label(self.win, text='Task')
        self.desc_label = tk.Label(self.win, text='Desc')
        self.date_label = tk.Label(self.win, text='Date')
        self.status_label = tk.Label(self.win, text='Status')
        self.priority_label = tk.Label(self.win, text='Priority')

        self.task_entry = tk.Entry(self.win, textvariable = self.task_var)
        self.desc_entry = tk.Entry(self.win, textvariable = self.desc_var)
        self.date_entry = tk.Entry(self.win, textvariable = self.date_var)
        self.status_entry = tk.Entry(self.win, textvariable = self.status_var)
        self.priority_entry = tk.Entry(self.win, textvariable = self.priority_var)
        
        self.confirm = tk.Button(self.win, text='Submit', command=add_confirm)

        self.task_label.pack()
        self.task_entry.pack()
        self.desc_label.pack()
        self.desc_entry.pack()
        self.date_label.pack()
        self.date_entry.pack()
        self.status_label.pack()
        self.status_entry.pack()
        self.priority_label.pack()
        self.priority_entry.pack()
        self.confirm.pack()

    def delete_task(self):
        for num, task in reversed(list(enumerate(self.items))):
            print(task)
            if task.var.get() == 1:
                for label in task.labels:
                    label.destroy()
                self.items.pop(num)
                self.user_list[self.username].pop(num)
    
    def save_task(self):
        self.json_dict = json.dumps(self.user_list)
        self.f = open("todolist.json", "w")
        print(self.json_dict)
        self.f.write(self.json_dict)
        self.f.close()

        self.container.container.destroy()

class Main(tk.Frame):
    def __init__(self, container, user_list, items, username):
        super().__init__(container)
        self.container = container
        self.user_list = user_list
        self.items = items
        self.username = username

        self.radio_p = tk.Radiobutton(self)
        self.task_l = tk.Label(self, text='Task', font=("Arial", 16))        
        self.description_l = tk.Label(self, text='Description', font=("Arial", 16))
        self.date_l = tk.Label(self, text='Date', font=("Arial", 16))
        self.status_l = tk.Label(self, text='Status', font=("Arial", 16))
        self.priority_l = tk.Label(self, text='Priority', font=("Arial", 16))
        
        self.radio_p.grid(column=0, row=0)
        self.task_l.grid(column=1, row=0, ipadx='50', ipady='10')
        self.description_l.grid(column=2, row=0, ipadx='50', ipady='10')
        self.date_l.grid(column=3, row=0, ipadx='50', ipady='10')
        self.status_l.grid(column=4, row=0, ipadx='50', ipady='10')
        self.priority_l.grid(column=5, row=0, ipadx='50', ipady='10')
        self.radio_p.grid_remove()

        self.draw_task()
    
    def draw_task(self, r=0):
        self.items.clear()  
        for i in self.user_list[self.username]:
            c = 1
            r += 1
            self.labels = []
            self.var = tk.IntVar()
            
            self.task_checkbtn = tk.Checkbutton(self, variable = self.var, bg='white')
            self.labels.append(self.task_checkbtn)
            self.task_checkbtn.grid(column=0, row=r, ipady='5')
            
            for j in i:
                self.l = tk.Label(self, text=j, bg='white')
                self.labels.append(self.l)
                self.l.grid(column=c, row=r, ipady='5', sticky="nsew")
                c += 1

            self.task = Task(self.var, self.task_checkbtn, self.labels, r - 1)
            self.items.append(self.task)

def main():
    file = open("passwords.json", "r")
    x = file.readline()
    pass_dict = json.loads(x)
    file.close()
    
    root = tk.Tk()
    root.geometry("1000x800")
    root.title("To-Do List")
    
    # Goes from Login screen to Application after successful login
    login = Login_Screen(root, pass_dict)
    root.mainloop()
main()
    
