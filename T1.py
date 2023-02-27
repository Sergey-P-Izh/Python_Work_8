
def inputText():
with open('file.txt', 'a') as data:
surname = data.write(input('Введите фамилию'))
data.write(' ')
name = data.write(input('Введите имя'))
data.write(' ')
fathername = data.write(input('Введите отчество'))
data.write(' ')
phoneNumber = data.write(input('Введите номер телефона'))
data.write('\n')

def printText():
path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
print(line)
data.close()

def checkText(userInfo):
path = 'file.txt'
data = open('file.txt', 'r')

for line in data.readlines():
if userInfo in line:
print(line)
data.close()

inputText()
printText()
checkText(input('Введите данные'))

with open("data2.txt", "w") as f: for _ in range(5):
     f.write(input("введи строку : ")) with open("data2.txt") as f: list1 =
    f.readlines() list1[1] = "Иванов Пётр\n"
    list1.pop(3) print(list1) with open("data2.txt", "w") as f: f.writelines(list1)