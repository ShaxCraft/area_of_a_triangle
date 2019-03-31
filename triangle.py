# Данные о треугольниках
# Triangle data
ErrorInput = 'Insert the number!\n\n'
try:
    A = float(input('Enter the length of side A:\n'))  # Введите длинну стороны А
    B = float(input('Enter the length of side B:\n'))  # Введите длинну стороны B
    C = float(input('Enter the length of side C:\n'))  # Введите длинну стороны C
except:
    print(ErrorInput)
