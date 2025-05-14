def hello(firstname='John', lastname='Doe'):
    if not isinstance(firstname, str): 
        raise TypeError("Le prénom doit être une chaîne")
    
    if not isinstance(lastname, str): 
        raise TypeError("Le nom doit être une chaîne")

    if firstname is None:
        raise TypeError("Il manque le prénom")

    if lastname is None:
        raise TypeError("Il manque le nom de famille")

    return f"Hello, {firstname} {lastname}!"

