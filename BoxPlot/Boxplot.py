# Boxplot - Box Diagram

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(100):
    random_number = random.randint(0,1000)
    vetor.append(random_number)

plt.boxplot(vetor)
plt.show()
plt.savefig("BoxDiagram", dpi=300)