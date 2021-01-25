temperature = 30
hummidity = 70
uv_index = 10
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's a cold day")
if hummidity > 50:
    print("It's a humid day")
else:
    print("It's not a humid day")
if uv_index <= 7:
    print("It's safe to go out")
elif uv_index <= 10:
    print("It's not safe to go out")
else:
    print("Do not go out")
