import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def my_function(x):
    return 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

# Генерація значень x в діапазоні від 0 до 5
x_values = np.linspace(0.01, 5, 500)  # Щоб уникнути ділення на 0, додано 0.01

# Обчислення відповідних значень y
y_values = my_function(x_values)

# Побудова графіка
plt.figure(figsize=(8, 6))

# Побудова графіка функції
plt.plot(x_values, y_values, label=r'$Y(x)=\frac{5 \cos(10x) \sin(3x)}{\sqrt{x}}$',
         color='b', linewidth=2)

# Додавання осей та назв
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Графік функції Y(x)')
plt.xlabel('x')
plt.ylabel('Y')

# Встановлення легенди
plt.legend()

# Показ графіка
plt.grid(True)
plt.show()
