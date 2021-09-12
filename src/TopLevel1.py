from tkinter import *
from src import MyException


class TopLevel1:
    def __init__(self, master):
        self.__tl = Toplevel(master)
        self.__lst = []
        self.__TlConfig()

    def __TlConfig(self):
        self.__tl.geometry("400x230")
        self.__tl.title("Thêm sản phẩm")
        frame = Frame(self.__tl)

        Label(frame, text="Thêm sản phẩm", font=("Arial", 20, "bold"), anchor=W).grid(
            row=0, column=0, columnspan=4, pady=20
        )

        Label(frame, text="Tên sản phẩm:", font=("Arial", 10), width=25, anchor=W).grid(
            row=1, column=0
        )
        entry1 = Entry(frame, font=("Arial", 10), width=21, justify=RIGHT)
        entry1.grid(row=1, column=1, columnspan=3)

        Label(frame, text="Số lượng:", font=("Arial", 10), width=25, anchor=W).grid(
            row=2, column=0
        )
        entry2 = Entry(frame, font=("Arial", 10), width=21, justify=RIGHT)
        entry2.grid(row=2, column=1, columnspan=3)

        Label(
            frame, text="Giá mỗi sản phẩm:", font=("Arial", 10), width=25, anchor=W
        ).grid(row=3, column=0)
        entry3 = Entry(frame, font=("Arial", 10), width=21, justify=RIGHT)
        entry3.grid(row=3, column=1, columnspan=3)

        Label(frame, text="Hạn sử dụng:", font=("Arial", 10), width=25, anchor=W).grid(
            row=4, column=0
        )
        entry4a = Entry(frame, font=("Arial", 10), width=5, justify=RIGHT)
        entry4a.grid(row=4, column=1)
        entry4b = Entry(frame, font=("Arial", 10), width=5, justify=RIGHT)
        entry4b.grid(row=4, column=2)
        entry4c = Entry(frame, font=("Arial", 10), width=7, justify=RIGHT)
        entry4c.grid(row=4, column=3)

        self.__lst = [entry1, entry2, entry3, entry4a, entry4b, entry4c]

        Button(frame, text="Submit", command=self.__submit).grid(
            row=5, column=0, columnspan=2, pady=10
        )
        Button(frame, text="Cancel", command=self.__tl.destroy).grid(
            row=5, column=1, columnspan=2
        )

        frame.pack()

    def __submit(self):
        try:
            self.__lst1 = [i.get() for i in self.__lst]
            MyException.checkName(self.__lst1[0])
            MyException.checkQuantity(self.__lst1[1])
            MyException.checkPrice(self.__lst1[2])
            MyException.checkDate(self.__lst1[3], self.__lst1[4], self.__lst1[5])
        except (
            MyException.NameException,
            MyException.QuantityException,
            MyException.PriceException,
            MyException.DateException,
        ) as e:
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
        finally:
            self.__tl.quit()
            self.__tl.destroy()

    def getInfo(self):
        return self.__lst1

    def resizable(self, width=True, height=True):
        self.__tl.resizable(width, height)

    def mainloop(self):
        self.__tl.mainloop()
