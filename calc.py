import tkinter as tk

def initializeWindow():
    root = tk.Tk()

    root.geometry('500x500')
    root.title('Calc')
    return root

if __name__ == '__main__':

    root = initializeWindow()
    root.mainloop()