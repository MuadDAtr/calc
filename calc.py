import tkinter as tk

def initializeWindow():
    root = tk.Tk()

    root.geometry('500x500')
    root.title('Calc')
    return root

def initializeScreen(root):
    screen = [tk.Label(root, width = 60, bg = '#545454' ) for i in range(3)]

    for i in range(len(scren)):
        screen[i].grid(row - 1, column = 0)
    return screen

if __name__ == '__main__':

    root = initializeWindow()
    screen = initializeScreen()

    root.mainloop()


