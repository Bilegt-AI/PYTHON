name = "Bilegt"
age = 22
salary = 4500.6789
balance = -1234.5
items = 3000000

# 1. salary-г аравтын 2 орон хүртэл хэвлэ.
print(f"Your Salary Is ${salary:.2f}")

# 2. salary-г аравтын 4 орон хүртэл хэвлэ.
print(f"Your Average Salary Is ${salary:.4f}")

# 3. salary-г нийт 10 зайтай, баруун талд байрлуулж хэвлэ.
print(f"Your Salary Is ${salary:10.2f}")
print(f"Your Salary Is ${salary:<10}")

# 4. salary-г нийт 15 зайтай, зүүн талд байрлуулж хэвлэ.
print(f"Your Salary Is ${salary:<15.2f}")

# 5. name-г нийт 20 зайтай, төвд байрлуулж хэвлэ.
print(f"Your Name Is {name:^20}")

# 6. items-г таслалтай (1,000,000 хэлбэрт) хэвлэ.
print(f"Your Item Count Is {items:,}")

# 7. balance сөрөг тоо. salary эерэг тоо. Хоёуланг нь + тэмдэгтэй, 
# аравтын 2 орон хүртэл хэвлэ.
print(f"{abs(balance):.2f}")
print(f"Your Portfolio Is {salary:+.2f}")

# 8. age-г нийт 5 зайтай, тэгээр дүүргэж хэвлэ. (жишээ: 00022)
print(f"Your Age Is {age:>05}")

# 9. salary-г нийт 12 зай, аравтын 2 орон,
#  баруун талд байрлуулж нэгэн зэрэг хэвлэ.
print(f"Your Salary Is {salary:>12.2f}")

# 10. f"My name is {name}, I am {age} years old, 
# my salary is {salary}" гэсэн өгүүлбэрийг — 
# name 10 зай төвд, age тэгээр дүүргэж 3 зай, 
# salary аравтын 2 орон хүртэл форматлаж хэвлэ.

print(f"My name is {name:^10}, I am {age:03} years old, my salary is {salary:.2f}")
