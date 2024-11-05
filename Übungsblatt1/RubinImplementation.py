import math
import numpy as np
import matplotlib.pyplot as plt


def naiveBerechnung(x: float, n: int) -> float:
    sum = 0
    for k in range(0, n):
        sum += (1/math.factorial(k)) * (x**k)
    return sum

def relativerFehler(ytilde: np.ndarray) -> np.ndarray:
    val = np.exp(-5.5)
    absfehler = np.abs(ytilde - val)
    relfehler = np.abs(absfehler/ytilde)
    return relfehler


methode1 = np.zeros(10)
methode2 = np.zeros(10)
methode3 = np.zeros(10)
index = list()

for i in range(0,10):
    index.append((i+1)*3)
    methode1[i] = naiveBerechnung(-5.5, index[i])
    methode2[i] = 1/naiveBerechnung(5.5, index[i])
    methode3[i] = naiveBerechnung(-0.5, index[i])**11

fehler1 = relativerFehler(methode1)
fehler2 = relativerFehler(methode2)
fehler3 = relativerFehler(methode3)

plt.figure(figsize=(10,6))
plt.xlabel("n")
plt.ylabel("Relativer Fehler")
plt.yscale('log')
plt.title("Relativer Fehler in Abhängigkeit von n für drei Methoden")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.plot(index, fehler1, label="Methode 1", marker='o')
plt.plot(index, fehler2, label="Methode 2", marker='v')
plt.plot(index, fehler3, label="Methode 3", marker='s')

plt.legend()
plt.show()
