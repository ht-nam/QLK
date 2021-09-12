from src import QLK
from src.Date import Date


def Add(lst):
    if len(lst) == 6:
        name, quantity, price, day, month, year = lst
        if (
            name != ""
            and quantity != ""
            and price != ""
            and day != ""
            and month != ""
            and year != ""
        ):
            dsKho.append(
                QLK.QLK(
                    name,
                    int(quantity),
                    int(price),
                    Date(int(day), int(month), int(year)),
                )
            )


def Display():
    for i in dsKho:
        print(i.__str__())


dsKho = []
