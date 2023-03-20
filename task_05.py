from datetime import datetime, timedelta
def date_in_future(integer):
    if isinstance(integer, int):
        return f"{(datetime.now() + timedelta(days=integer)).strftime('%d-%m-%Y %H:%M:%S')}"
    else:
        return f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"