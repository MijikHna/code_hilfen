from datetime import datetime


def getDateTime():
    currentDate = datetime.now()
    currentDateStr = currentDate.strftime('%d.%m.%Y - %H:%M:%S')
    return currentDateStr

# weiter Funktionen
def getStatus():
    status = True
    currentDate = getDateTime()
    return {"date": currentDate, "status": status}