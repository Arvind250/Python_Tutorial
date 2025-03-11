def kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
kwargs(name = "Alice",age=21)
kwargs(name="new")
kwargs(msg="hello")