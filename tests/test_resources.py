import psutil
import time
import csv

def monitor_resources(duration=30, output_file="resource_usage.csv"):
    print(f"Monitorando uso de recursos por {duration} segundos...")
    start_time = time.time()

    # Cria ou sobrescreve o arquivo CSV
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CPU (%)", "Memória (%)", "Swap (%)"])

        while time.time() - start_time < duration:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            swap = psutil.swap_memory()

            # Escrever uma linha no CSV
            writer.writerow([timestamp, cpu_percent, memory.percent, swap.percent])

            print(f"{timestamp} | CPU: {cpu_percent}% | Memória: {memory.percent}% | Swap: {swap.percent}%")

    print(f"✅ Monitoramento finalizado! Dados salvos em '{output_file}'.")

if __name__ == "__main__":
    monitor_resources(duration=30)  # ou ajuste a duração que quiser
