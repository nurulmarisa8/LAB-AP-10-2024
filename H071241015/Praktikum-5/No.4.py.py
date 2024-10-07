str = input("Input your string: ")

print("=" * 30)

result = []

for length in range(1, len(str) + 1): 
    for i in range(len(str) - length + 1):  
        result.append(str[i:i + length])

print("\n".join(result))
