import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.plot(input_values, squares, linewidth=3)

# Назначение заголовка диаграммы и меток осей
plt.title("Square Numbers", fontsize=16)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=12)

# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', labelsize=10)

plt.show()