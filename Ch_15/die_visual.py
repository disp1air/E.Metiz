from die import Die
import pygal

die = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []

for x in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов
frequencies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')