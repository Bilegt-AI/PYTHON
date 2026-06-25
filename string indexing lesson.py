# indexing = accessing elements of a sequence using [] (indexing operators)
# [start : end : step]

credit_number="1234-5678-9010-1234"

print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-5])
print(credit_number[::2])
print(credit_number[15:20])

last_digits=credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
