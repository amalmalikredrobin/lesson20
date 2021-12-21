file = open('data.txt', 'r+')

# for num in range(1, 11):
#     file.write(f'{num}\n')

names = file.readlines()
file.seek(0)

for name in names:
    file.write(name.upper())
    print(file.tell())

file.close()

print(file.close)