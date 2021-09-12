from tkinter import *
from src import menu


class TopLevel4:
    def __init__(self, master):
        self.__tl = Toplevel(master)
        self.__TlConfig()

    def __TlConfig(self):
        self.__tl.title("Hiển thị kho")
        frame = Frame(self.__tl)

        if len(menu.dsKho) > 0:
            self.__tl.geometry("1000x{}".format(100 + 40 * len(menu.dsKho)))
            self.__Display(frame)
        else:
            self.__tl.geometry("500x50")
            Label(
                frame,
                text="Danh sách kho hàng rỗng",
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()

        frame.pack()

    def __Display(self, frame):
        Label(frame, text="Danh sách kho hàng", font=("Arial", 20, "bold")).grid(
            row=0, column=0, columnspan=6, pady=20
        )
        self.__table(frame)
        Label(frame, text="STT", font=("Arial", 10, "bold")).grid(row=1, column=0)
        Label(frame, text="Tên sản phẩm", font=("Arial", 10, "bold")).grid(
            row=1, column=1
        )
        Label(frame, text="Đơn giá", font=("Arial", 10, "bold")).grid(row=1, column=2)
        Label(frame, text="Số lượng", font=("Arial", 10, "bold")).grid(row=1, column=3)
        Label(frame, text="Tổng cộng", font=("Arial", 10, "bold")).grid(row=1, column=4)
        Label(frame, text="Hạn sử dụng", font=("Arial", 10, "bold")).grid(
            row=1, column=5
        )
        self.__DisplayPrd(frame)

    def __DisplayPrd(self, frame):
        q = 0
        for i in menu.dsKho:
            q += 1
            Label(frame, text=str(q), font=("Arial", 10)).grid(row=q + 1, column=0)
            Label(frame, text=i.getName(), font=("Arial", 10)).grid(row=q + 1, column=1)
            Label(frame, text=i.getPrice(), font=("Arial", 10)).grid(
                row=q + 1, column=2
            )
            Label(frame, text=i.getQuantity(), font=("Arial", 10)).grid(
                row=q + 1, column=3
            )
            Label(
                frame,
                text=i.getTotalPrice(),
                font=("Arial", 10),
            ).grid(row=q + 1, column=4)
            Label(
                frame,
                text=i.getExpDate(),
                font=("Arial", 10),
            ).grid(row=q + 1, column=5)

    def __table(self, frame):
        for q in range(len(menu.dsKho) + 1):
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

    def mainloop(self):
        self.__tl.mainloop()

    def resizable(self, width=True, height=True):
        self.__tl.resizable(width, height)


""" Test
def open():
    tl = TopLevel4(a)
    tl.resizable(width=False, height=False)
    tl.mainloop()


a = Tk()
Button(a, text="Click", command=open).pack()
a.mainloop()
"""
