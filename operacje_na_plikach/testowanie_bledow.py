def show_temp_status(temp: float) -> str:
    try:
        if 36.4 <= temp <= 36.8:
            return "ok"
        else:
            return "NOT OK"
    except TypeError:
        return "ERROR"

assert show_temp_status(36.6) == "OK"
#print(show_temp_status(36.4))
