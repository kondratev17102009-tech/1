def bisection_method(f, a, b, eps=1e-5):
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах отрезка")
    
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    return (a + b) / 2

# Пример использования для уравнения x^3 - x - 2 = 0 на отрезке [1, 2]
f = lambda x: x**3 - x - 2
root = bisection_method(f, 1, 2)
print(f"Корень: {root}")
