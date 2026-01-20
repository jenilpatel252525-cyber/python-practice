def pk(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:is{value}")

pk(name="jenil",hobby="coding")