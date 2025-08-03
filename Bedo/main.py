#pyre-strict

print("hello")
nums: list[int] = [1, 2, 3, 4, 5]

def sum(a: int, b: int) -> int:  
    return a + b

for i in nums:
    if i == 3:
        print("Welcome Abdelrahman")
    else:
        print("not expected")

print(sum(2, 3))
