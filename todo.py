import pickle
# import tkinter as tk

# window = tk.Tk()
# window.title = 'To-Do'
# window.geometry = "900x2000"

# label = tk.Label(text='Hello world')
# label.pack()

def enumerate_list(list):
  if len(list) == 0:
    print()
    print('There\'s no elements in the list')
  else:
    for i, x in enumerate(list):
      if x.completed:
        completed_text = 'complete'
      else:
        completed_text = 'incomplete'
      print(str(i)+'.'+x.description+' ('+completed_text+')')

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def set_completed(self):
        enumerate_list(self.tasks)
        while True:
          try:
            index = int(input('Enter the number of the task you want to mark as completed: '))
            self.tasks[index].completed = True
            print('Task ' + str(index) + ' has been completed.')
            break
          except Exception:
            print('Please enter a valid task number')
    def show_list(self):
      enumerate_list(self.tasks)
    def delete_task(self):
      enumerate_list(self.tasks)
      while True:
        try:
          option = int(input('Enter the number of the task you want to delete: '))
          self.tasks.pop(option)
          print()
          print('Task ' + str(option) + ' deleted')
          break
        except Exception:
          print('Enter a valid task number')

menu = ['Show list', 'Add task', 'Mark as complete', 'Delete task', 'Exit']

try:
  with open('data.pkl', 'rb') as f:
    todo_list = pickle.load(f)
except Exception:
  todo_list = ToDoList()

def main_loop():
  print('--------------')
  print('What do you want to do?')
  print()
  for i, x in enumerate(menu):
    print(str(i)+'. '+x)
  try:
    option = int(input('Input the option number: '))
    print()
    if option == 0:
      todo_list.show_list()
      main_loop()
    elif option == 1:
      description = input('Enter task description: ')
      todo_list.add_task(description)
      with open('data.pkl', 'wb') as f:
        pickle.dump(todo_list, f)
      print()
      print()
      main_loop()
    elif option == 2:
      todo_list.set_completed()
      with open('data.pkl', 'wb') as f:
        pickle.dump(todo_list, f)
      print()
      print()
      main_loop()
    elif option == 3:
      print()
      todo_list.delete_task()
      with open('data.pkl', 'wb') as f:
        pickle.dump(todo_list, f)
      print()
      main_loop()
    elif option == 4:
      print()
      print('Bye!')
  except Exception:
    print('Enter a valid option number')

main_loop()
