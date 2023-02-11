import tkinter as tk

def initializeWindow():
    root = tk.Tk()

    root.geometry('500x500')
    root.title('Calc')
    return root

def initializeScreen(root):
    screen = [tk.Label(root, width = 40, bg = '#545454', text = 'test', anchor = 'w', borderwidth = 3 ) for i in range(3)]

    for i in range(len(screen)):
        screen[i].grid(row = i, column = 0, ipadx = 10, ipady = 10)
    return screen

if __name__ == '__main__':

    root = initializeWindow()
    screen = initializeScreen(root)

    root.mainloop()


