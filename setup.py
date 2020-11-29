"""
Simple Calculator - Hageru Ray 2020
The code looks bad and hard to understand
"""


import tkinter as tk

APP_NAME = "Simple Calculator"


class GUI:
    def __init__(self, author):
        self.variable = ''
        self.variable_main = 0
        self.title = author
        self.size = '350x380'
        self.symbol = ''

        self.bg_main = "#1F1F1F"
        self.bg_one = "#FFFFFF"
        self.bg_two = "#131313"
        self.bg_three = "#343434"
        self.bg_four = "#060606"
        self.bg_five = "#31302F"

    def clear_variable(self):
        self.variable = ''
        self.variable_main = 0
        self.symbol = ''
        variable_one.set(self.variable)

    def set_value(self, symbol=''):
        if symbol != '':
            if True:
                if self.variable_main == 0:
                    self.variable_main = self.variable
                if self.symbol == '+':
                    self.variable_main = float(self.variable_main) + float(self.variable)
                if self.symbol == '-':
                    self.variable_main = float(self.variable_main) - float(self.variable)
                if self.symbol == '×':
                    self.variable_main = float(self.variable_main) * float(self.variable)
                if self.symbol == '÷':
                    self.variable_main = float(self.variable_main) / float(self.variable)
                self.variable = ''
                self.symbol = symbol
            if symbol == '√x':
                self.variable = float(self.variable_main) ** (1 / 2)
                self.symbol = ''
                self.variable_main = 0
            elif symbol == '1/x':
                self.variable = 1 / float(self.variable_main)
                self.symbol = ''
                self.variable_main = 0
            elif symbol == 'x*2':
                self.variable = float(self.variable_main) ** 2
                self.symbol = ''
                self.variable_main = 0
            variable_one.set(self.variable)
        if symbol == '':
            if self.symbol == '+':
                self.variable = float(self.variable_main) + float(self.variable)
            if self.symbol == '-':
                self.variable = float(self.variable_main) - float(self.variable)
            if self.symbol == '×':
                self.variable = float(self.variable_main) * float(self.variable)
            if self.symbol == '÷':
                self.variable = float(self.variable_main) / float(self.variable)
            self.variable_main = 0
            variable_one.set(self.variable)
            self.symbol = symbol

    def set_variable(self, variable):
        self.variable = str(self.variable) + str(variable)
        variable_one.set(self.variable)

    def gui_setup(self):
        main_gui.pack()

        window.title(self.title)
        window.geometry(self.size)
        window.configure(bg=self.bg_main)
        main_gui.configure(bg=self.bg_main)

    def gui_pretty(self):
        number = tk.Label(anchor='e', textvariable=variable_one, master=main_gui, relief='flat',
                          font=("Arial", 40, "bold"), bd=0, width=9, fg=self.bg_one,
                          bg=self.bg_main)
        destroy = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                            relief='flat', bd=0, width=20, height=2, fg=self.bg_one, bg=self.bg_five,
                            text="CLEAR VARIABLE", command=lambda: self.clear_variable())

        one_per_x = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                              relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                              text="1/x", command=lambda: self.set_value('1/x'))
        x_power_2 = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                              relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                              text="x*2", command=lambda: self.set_value('x*2'))
        x_root_2 = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                             relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                             text="√x", command=lambda: self.set_value('√x'))
        divide = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                           relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_two,
                           text="÷", command=lambda: self.set_value('÷'))

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
                             text="×", command=lambda: self.set_value('×'))

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
                          text="--", command=lambda: self.set_value('-'))

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
                        text="+", command=lambda: self.set_value('+'))

        plus_minus = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                               relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                               text="±")
        zero = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                         relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                         text="0", command=lambda: self.set_variable(0))
        dot = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                        relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_four,
                        text=".")
        equals = tk.Button(master=main_gui, activebackground=self.bg_three, font=("Arial", 12, "bold"),
                           relief='flat', bd=0, width=7, height=2, fg=self.bg_one, bg=self.bg_five,
                           text="=", command=lambda: self.set_value())

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

    variable_one = tk.StringVar(main_gui)

    interface = GUI(APP_NAME)
    interface.gui_setup()
    interface.gui_pretty()

    window.mainloop()
