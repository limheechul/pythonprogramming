def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def get_real(prompt):
    return float(input(prompt))

fahrenheit = get_real("변환하고자 하는 화씨온도? ")

celsius = fahrenheit_to_celsius(fahrenheit)

print(f"화씨 {fahrenheit:.1f} 도는 섭씨 {celsius} 도")
