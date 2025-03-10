#Funtion to greet the user and if no name provided then use default value
def greet(name="Guest"):
    msg = "Hello "+name
    return msg
print(greet(""))