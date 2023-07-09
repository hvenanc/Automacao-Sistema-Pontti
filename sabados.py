from datetime import datetime, timedelta,date

def get_saturdays(year = datetime.today().year, month= datetime.today().month):
    # Primeiro dia do mês
    start_date = datetime(year, month, 1)
    
    # Último dia do mês
    if month == 12:
        end_date = datetime(year + 1, 1, 1)
    else:
        end_date = datetime(year, month + 1, 1)
    
    # Encontrar o primeiro sábado
    current_date = start_date + timedelta(days=(5 - start_date.weekday() + 7) % 7)
    
    # Iterar sobre os sábados até o final do mês
    saturdays = []
    while current_date < end_date:
        saturdays.append(current_date.strftime("%d/%m/%Y"))
        current_date += timedelta(days=7)
        
    return saturdays