customer = {
    "name": "Ray Hsiao",
    "age": 29,
    "is verified": True
}
customer["name"] = "Raymond Hsiao"
customer["birthdate"] = "Nov 20 1991"
print(customer["name"])
print(customer.get("birthdate", "Jan 1 1991"))