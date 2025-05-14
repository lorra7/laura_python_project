def hello(firstname='John', lastname='Doe'):
    if not firstname:
        raise TypeError("Il manque le prénom")
    if not lastname:
        raise TypeError("Il manque le nom de famille")

    if not isinstance(firstname, str):
        raise TypeError("Le nom doit être une chaîne")

    if not isinstance(lastname, str):
        raise TypeError("Le nom doit être une chaîne")

    return f"Hello, {firstname} {lastname}!"
