import tkinter as tk

symbols = ['7','8','9', '/', 'C', 
            '4', '5', '6', '*', '(',
            '1', '2', '3', '+', ')',
            ',', '0', '%', '-', '=']

def initializeWindow():
    root = tk.Tk()

    root.geometry('500x500')
    root.title('Calc')
    return root

def initializeScreen(root):
    screen = [tk.Label(root, width = 60, bg = '#545454', text = 'test', anchor = 'center', borderwidth = 3 ) for i in range(3)]

    for i in range(len(screen)):
        screen[i].grid(row = i, columnspan = 5, ipadx = 10, ipady = 10)
    return screen

def initializeDataField(root, screen):
    data_field = tk.Entry(root)
    data_field.grid(row = len(screen), columnspan = 5, ipadx = 100, ipady = 5)

    info = tk.Label(root, width = 60, bg = 'green', text = 'info', anchor = 'center', borderwidth = 2)
    info.grid(row = len(screen) + 1, columnspan = 5, ipady = 15, ipadx = 1)

    return data_field

def initializeButtons(root, screen):
    button = [tk.Button(root, text = symb) for symb in symbols]
    j = len(screen)+2
    for i in range(len(button)):
        if i%5 == 0:
            j+=1
        button[i].grid(row = j, column = i % 5, ipadx = 5, ipady = 5)
        button[i].configure(command)
    return button

def click(data_field, symbol):


if __name__ == '__main__':

    root = initializeWindow()
    screen = initializeScreen(root)
    data_field = initializeDataField(root, screen)
    initializeButtons(root, screen)


    root.mainloop()


