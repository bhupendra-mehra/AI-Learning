def discount(rate):

    def calculate(price):
        return price - (price * rate)

    return calculate


ten_percent = discount(0.10)

print(ten_percent(1000))