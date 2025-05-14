def hello(firstname=None, lastname=None):
    if firstname is None and lastname is None:
        return "Hello, GitHub Actions!"
    

    if firstname is not None and lastname is None:
        if not isinstance(firstname, str):
            raise TypeError("Le nom doit être une chaîne")
    
    if not isinstance(firstname, str):
        raise TypeError("Le nom doit être une chaîne")
    
    if not isinstance(lastname, str):
        raise TypeError("Le nom doit être une chaîne")
    

    return f"Hello, {firstname} {lastname}!"

