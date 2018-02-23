import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=16)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of Value", fontsize=12)

# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()