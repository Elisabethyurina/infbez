def func(str1,str2):
    array = []
    for i in str2:
        array.append(ord(i)- ord('A'))
    res = ''
    for i in range(len(str1)):
        res += chr((ord(str1[i])-ord("A")+array[i%len(array)])%26+ord('A'))
    return res
t = input("Введите фразу\n")
f = input("Введите кодовую фразу\n")
print("Ваша фраза: ", func(t.upper(), f.upper()))


