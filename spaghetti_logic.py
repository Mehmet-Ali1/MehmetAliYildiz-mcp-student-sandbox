
INCREASE_RATE = 1.15

def calculate_totals(data, rate=INCREASE_RATE):
    """Verilen verileri oranla çarpar ve yeni değerleri döndürür."""
    return [item * rate for item in data]

def format_totals(totals):
    """Her bir toplamı biçimlendirir ve string listesi döndürür."""
    return [f"Total: {total:.2f}" for total in totals]

def print_totals(formatted_totals):
    """Biçimlendirilmiş toplamları ekrana yazdırır."""
    for line in formatted_totals:
        print(line)

def log_totals(totals, filename="log.txt"):
    """Toplamları dosyaya kaydeder."""
    with open(filename, "a") as f:
        f.write(str(totals) + "\n")

def process_data(data):
    """Veri işleme akışını yönetir."""
    totals = calculate_totals(data)
    formatted = format_totals(totals)
    print_totals(formatted)
    log_totals(totals)
    return totals
