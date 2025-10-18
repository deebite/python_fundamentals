# def calculate_bill(*products, **details):
#     products_sum = sum(products)

#     for key , val in details.items():
#         if key == "discount":
#             products_sum -= (products_sum * (val/100))
#             continue
#         elif key == "tax":
#             products_sum += (products_sum * (val/100))
#             continue

#         print(f"Bill for this customer: {val} is {products_sum}")


def calculate_bill(*products, **details):
    total = sum(products)
    discount = details.get("discount", 0)
    tax = details.get("tax", 0)
    name = details.get("customer", "Guest")

    total -= (total * (discount/100))
    total += (total * (tax/100))

    print(f"Bill for this customer: {name} is {total} Rs")

calculate_bill(100, 200, 300, discount=10, tax=5, customer="Amardeep")
