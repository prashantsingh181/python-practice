def mini_inventory(items):
    expensive_item = items[0]
    total = 0
    oos = []
    for item in items:
        total += item["price"] * item["quantity"]
        if item["price"] > expensive_item["price"]:
            expensive_item = item
        if item["quantity"] <= 0:
            oos.append(item)
    return {"expensive_item": expensive_item, "total": total, "oos": oos}


print(
    mini_inventory(
        [
            {"name": "Shampoo", "price": 100, "quantity": 20},
            {"name": "PS5", "price": 200, "quantity": 0},
            {"name": "Carrot", "price": 1, "quantity": 10},
        ]
    )
)
