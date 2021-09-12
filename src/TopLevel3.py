from tkinter import *
import os, time
from src import menu, MyException
from src.Date import Date
from src.QLK import QLK


class TopLevel3:
    def __init__(self, master):
        self.__master = master
        self.__tl = Toplevel(master)
        if len(menu.dsKho) > 0:
            self.__TlConfig()
        else:
            self.__tl.geometry("500x50")
            Label(
                self.__tl,
                text="Danh sách kho hàng rỗng",
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()

    def __TlConfig(self):
        self.__tl.geometry("500x290")
        self.__tl.title("Sửa thông tin")
        icon = PhotoImage(file=os.getcwd() + r"\resource\setting.png").subsample(3, 3)
        icon_label = Label(self.__tl, image=icon)
        icon_label.image = icon
        icon_label.place(x=10, y=60)

        Label(
            self.__tl, text="Nhập tên mặt hàng cần sửa:", font=("Arial", 12, "bold")
        ).place(x=230, y=90)

        self.__etr = Entry(self.__tl, width=20, font=("Arial", 15), justify=RIGHT)
        self.__etr.place(x=228, y=120)

        Button(
            self.__tl, text="Submit", fg="Green", font=("Arial", 12), command=self.__get
        ).place(x=250, y=160)
        Button(
            self.__tl,
            text="Cancel",
            fg="Red",
            font=("Arial", 12),
            command=self.__tl.destroy,
        ).place(x=360, y=160)

    def __get(self):
        try:
            name = self.__etr.get()
            MyException.checkName(name)
            lstname = [i.getName() for i in menu.dsKho]
            self.__tl1 = Toplevel(self.__tl)
            if name not in lstname:
                Label(
                    self.__tl1,
                    text="Không có sản phẩm trong danh sách",
                    fg="Red",
                    font=("Arial", 20, "bold"),
                ).pack()
            else:
                self.__tl1.geometry("1000x400")
                self.__tl1.title("Sửa thông tin")
                self.__tl1.resizable(width=False, height=False)
                Label(
                    self.__tl1,
                    text="Thông tin sản phẩm cần sửa",
                    font=("Arial", 20, "bold"),
                ).pack(pady=5)
                self.__product(lstname.index(name))
                self.__change(lstname.index(name))
            self.__tl1.mainloop()
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

    def __product(self, pos):
        frame = Frame(self.__tl1)
        self.__table(frame)
        Label(frame, text="STT", font=("Arial", 12, "bold")).grid(row=0, column=0)
        Label(frame, text="Tên sản phẩm", font=("Arial", 12, "bold")).grid(
            row=0, column=1
        )
        Label(frame, text="Đơn giá", font=("Arial", 12, "bold")).grid(row=0, column=2)
        Label(frame, text="Số lượng", font=("Arial", 12, "bold")).grid(row=0, column=3)
        Label(frame, text="Tổng cộng", font=("Arial", 12, "bold")).grid(row=0, column=4)
        Label(frame, text="Hạn sử dụng", font=("Arial", 12, "bold")).grid(
            row=0, column=5
        )

        Label(frame, text=pos + 1, font=("Arial", 10, "bold")).grid(row=1, column=0)
        Label(frame, text=menu.dsKho[pos].getName(), font=("Arial", 10)).grid(
            row=1, column=1
        )
        Label(frame, text=menu.dsKho[pos].getPrice(), font=("Arial", 10)).grid(
            row=1, column=2
        )
        Label(frame, text=menu.dsKho[pos].getQuantity(), font=("Arial", 10)).grid(
            row=1, column=3
        )
        Label(frame, text=menu.dsKho[pos].getTotalPrice(), font=("Arial", 10)).grid(
            row=1, column=4
        )
        Label(frame, text=menu.dsKho[pos].getExpDate(), font=("Arial", 10)).grid(
            row=1, column=5
        )

        frame.pack(pady=5)

    def __table(self, frame):
        for q in range(2):
            Label(
                frame,
                width=12,
                height=2,
                relief="solid",
                borderwidth=1,
            ).grid(row=q, column=0)
            Label(
                frame,
                width=15,
                height=2,
                padx=100,
                relief="solid",
                borderwidth=1,
            ).grid(row=q, column=1)
            Label(
                frame,
                width=5,
                height=2,
                padx=40,
                relief="solid",
                borderwidth=1,
            ).grid(row=q, column=2)
            Label(
                frame,
                width=5,
                height=2,
                padx=40,
                relief="solid",
                borderwidth=1,
            ).grid(row=q, column=3)
            Label(
                frame,
                width=5,
                height=2,
                padx=40,
                relief="solid",
                borderwidth=1,
            ).grid(row=q, column=4)
            Label(
                frame,
                width=5,
                height=2,
                padx=40,
                relief="solid",
                borderwidth=1,
            ).grid(row=q, column=5)

    def __change(self, pos):
        frame1 = Frame(self.__tl1)
        self.__pos = pos
        Button(
            frame1,
            text="Sửa tên sản phẩm",
            width=20,
            bg="Yellow",
            font=("Arial", 12, "bold"),
            command=self.__changeName,
        ).grid(row=0, column=0, padx=20, pady=10)
        Button(
            frame1,
            text="Sửa đơn giá",
            width=20,
            bg="Yellow",
            font=("Arial", 12, "bold"),
            command=self.__changePrice,
        ).grid(row=0, column=1, padx=20, pady=10)
        Button(
            frame1,
            text="Sửa số lượng",
            width=20,
            bg="Yellow",
            font=("Arial", 12, "bold"),
            command=self.__changeQuantity,
        ).grid(row=1, column=0, padx=20, pady=10)
        Button(
            frame1,
            text="Sửa hạn sử dụng",
            width=20,
            bg="Yellow",
            font=("Arial", 12, "bold"),
            command=self.__changeDate,
        ).grid(row=1, column=1, padx=20, pady=10)
        frame1.pack(pady=30)

    def __changeName(self):
        Label(self.__tl1, width=60, height=40).place(x=300, y=295)
        Label(self.__tl1, text="Tên sản phẩm:", font=("Arial", 12, "bold")).place(
            x=300, y=300
        )
        self.__entry2 = Entry(self.__tl1, font=("Arial", 15), width=17, justify=RIGHT)
        self.__entry2.place(x=424, y=300)
        Button(
            self.__tl1,
            text="Submit",
            fg="Green",
            font=("bold"),
            command=self.__setName,
        ).place(x=625, y=297)

    def __changePrice(self):
        Label(self.__tl1, width=60, height=40).place(x=300, y=295)
        Label(self.__tl1, text="Giá sản phẩm:", font=("Arial", 12, "bold")).place(
            x=300, y=300
        )
        self.__entry2 = Entry(self.__tl1, font=("Arial", 15), width=17, justify=RIGHT)
        self.__entry2.place(x=424, y=300)
        Button(
            self.__tl1,
            text="Submit",
            fg="Green",
            font=("bold"),
            command=self.__setPrice,
        ).place(x=625, y=297)

    def __changeQuantity(self):
        Label(self.__tl1, width=60, height=40).place(x=300, y=295)
        Label(self.__tl1, text="Số lượng:", font=("Arial", 12, "bold")).place(
            x=390, y=300
        )
        self.__entry2 = Entry(self.__tl1, font=("Arial", 15), width=5, justify=RIGHT)
        self.__entry2.place(x=477, y=300)
        Button(
            self.__tl1,
            text="Submit",
            fg="Green",
            font=("bold"),
            command=self.__setQuantity,
        ).place(x=545, y=297)

    def __changeDate(self):
        Label(self.__tl1, width=60, height=40).place(x=300, y=295)
        Label(self.__tl1, text="Hạn sử dụng:", font=("Arial", 12, "bold")).place(
            x=310, y=300
        )
        self.__entry2a = Entry(self.__tl1, font=("Arial", 15), width=5, justify=RIGHT)
        self.__entry2a.place(x=425, y=300)
        self.__entry2b = Entry(self.__tl1, font=("Arial", 15), width=5, justify=RIGHT)
        self.__entry2b.place(x=490, y=300)
        self.__entry2c = Entry(self.__tl1, font=("Arial", 15), width=5, justify=RIGHT)
        self.__entry2c.place(x=555, y=300)
        Button(
            self.__tl1,
            text="Submit",
            fg="Green",
            font=("bold"),
            command=self.__setDate,
        ).place(x=620, y=297)

    def __setName(self):
        name = self.__entry2.get()
        menu.dsKho[self.__pos].setName(name)
        self.__Tl1Refresh()

    def __setPrice(self):
        price = self.__entry2.get()
        menu.dsKho[self.__pos].setPrice(price)
        self.__Tl1Refresh()

    def __setQuantity(self):
        qtt = self.__entry2.get()
        menu.dsKho[self.__pos].setQuantity(qtt)
        self.__Tl1Refresh()

    def __setDate(self):
        day = self.__entry2a.get()
        month = self.__entry2b.get()
        year = self.__entry2b.get()
        menu.dsKho[self.__pos].setExpDate(day, month, year)
        self.__Tl1Refresh()

    def __Tl1Refresh(self):
        self.__tl1.destroy()
        self.__get()

    def resizable(self, width=True, height=True):
        self.__tl.resizable(width, height)

    def mainloop(self):
        self.__tl.mainloop()


"""TEST
def cl():
    tl = TopLevel3(a)
    tl.resizable(width=False, height=False)
    tl.mainloop()


menu.dsKho.append(QLK("a", 1, 1, Date(1, 1, 1)))
a = Tk()
Button(a, text="Click", command=cl).pack()
a.mainloop()
"""
