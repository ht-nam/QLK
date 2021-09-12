from tkinter import *
from src import menu, MyException
import os


class TopLevel2:
    def __init__(self, master):
        self.__tl = Toplevel(master)
        self.__TlConfig()

    def __TlConfig(self):
        icon = PhotoImage(file=os.getcwd() + r"\resource\search.png").subsample(
            x=4, y=4
        )
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
            self.__tl.title("Tìm kiếm sản phẩm")
            lb = Label(self.__tl, image=icon)
            lb.image = icon
            lb.place(x=10, y=30)

            Label(
                self.__tl, text="Nhập tên sản phẩm cần tìm:", font=("Aria", 13, "bold")
            ).place(x=150, y=40)

            self.__etr = Entry(self.__tl, width=17, font=("Aria", 15), justify=RIGHT)
            self.__etr.place(x=168, y=80)

            Button(
                self.__tl,
                text="Submit",
                fg="Green",
                font=("Arial", 12),
                command=self.__get,
            ).place(
                x=170,
                y=130,
            )
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
            pos = -1
            for i, j in enumerate(menu.dsKho):
                if name == j.getName():
                    pos = i

            tl1 = Toplevel(self.__tl)
            tl1.title("Tìm kiếm sản phẩm")
            if pos == -1:
                tl1.geometry("500x50")
                Label(
                    tl1,
                    text="Không có sản phẩm trong danh sách",
                    fg="Red",
                    font=("Arial", 20, "bold"),
                ).pack()
            else:
                tl1.geometry("1000x200")
                frame = Frame(tl1)
                Label(frame, text="Tìm kiếm sản phẩm", font=("Arial", 20, "bold")).grid(
                    row=0, column=0, columnspan=6, pady=20
                )
                self.__table(frame)
                Label(frame, text="STT", font=("Arial", 10, "bold")).grid(
                    row=1, column=0
                )
                Label(frame, text="Tên sản phẩm", font=("Arial", 10, "bold")).grid(
                    row=1, column=1
                )
                Label(frame, text="Đơn giá", font=("Arial", 10, "bold")).grid(
                    row=1, column=2
                )
                Label(frame, text="Số lượng", font=("Arial", 10, "bold")).grid(
                    row=1, column=3
                )
                Label(frame, text="Tổng cộng", font=("Arial", 10, "bold")).grid(
                    row=1, column=4
                )
                Label(frame, text="Hạn sử dụng", font=("Arial", 10, "bold")).grid(
                    row=1, column=5
                )
                # Display Product
                Label(frame, text=str(pos + 1), font=("Arial", 10)).grid(
                    row=2, column=0
                )
                Label(frame, text=menu.dsKho[pos].getName(), font=("Arial", 10)).grid(
                    row=2, column=1
                )
                Label(frame, text=menu.dsKho[pos].getPrice(), font=("Arial", 10)).grid(
                    row=2, column=2
                )
                Label(
                    frame, text=menu.dsKho[pos].getQuantity(), font=("Arial", 10)
                ).grid(row=2, column=3)
                Label(
                    frame,
                    text=menu.dsKho[pos].getTotalPrice(),
                    font=("Arial", 10),
                ).grid(row=2, column=4)
                Label(
                    frame,
                    text=menu.dsKho[pos].getExpDate(),
                    font=("Arial", 10),
                ).grid(row=2, column=5)
                frame.pack()
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

    def __table(self, frame):
        for q in range(2):
            Label(
                frame,
                width=12,
                height=2,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=0)
            Label(
                frame,
                width=15,
                height=2,
                padx=100,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=1)
            Label(
                frame,
                width=5,
                height=2,
                padx=40,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=2)
            Label(
                frame,
                width=5,
                height=2,
                padx=40,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=3)
            Label(
                frame,
                width=5,
                height=2,
                padx=40,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=4)
            Label(
                frame,
                width=5,
                height=2,
                padx=40,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=5)

    def resizable(self, width=True, height=True):
        self.__tl.resizable(width, height)

    def mainloop(self):
        self.__tl.mainloop()


"""TEST


def open():
    b = TopLevel2(a)
    b.mainloop()


a = Tk()
Button(text="click", command=open).pack()
a.mainloop()
"""
