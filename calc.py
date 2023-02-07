from tkinter import Tk, Button, Entry

def initializeWindow():
    root = tk.Tk()

    root.geometry('600x600')
    root.title('Calc')
    return root

if __name__ == '__main__':

    root.initializeWindow()
    root.mainloop()