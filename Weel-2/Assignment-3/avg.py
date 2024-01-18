
def avg(data):
    all_products = data["products"]

    total = 0
    for item in all_products:
        total += item["price"]

    return round(total/len(all_products), 3)


print(avg({
    "products": [
        {
            "name": "Product 1",
            "price": 100},
        {
            "name": "Product 2",
            "price": 700
        },
        {
            "name": "Product 3",
            "price": 300
        }
    ]
})
)
