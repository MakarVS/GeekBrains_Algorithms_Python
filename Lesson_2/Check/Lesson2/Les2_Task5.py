#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. 
#Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

def f(str, n, code):
    if code > 127:
        return
    str = f"{str}\t{code} {chr(code)}"
    if n % 10 == 0 or code == 127:
        print(str)
        str = ''
    f(str, n + 1, code + 1)
    return

f('', 1, 32)

