import tkinter
import customtkinter

class Calculator:

    # Constructor
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.app = customtkinter.CTk()
        self.app.geometry("240x360")
        self.app.resizable(0, 0)
        self.app.title(' Calculator')
        self.app.iconbitmap('logo.ico')

        self.scvalue = tkinter.StringVar()
        self.scvalue.set("")
        self.expression = customtkinter.CTkEntry(self.app, textvar = self.scvalue, width = 190, height = 35, corner_radius = 8,
                                            justify = 'right')
        self.expression.place(x = 20, y = 20)
        self.expression.update()

        # 1 Row
        self.b1 = customtkinter.CTkButton(self.app, text = '9', width = 40, height = 40, text_font = ('Consolas', 14),
                                    command = lambda: self.button_clicked(self.b1))
        self.b1.place(x = 20, y = 70)

        self.b2 = customtkinter.CTkButton(self.app, text = '8', width = 40, height = 40, text_font = ('Consolas', 14),
                                    command = lambda: self.button_clicked(self.b2))
        self.b2.place(x = 70, y = 70)

        self.b3 = customtkinter.CTkButton(self.app, text = '7', width = 40, height = 40, text_font = ('Consolas', 14),
                                     command = lambda: self.button_clicked(self.b3))
        self.b3.place(x = 120, y = 70)

        self.b4 = customtkinter.CTkButton(self.app, text = 'C', width = 40, height = 40, text_font = ('Consolas', 14),
                                     command = lambda: self.button_clicked(self.b4))
        self.b4.place(x = 170, y = 70)

        # 2 Row
        self.b5 = customtkinter.CTkButton(self.app, text = '6', width = 40, height = 40, text_font = ('Consolas', 14),
                                     command = lambda: self.button_clicked(self.b5))
        self.b5.place(x = 20, y = 120)

        self.b6 = customtkinter.CTkButton(self.app, text = '5', width = 40, height = 40, text_font = ('Consolas', 14),
                                     command = lambda: self.button_clicked(self.b6))
        self.b6.place(x = 70, y = 120)

        self.b7 = customtkinter.CTkButton(self.app, text = '4', width = 40, height = 40, text_font = ('Consolas', 14),
                                     command = lambda: self.button_clicked(self.b7))
        self.b7.place(x = 120, y = 120)

        self.b8 = customtkinter.CTkButton(self.app, text = '+', width = 40, height = 40, text_font = ('Consolas', 14),
                                     command = lambda: self.button_clicked(self.b8))
        self.b8.place(x = 170, y = 120)

        # 3 Row
        self.b9 = customtkinter.CTkButton(self.app, text = '3', width = 40, height = 40, text_font = ('Consolas', 14),
                                     command = lambda: self.button_clicked(self.b9))
        self.b9.place(x = 20, y = 170)

        self.b10 = customtkinter.CTkButton(self.app, text = '2', width = 40, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b10))
        self.b10.place(x = 70, y = 170)

        self.b11 = customtkinter.CTkButton(self.app, text = '1', width = 40, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b11))
        self.b11.place(x = 120, y = 170)

        self.b12 = customtkinter.CTkButton(self.app, text = '-', width = 40, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b12))
        self.b12.place(x = 170, y = 170)

        # 4 Row
        self.b13 = customtkinter.CTkButton(self.app, text = '.', width = 40, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b13))
        self.b13.place(x = 20, y = 220)

        self.b14 = customtkinter.CTkButton(self.app, text = '0', width = 40, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b14))
        self.b14.place(x = 70, y = 220)

        self.b15 = customtkinter.CTkButton(self.app, text = '%', width = 40, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b15))
        self.b15.place(x = 120, y = 220)

        self.b16 = customtkinter.CTkButton(self.app, text = '*', width = 40, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b16))
        self.b16.place(x = 170, y = 220)

        # 5 Row
        self.b17 = customtkinter.CTkButton(self.app, text = '=', width = 140, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b17))
        self.b17.place(x = 20, y = 270)

        self.b18 = customtkinter.CTkButton(self.app, text = '/', width = 40, height = 40, text_font = ('Consolas', 14),
                                      command = lambda: self.button_clicked(self.b18))
        self.b18.place(x = 170, y = 270)

        # Theme
        self.optionmenu = customtkinter.CTkOptionMenu(values = ["Light", "Dark", "System"], width = 90,
                                                 command = self.change_theme)
        self.optionmenu.place(x = 70, y = 320)
        self.optionmenu.set("Dark")

    # Button Press
    def button_clicked(self, button):
        text = button.text
        if text == "=":
            if self.scvalue.get().isdigit():
                value = int(self.scvalue.get())
            else:
                try:
                    value = eval(self.expression.get())
                except Exception as e:
                    value = "Error"

            self.scvalue.set(value)
            self.expression.update()
        elif text == "C":
            self.scvalue.set("")
            self.expression.update()
        else:
            self.scvalue.set(self.scvalue.get() + text)
            self.expression.update()

    # Themes
    def change_theme(self, theme):
        customtkinter.set_appearance_mode(theme)

    # Tkinter Loop
    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()