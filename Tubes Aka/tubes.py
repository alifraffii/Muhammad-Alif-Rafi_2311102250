import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import math


# Rekursif: Hitung nilai e^x menggunakan deret Taylor
def exp_recursive(x, n):
    if n == 0:
        return 1
    return (x ** n) / math.factorial(n) + exp_recursive(x, n - 1)

# Iteratif: Hitung nilai e^x menggunakan deret Taylor
def exp_iterative(x, n):
    result = 1
    for i in range(1, n + 1):
        result += (x ** i) / math.factorial(i)
    return result

# Grafik untuk menyimpan data
x_values = []
recursive_times = []
iterative_times = []

# Fungsi untuk memperbarui grafik
def update_graph():
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, recursive_times, label='Recursive', marker='o', linestyle='-')
    plt.plot(x_values, iterative_times, label='Iterative', marker='o', linestyle='-')
    plt.title('Performance Comparison: Recursive vs Iterative for e^x')
    plt.xlabel('Input (x)')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Fungsi untuk mencetak tabel waktu eksekusi
def print_execution_table():
    table = PrettyTable()
    table.field_names = ["x", "Recursive Time (s)", "Iterative Time (s)"]
    min_len = min(len(x_values), len(recursive_times), len(iterative_times))
    for i in range(min_len):
        table.add_row([x_values[i], recursive_times[i], iterative_times[i]])
    print(table)

# Program utama
while True:
    try:
        x = float(input("Masukkan nilai x (atau ketik -1 untuk keluar): "))
        if x == -1:
            print("Program selesai. Terima kasih!")
            break
        if x < 0:
            print("Masukkan nilai x yang positif atau nol!")
            continue

        n_terms = 10  # Jumlah suku deret Taylor
        x_values.append(x)

        # Ukur waktu eksekusi algoritma rekursif
        start_time = time.time()
        exp_recursive(x, n_terms)
        recursive_times.append(time.time() - start_time)

        # Ukur waktu eksekusi algoritma iteratif
        start_time = time.time()
        exp_iterative(x, n_terms)
        iterative_times.append(time.time() - start_time)

        # Cetak tabel waktu eksekusi
        print_execution_table()

        # Perbarui grafik
        update_graph()

    except ValueError:
        print("Masukkan nilai x yang valid!")