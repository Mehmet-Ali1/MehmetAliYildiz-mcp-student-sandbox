
def safe_divide(numerator, denominator):
    """Sıfıra bölme hatasını önler."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None

def average_ratios(numbers):
    """Her sayı için 100/sayı oranını hesaplar, sıfırları atlar."""
    ratios = []
    for number in numbers:
        result = safe_divide(100, number)
        if result is not None:
            ratios.append(result)
        else:
            print(f"Uyarı: 0'a bölme atlandı (girdi: {number})")
    if not ratios:
        raise ValueError("Geçerli oran hesaplanamadı: tüm girdiler sıfır!")
    return sum(ratios) / len(ratios)

def main():
    numbers = [10, 5, 0]
    try:
        avg = average_ratios(numbers)
        print(f"Ortalama oran: {avg:.2f}")
    except ValueError as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()
