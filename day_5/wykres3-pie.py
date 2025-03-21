import matplotlib.pyplot as plt

labels = ["Jabłko", "Banany", "Winogrona", 'Pomarańćze']
sizes = [30, 25, 20, 45]
colors = ['red', 'blue', 'purple', 'yellow']

plt.pie(sizes, labels=labels, colors=colors,startangle=90, shadow=True, explode=(0.1, 0, 0, 0),
autopct = '%1.1f%%')

plt.title("Wykres kołowy")
plt.axis('equal')
plt.show()
