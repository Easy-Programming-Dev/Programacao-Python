from datetime import date

data = date.today()

data_form = data.strftime('%d/%m/%Y')
print(data_form)