"""
Simple Calculator - Hageru Ray 2020
The code looks bad and hard to understand
"""


import tkinter as tk

APP_NAME = "Simple Calculator"


class GUI:
    def __init__(self, author):
        self.variable_one = ''
        self.variable_two = ''
        self.variable_text = ''
        self.operator = ''
    
        self.title = author
        self.size = '350x380'

        self.bg_main = "#1F1F1F"
        self.bg_one = "#FFFFFF"
        self.bg_two = "#131313"
        self.bg_three = "#343434"
        self.bg_four = "#060606"
        self.bg_five = "#31302F"

    def set_variable(self, variable):
        if self.operator == '': # Set Variable One
            if self.variable_one == '' and variable == '.':
                self.variable_one = str(0) + str(variable)
                self.variable_text = self.variable_one
            if self.variable_one.find('.') != -1 and variable == '.':
                pass
            else:
                self.variable_one = str(self.variable_one) + str(variable)
                self.variable_text = self.variable_one
        else: # Set Variable Two
            if self.variable_two == '' and variable == '.':
                self.variable_two = str(0) + str(variable)
                self.variable_text = self.variable_two
            if self.variable_two.find('.') != -1 and variable == '.':
                pass
            else:
                self.variable_two = str(self.variable_two) + str(variable)
                self.variable_text = self.variable_two
        display.set(self.variable_text)
        
    def set_operator(self, operator=''):
        if self.operator != '':
            self.set_value()
        self.operator = operator

    def set_value(self):
        if self.operator == '+':
            self.variable_one = str(float(self.variable_one) + float(self.variable_two))
        if self.operator == '-':
            self.variable_one = str(float(self.variable_one) - float(self.variable_two))
        if self.operator == '×':
            self.variable_one = str(float(self.variable_one) * float(self.variable_two))
        if self.operator == '÷':
            self.variable_one = str(float(self.variable_one) / float(self.variable_two))
        self.variable_two = ''
        self.variable_text = round(float(self.variable_one), 3)
        display.set(self.variable_text)
    
    def set_value_two(self, operator):
        if operator == 'x*2':
            self.variable_one = str(float(self.variable_one) ** 2)
        if operator == '√x':
            self.variable_one = str(float(self.variable_one) ** (1/2))
        if operator == '1/x':
            self.variable_one = str(1 / float(self.variable_one))
        self.variable_text = round(float(self.variable_one), 3)
        display.set(self.variable_text)
        
    def set_clear(self):
        self.variable_one = ''
        self.variable_two = ''
        self.variable_text = ''
        self.symbol = ''
        display.set(self.variable_text)
        
    def gui_setup(self):
        main_gui.pack()

        window.title(self.title)
        window.geometry(self.size)
        window.configure(bg=self.bg_main)
        main_gui.configure(bg=self.bg_main)

    def gui_main(self):
        number = tk.Label(anchor='e', textvariable=display, master=main_gui, relief='flat',
                          font=("Arial", 40, "bold"), bd=0, width=9, fg=self.bg_one,
                          bg=self.bg_main)
        destroy = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                            relief='flat', bd=0, width=20, height=2, fg=self.bg_one, bg=self.bg_five,
                            text="CLEAR VARIABLE", command=lambda: self.set_clear())

        one_per_x = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                              relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                              text="1/x", command=lambda: self.set_value_two('1/x'))
        x_power_2 = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                              relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                              text="x*2", command=lambda: self.set_value_two('x*2'))
        x_root_2 = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                             relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                             text="√x", command=lambda: self.set_value_two('√x'))
        divide = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                           relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                           text="÷", command=lambda: self.set_operator('÷'))

        seven = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                          relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                          text="7", command=lambda: self.set_variable(7))
        eight = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                          relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                          text="8", command=lambda: self.set_variable(8))
        nine = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                         relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                         text="9", command=lambda: self.set_variable(9))
        multiply = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                             relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                             text="×", command=lambda: self.set_operator('×'))

        four = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                         relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                         text="4", command=lambda: self.set_variable(4))
        five = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                         relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                         text="5", command=lambda: self.set_variable(5))
        six = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                        relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                        text="6", command=lambda: self.set_variable(6))
        minus = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                          relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                          text="--", command=lambda: self.set_operator('-'))

        one = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                        relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                        text="1", command=lambda: self.set_variable(1))
        two = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                        relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                        text="2", command=lambda: self.set_variable(2))
        three = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                          relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                          text="3", command=lambda: self.set_variable(3))
        add = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                        relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                        text="+", command=lambda: self.set_operator('+'))

        plus_minus = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                               relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                               text="±")
        zero = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                         relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                         text="0", command=lambda: self.set_variable(0))
        dot = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                        relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                        text=".", command=lambda: self.set_variable('.'))
        equals = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                           relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_five,
                           text="=", command=lambda: self.set_operator())

        number.grid(column=0, row=0, columnspan=4, pady=5)
        destroy.grid(column=0, row=7, columnspan=3, pady=1)

        one_per_x.grid(column=0, row=2, pady=1, padx=1)
        x_power_2.grid(column=1, row=2, pady=1, padx=1)
        x_root_2.grid(column=2, row=2, pady=1, padx=1)
        divide.grid(column=3, row=2, pady=1, padx=1)

        seven.grid(column=0, row=3, pady=1, padx=1)
        eight.grid(column=1, row=3, pady=1, padx=1)
        nine.grid(column=2, row=3, pady=1, padx=1)
        multiply.grid(column=3, row=3, pady=1, padx=1)

        four.grid(column=0, row=4, pady=1, padx=1)
        five.grid(column=1, row=4, pady=1, padx=1)
        six.grid(column=2, row=4, pady=1, padx=1)
        minus.grid(column=3, row=4, pady=1, padx=1)

        one.grid(column=0, row=5, pady=1, padx=1)
        two.grid(column=1, row=5, pady=1, padx=1)
        three.grid(column=2, row=5, pady=1, padx=1)
        add.grid(column=3, row=5, pady=1, padx=1)

        plus_minus.grid(column=0, row=6, pady=1, padx=1)
        zero.grid(column=1, row=6, pady=1, padx=1)
        dot.grid(column=2, row=6, pady=1, padx=1)
        equals.grid(column=3, row=6, pady=1, padx=1)


if __name__ == "__main__":
    window = tk.Tk()
    main_gui = tk.Frame(master=window)

    display = tk.StringVar(main_gui)

    interface = GUI(APP_NAME)
    interface.gui_setup()
    interface.gui_main()

    window.mainloop()
    