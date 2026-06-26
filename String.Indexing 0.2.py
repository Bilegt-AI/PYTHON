credit_number = "1234-5678-9010-1234"

print(credit_number[0])
print(credit_number[-1])
print(credit_number[5:9])
print(credit_number[10:14])
print(credit_number[-4:])
print(credit_number[::-1])
print(credit_number.replace('-',''))
result=len(credit_number)
print(result)
last_degits=credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_degits}")
