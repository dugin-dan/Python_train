##5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

s_all = 0
n = True
print('Введите числа, разделенные пробелом, или q для завершения программы:')
while n:
    nums = input().split(" ")
    s = 0
    k = False
    for i in nums:
        if i == 'q':
            print(s_all,'(',s,')')
            n = False
            break
        else:
            try:
                s += float(i)
            except:
                k = True 
    s_all += s
    if k:
        print('Вводите только числа, разделенные пробелом, или q для завершения работы')
    print(s_all,'(',s,')')