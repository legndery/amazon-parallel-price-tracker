from win10toast import ToastNotifier
class NotificationManager:
    def __init__(self) -> None:
        pass
    @staticmethod
    def FirePriceNotification(lastProduct, currentProduct):
        try:
            old_price = float(lastProduct["price"])
            new_price = float(currentProduct["price"])
            if old_price > new_price:
                ToastNotifier().show_toast("Amazon Price Alert", f"{currentProduct['title']}\nPRICE DECREASED", duration=5, threaded=True)
                print("PRICE DECREASED!!!!!!!")
            elif old_price < new_price:
                ToastNotifier().show_toast("Amazon Price Alert", f"{currentProduct['title']}\nPRICE INCREASED", duration=5, threaded=True)
                print("PRICE INCREASED!!!!!!!")
        except Exception as e:
            pass
