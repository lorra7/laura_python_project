def hello(firstname='John', lastname='Doe'):
    if not isinstance(firstname, str, lastname, str):
        raise TypeError("Le nom doit être une chaîne")    
    return f"Hello, firstname lastname !"
