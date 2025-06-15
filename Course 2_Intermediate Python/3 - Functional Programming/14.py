
numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num % 2 == 0)

even_numbers = [num for num in numbers if num % 2 == 0]

for num in numbers:
    if num % 2 != 0:
        odd.append(num % 2 != 0)

odd_numbers = [num for num in numbers if num % 2 != 0]  

print(f"Original Numbers: {numbers}")
print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")  