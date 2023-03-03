import tkinter as tk

symbols = ['7','8','9', '/', 'C', 
            '4', '5', '6', '*', '(',
            '1', '2', '3', '+', ')',
            ',', '0', '%', '-']

def initializeWindow():
    root = tk.Tk()

    root.geometry('500x500')
    root.title('Calc')
    return root

def initializeScreen(root):
    screen = [tk.Label(root, width = 60, bg = '#545454', text = 'text', anchor = 'center', borderwidth = 3 ) for i in range(3)]

    for i in range(len(screen)):
        screen[i].grid(row = i, columnspan = 5, ipadx = 10, ipady = 10)
    return screen

def initializeDataField(root, screen):
    data_field = tk.Entry(root)
    data_field.grid(row = len(screen), columnspan = 5, ipadx = 100, ipady = 5)

    info = tk.Label(root, width = 60, bg = 'green', text = 'info', anchor = 'center', borderwidth = 2)
    info.grid(row = len(screen) + 1, columnspan = 5, ipady = 15, ipadx = 1)

    return data_field, info

def initializeButtons(root, screen, info):
    button = [tk.Button(root, text = symb) for symb in symbols]
    j = len(screen)+2
    for i in range(len(button)):
        if i%5 == 0:
            j+=1
        button[i].grid(row = j, column = i % 5, ipadx = 5, ipady = 5)
        button[i].configure(command = click(data_field, button[i]['text']))

    eq_sign = tk.Button(root, text = '=', bg = 'green', command = equation(data_field, screen, info))
    eq_sign.grid(row = len(screen)+ 6, column = 4)
    return button

def click(data_field, symbol):
    def click_1():
        if symbol == 'C':
            data_field.delete(0, tk.END)
        else:
            data_field.insert(tk.END, symbol)

    return click_1

def equation(data_field, screen, info):

    def sign_correct(text):
        i=1
        while text[i] == ')':
            i += 1
        return text[-i].isdigit()

    def func():
        text = data_field.get()
        if not sign_correct(text):
            info['text'] = ['Error !!']
            info['bg'] = ['red']
        else:

            for i in range(1, len(screen)):
                if screen[i]['text']:
                    screen[i - 1]['text'] = screen[i]['text']
            screen[-1]['text'] = text + " = " + str(eval(text))
            info['bg'] = ['green']
            info['text'] = ['info']

    return func



if __name__ == '__main__':

    root = initializeWindow()
    screen = initializeScreen(root)
    data_field, info = initializeDataField(root, screen)
    initializeButtons(root, screen, info)


    root.mainloop()


