name = "Raymond Hsiao"
age = 19
if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")
if age < 18:
    print("Too young for this")
elif age > 40:
    print("Too olf for this")
else:
    print("Perfect age")