from tkinter import *
import os
from src import menu
from src import TopLevel1, TopLevel2, TopLevel3, TopLevel4, TopLevel5


class MyGUI:
    def __init__(self, master):
        self.__master = master
        self.__masterConfig(master)

        self.__frame = Frame(master)
        self.__setFrame()
        self.__frame.pack()

    def __masterConfig(self, master):
        path = os.getcwd() + r"\resource\icon.png"
        icon = PhotoImage(file=path)
        master.iconphoto(True, icon)
        master.title("QLK")
        master.geometry("1000x500")

    def __setFrame(self):
        label1 = Label(
            self.__frame, text=" Quản lý kho", font=("Arial", 30, "bold"), pady=50
        )
        label1.grid(row=0, column=0, columnspan=2, pady=(20, 20))

        button1 = Button(
            self.__frame,
            text="Thêm sản phẩm",
            font=("Aria", 20),
            padx=36,
            command=self.__button1,
        )
        button1.grid(row=1, column=0, padx=70, pady=10)

        button2 = Button(
            self.__frame,
            text="Tìm sản phẩm",
            font=("Aria", 20),
            padx=47,
            command=self.__button2,
        )
        button2.grid(row=1, column=1, padx=70, pady=10)

        button3 = Button(
            self.__frame,
            text=" Sửa thông tin ",
            font=("Aria", 20),
            padx=44,
            command=self.__button3,
        )
        button3.grid(row=2, column=0, padx=70)

        button4 = Button(
            self.__frame,
            text="Hiển thị kho",
            font=("Aria", 20),
            padx=61,
            command=self.__button4,
        )
        button4.grid(row=2, column=1, padx=70)

        button5 = Button(
            self.__frame,
            text="Xóa sản phẩm",
            font=("Aria", 20),
            padx=47,
            command=self.__button5,
        )
        button5.grid(row=3, column=0, padx=70)

        quit_button = Button(
            self.__frame,
            text="Kết thúc chương trình",
            font=("Aria", 20),
            command=self.__quit,
        )
        quit_button.grid(row=3, column=1, padx=70, pady=10)

    def __button1(self):
        tk = TopLevel1.TopLevel1(self.__master)
        tk.resizable(width=False, height=False)
        tk.mainloop()
        menu.Add(tk.getInfo())

    def __button2(self):
        tk = TopLevel2.TopLevel2(self.__master)
        tk.resizable(width=False, height=False)
        tk.mainloop()

    def __button3(self):
        tk = TopLevel3.TopLevel3(self.__master)
        tk.resizable(width=False, height=False)
        tk.mainloop()

    def __button4(self):
        tk = TopLevel4.TopLevel4(self.__master)
        tk.resizable(width=False, height=False)
        tk.mainloop()

    def __button5(self):
        tk = TopLevel5.TopLevel5(self.__master)
        tk.resizable(width=False, height=False)
        tk.mainloop()

    def __quit(self):
        p = Toplevel(self.__master)
        p.geometry("200x50")
        Label(p, text="Bạn muốn kết thúc chương trình?", font=("Aria", 10)).grid(
            row=0, column=0, columnspan=2
        )
        Button(
            p,
            text="Kết thúc",
            font=("Aria", 10),
            fg="Red",
            command=self.__master.destroy,
        ).grid(row=1, column=0)
        Button(p, text="Hủy", font=("Aria", 10), padx=15, command=p.destroy).grid(
            row=1, column=1
        )
        p.mainloop()


root = Tk()
myGui = MyGUI(root)
root.resizable(width=False, height=False)
root.mainloop()
