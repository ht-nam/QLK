from tkinter import *
import os
from src import menu, MyException


class TopLevel5:
    def __init__(self, master):
        self.__master = master
        self.__tl = Toplevel(master)
        self.__TlConfig()

    def __TlConfig(self):
        icon = PhotoImage(file=os.getcwd() + r"\resource\remove.png")

        if len(menu.dsKho) == 0:
            self.__tl.geometry("500x50")
            Label(
                self.__tl,
                text="Danh sách kho hàng rỗng",
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()
        else:
            self.__tl.geometry("400x200")
            self.__tl.title("Xóa sản phẩm")
            lb = Label(self.__tl, image=icon)
            lb.image = icon
            lb.place(x=10, y=30)

            Label(
                self.__tl, text="Nhập tên sản phẩm cần xóa:", font=("Aria", 13, "bold")
            ).place(x=150, y=40)

            self.__etr = Entry(self.__tl, width=17, font=("Aria", 15), justify=RIGHT)
            self.__etr.place(x=168, y=80)

            Button(
                self.__tl,
                text="Submit",
                fg="Green",
                font=("Arial", 12),
                command=self.__get,
            ).place(x=170, y=130)
            Button(
                self.__tl,
                text="Cancel",
                fg="Red",
                font=("Arial", 12),
                command=self.__tl.destroy,
            ).place(x=290, y=130)

    def __get(self):
        try:
            name = self.__etr.get()
            MyException.checkName(name)
            lstname = [i.getName() for i in menu.dsKho]
            tl1 = Toplevel(self.__tl)
            tl1.title("Xóa sản phẩm")
            if len(menu.dsKho) == 0:
                tl1.geometry("500x50")
                Label(
                    tl1,
                    text="Danh sách kho hàng rỗng",
                    fg="Red",
                    font=("Arial", 20, "bold"),
                ).pack()
            elif name not in lstname:
                tl1.geometry("500x50")
                Label(
                    tl1,
                    text="Không có sản phẩm trong danh sách",
                    fg="Red",
                    font=("Arial", 20, "bold"),
                ).pack()
            else:
                lst = [i for i in menu.dsKho if i.getName() == name]
                menu.dsKho.remove(lst[0])
                Label(
                    tl1,
                    text="Xóa sản phẩm thành công",
                    fg="Red",
                    font=("Arial", 20, "bold"),
                ).pack()
            tl1.mainloop()
        except MyException.NameException as e:
            e.warning(self.__tl)
        except:
            tl = Toplevel(self.__tl)
            tl.geometry("500x50")
            tl.resizable(width=False, height=False)
            Label(
                tl,
                text="Lỗi không xác định, hãy note lại",
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()
            tl.mainloop()

    def resizable(self, width=True, height=True):
        self.__tl.resizable(width, height)

    def mainloop(self):
        self.__tl.mainloop()


"""TEST

def click():
    tl = TopLevel5(a)
    tl.mainloop()


a = Tk()
Button(text="Click", command=click).pack()
a.mainloop()
"""
