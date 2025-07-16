from functools import partial
def calculate_price(price,discount):
    return price-(price*discount/100)
student_discount= partial(calculate_price,discount=10)
senior_discount= partial(calculate_price,discount=20)
price=float((input()))
print("enter price :",price)
print(f"student pays :{student_discount(price)}")
print(f"senior pays :{senior_discount(price)}")