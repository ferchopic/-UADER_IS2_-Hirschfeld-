import matplotlib.pyplot as plt


def collatz(n):
    """Calcula la secuencia de Collatz para un número dado."""
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

def main():
    """Calcula el número de iteraciones de la conjetura de Collatz para números del 1 al 10000."""
    numbers = list(range(1, 10001))
    iterations = [collatz(n) for n in numbers]

    # Gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(iterations, numbers, s=5, color='blue')
    plt.title('numero de iteraciones de la conjetura de Collatz para numeros del 1 al 10000')
    plt.xlabel('iteracion')
    plt.ylabel('numero de comienzo')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
