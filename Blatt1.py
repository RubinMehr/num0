import math
import matplotlib.pyplot as plt

# Funktion zur Berechnung des Polynoms mit Algorithmus 1 (naiver Näherungswert)
def naiverNäherungswert(x, n):
    sum = 0
    for k in range(0, n+1):
        sum += (x**k) / math.factorial(k)
    return sum

# Funktion zur Berechnung des relativen Fehlers
def relFehler(yTilde):
    exact_value = math.exp(-5.5)
    absFehler = abs(yTilde - exact_value)
    return absFehler / abs(exact_value)

# Function to calculate the polynomial using Horner's scheme
def horner_approximation(x, n):
    # Start from the term with the highest factorial, which is 1/n!
    result = 1 / math.factorial(n)
    # Loop backwards from n-1 down to 0, applying Horner's method
    for k in range(n - 1, -1, -1):
        result = result * x + 1 / math.factorial(k)
    return result


# Liste zur Speicherung der Näherungswerte für jede Methode und jedes n
methode1 = []
methode2 = []
methode3 = []
n_values = list(range(3, 31, 3))

# Berechnung der Näherungswerte
for n in n_values:
    methode1.append(naiverNäherungswert(-5.5, n))
    methode2.append(1 / naiverNäherungswert(5.5, n))
    methode3.append(naiverNäherungswert(-0.5, n) ** 11)

# Berechnung der relativen Fehler für jede Methode
relative_errors = {
    "Direct": [relFehler(approx) for approx in methode1],
    "Reciprocal": [relFehler(approx) for approx in methode2],
    "PowerForm": [relFehler(approx) for approx in methode3]
}

# Erstelle das Plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, relative_errors["Direct"], label="Direkte Berechnung", marker='o')
plt.plot(n_values, relative_errors["Reciprocal"], label="Kehrwert-Form", marker='s')
plt.plot(n_values, relative_errors["PowerForm"], label="Potenz-Form", marker='^')

# Logarithmische Skalierung der y-Achse
plt.yscale('log')

# Labels und Titel
plt.xlabel("n")
plt.ylabel("Relativer Fehler")
plt.title("Relativer Fehler in Abhängigkeit von n für drei Methoden")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Zeige das Plot
plt.show()
