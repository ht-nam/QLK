from src import Date
from tkinter import *


class NameException(Exception):
    def __init__(self, str=""):
        self.__str = str

    def warning(self, master):
        tl = Toplevel(master)
        tl.geometry("500x50")
        tl.resizable(width=False, height=False)
        if len(self.__str) == 0:
            Label(
                tl, text="Tên không được để trống", fg="Red", font=("Arial", 20, "bold")
            ).pack()
        elif len(self.__str) > 40:
            Label(
                tl,
                text="Tên không được dài quá 40 kí tự",
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()
        elif self.__str.isalpha() == 0:
            Label(
                tl,
                text="Tên không được chứa số hoặc kí tự đặc biệt",
                fg="Red",
                font=("Arial", 15, "bold"),
            ).pack(pady=8)
        else:
            Label(
                tl, text="Tên không hợp lệ", fg="Red", font=("Arial", 20, "bold")
            ).pack()
        tl.mainloop()

    def __str__(self):
        return (
            self.__str + " không hợp lệ"
            if len(self.__str) != 0
            else "Tên sản phẩm không được để trống"
        )


class QuantityException(Exception):
    def __init__(self, Qtt):
        self.__Qtt = Qtt

    def warning(self, master):
        tl = Toplevel(master)
        tl.geometry("500x50")
        tl.resizable(width=False, height=False)
        if len(self.__Qtt) == 0:
            Label(
                tl,
                text="Số lượng không được để trống",
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()
        elif not self.__Qtt.isdigit():
            Label(
                tl,
                text="Số lượng không được chứa số hoặc kí tự đặc biệt",
                fg="Red",
                font=("Arial", 15, "bold"),
            ).pack(pady=8)
        else:
            Label(
                tl, text="Số lượng không hợp lệ", fg="Red", font=("Arial", 20, "bold")
            ).pack()
        tl.mainloop()

    def __str__(self):
        return (
            "Số lượng không được để trống"
            if len(self.__Qtt) == 0
            else self.__Qtt + " không phải là số"
            if self.__Qtt.isdigit() == False
            else "Số lượng sản phẩm quá lớn (giới hạn 10000)"
            if int(self.__Qtt) > 10000
            else self.__Qtt + " không hợp lệ"
        )


class PriceException(Exception):
    def __init__(self, Prc):
        self.__Prc = Prc

    def warning(self, master):
        tl = Toplevel(master)
        tl.geometry("500x50")
        tl.resizable(width=False, height=False)
        if len(self.__Prc) == 0:
            Label(
                tl,
                text="ĐƠn giá không được để trống",
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()
        elif not self.__Prc.isdigit():
            Label(
                tl,
                text="Đơn giá không được chứa số hoặc kí tự đặc biệt",
                fg="Red",
                font=("Arial", 15, "bold"),
            ).pack(pady=8)
        else:
            Label(
                tl, text="Đơn giá không hợp lệ", fg="Red", font=("Arial", 20, "bold")
            ).pack()
        tl.mainloop()

    def __str__(self):
        return (
            "Đơn giá không được để trống"
            if len(self.__Prc) == 0
            else self.__Prc + " không phải là số"
            if self.__Prc.isdigit() == False
            else "Đơn giá quá lớn (giới hạn 1000000000)"
            if int(self.__Prc) > 1000000000
            else self.__Prc + " không hợp lệ"
        )


class DateException(Exception):
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def warning(self, master):
        tl = Toplevel(master)
        tl.geometry("500x50")
        tl.resizable(width=False, height=False)
        self.__day = str(self.__day)
        self.__month = str(self.__month)
        self.__year = str(self.__year)
        if len(self.__day) == 0 or len(self.__month) == 0 or len(self.__year) == 0:
            Label(
                tl,
                text="{} không được để trống".format(
                    "Ngày"
                    if len(self.__day) == 0
                    else "Tháng"
                    if len(self.__month) == 0
                    else "Năm"
                ),
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()
        else:
            Label(
                tl,
                text="Hạn sử dụng không hợp lệ",
                fg="Red",
                font=("Arial", 20, "bold"),
            ).pack()
        tl.mainloop()

    def __str__(self):
        return "Ngày không hợp lệ"


def checkName(name):
    if len(name) == 0 or len(name) > 40 or not "".join(name.split()).isalpha():
        raise NameException(name)


def checkQuantity(qtt):
    if len(qtt) == 0 or qtt.isdigit() == False or len(qtt) == 0 or int(qtt) > 10000:
        raise QuantityException(qtt)


def checkPrice(prc):
    if (
        len(prc) == 0
        or prc.isdigit() == False
        or len(prc) == 0
        or int(prc) > 1000000000
    ):
        raise PriceException(prc)


def checkDate(day, month, year):
    if (
        len(day) == 0
        or len(month) == 0
        or len(year) == 0
        or str(day + month + year).isdigit() == False
    ):
        raise DateException(day, month, year)
    year, month, day = int(year), int(month), int(day)
    if year < 2021 or year > 2100 or month < 0 or month > 12 or day < 0:
        raise DateException(day, month, year)
    if (year % 4 and year % 100 != 0) or year % 400:
        if month == 2 and day > 29:
            raise DateException(day, month, year)
    else:
        if month == 2 and day > 28:
            raise DateException(day, month, year)
    if month in {1, 3, 5, 7, 8, 10, 12} and day > 31:
        raise DateException(day, month, year)
    if month in {4, 6, 9, 11} and day() > 30:
        raise DateException(day, month, year)


"""
try:
    checkName("a")
    checkQuantity("1")
    checkPrice("1")
    checkDate("1", "1", "2022")
except (NameException, QuantityException, PriceException, DateException) as e:
    print(e)
"""
