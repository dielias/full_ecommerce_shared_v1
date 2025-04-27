import psutil
import time
import requests
import csv

def test_resource_usage_during_request():
    process = psutil.Process()
    
    # Antes de fazer a requisição
    memory_before = process.memory_info().rss
    cpu_before = process.cpu_percent(interval=None)

    start_time = time.time()

    # Faz uma requisição para seu serviço (por exemplo, listar produtos)
    response = requests.get("http://localhost:8002/products")

    elapsed_time = time.time() - start_time

    # Depois da requisição
    memory_after = process.memory_info().rss
    cpu_after = process.cpu_percent(interval=None)

    print(f"Memory Before: {memory_before} bytes")
    print(f"Memory After: {memory_after} bytes")
    print(f"CPU Before: {cpu_before}%")
    print(f"CPU After: {cpu_after}%")
    print(f"Elapsed Time: {elapsed_time:.4f} seconds")

    assert response.status_code == 200
    assert elapsed_time < 2.0  # Por exemplo, queremos respostas em menos de 2 segundos

    # Salvar os dados em um arquivo CSV
def save_stats_to_csv():
    with open("resource_usage_results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Endpoint", "CPU (%)", "Memória (%)", "Swap (%)", "Tempo de Resposta (s)"])

        for i in range(len(stats["endpoint"])):
            writer.writerow([
                stats["endpoint"][i],
                stats["cpu_percent"][i],
                stats["memory_percent"][i],
                stats["swap_percent"][i],
                stats["response_time"][i],
            ])

save_stats_to_csv()
print("✅ Resultados salvos em resource_usage_results.csv!")

