def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

if __name__ == "__main__":
    choice = input("Choose conversion (C-F, F-C, C-K, K-C, F-K, K-F): ").strip().upper()
    temp = float(input("Enter temperature: "))

    conversions = {
        "C-F": celsius_to_fahrenheit,
        "F-C": fahrenheit_to_celsius,
        "C-K": celsius_to_kelvin,
        "K-C": kelvin_to_celsius,
        "F-K": fahrenheit_to_kelvin,
        "K-F": kelvin_to_fahrenheit
    }

    if choice in conversions:
        print(f"Converted Temperature: {conversions[choice](temp)}")
    else:
        print("Invalid choice.")
