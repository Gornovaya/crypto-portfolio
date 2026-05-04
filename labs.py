# 0.	Нахождение НОК.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)
print(f"[{num1},{num2}] = {num1}*{num2} / ({num1},{num2})")
print(f"[{num1},{num2}] = {num1 * num2} / {gcd_result}")
print(f"[{num1},{num2}] = {lcm_result}")

# ===================================================================================
# 1.	нахождение НОД и его линейного разложения по расширенному алгоритму Эвклида.
def gcd_table(a, b):
    r0, r1 = a, b
    print(f"{'r':>4} {'q':>4}")
    print(f"{r0:>4} {'-':>4}")
    print(f"{r1:>4} {'-':>4}")
    
    while r1 != 0:
        q = r0 // r1
        r = r0 % r1
        print(f"{r:>4} {q:>4}")
        r0, r1 = r1, r
    return r0

def extended_gcd(a, b):
    r0, r1 = a, b
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    print(f"{'r':>4} {'q':>4} {'x':>4} {'y':>4}")
    print(f"{r0:>4} {'-':>4} {x0:>4} {y0:>4}")
    print(f"{r1:>4} {'-':>4} {x1:>4} {y1:>4}")
    while r1 != 0:
        q = r0 // r1
        r = r0 % r1
        x = x0 - q * x1
        y = y0 - q * y1  
        print(f"{r:>4} {q:>4} {x:>4} {y:>4}")
        r0, r1 = r1, r
        x0, x1 = x1, x
        y0, y1 = y1, y
    return r0, x0, y0

a = int(input("Введите a: "))
b = int(input("Введите b: "))

print("\n----------------------")
print("Алгоритм Евклида:")
gcd_table(a, b)
print("----------------------\n")

print("Расширенный алгоритм Евклида:")
g, x, y = extended_gcd(a, b)
print("----------------------\n")

print(f"НОД({a}, {b}) = {g}")
print(f"Линейное разложение: {g} = {a}*({x}) + {b}*({y})")

# ===================================================================================
# 2.	поиск простых чисел до числа n (с помощью алгоритмов, которые вы готовили на доклады) +приложить презентацию.
# Методы: Решето Эратосфена и Решето Сундарама.
def erat(n):
    #Создаем список, где все числа считаются простыми (True)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  #0 и 1 не являются простыми числами

    p = 2
    while p * p <= n:
        if is_prime[p]: # Если число p все еще считается простым помечаем все его кратные как не простые
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

def sund(n):
    if n < 2:
        return []
    k = (n - 2) // 2
    is_prime = [True] * (k + 1)

    # Применяем решето Сундарама
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            is_prime[i + j + 2 * i * j] = False
            j += 1

    primes = [2]  #2 - единственное четное простое число
    primes.extend([2 * i + 1 for i in range(1, k + 1) if is_prime[i]])

    return primes
n = int(input("Поиск простых чисел до n. Введите n: "))
choise = int(input("Какой метод нахождения простых чисел вы хотите использовать? \nНажмите\n1 - Решето Эратосфена. \n2 - Решето Сундарама\nЯ выбираю "))

if choise == 1:
    primes = erat(n)
    print(f"Простые числа до {n}: {primes}")
elif choise == 2:
    primes = sund(n)
    print(f"Простые числа до {n}: {primes}")
else:
    print("Введите 1 или 2.")

# ===================================================================================
# 3.	каноническое разложение числа на простые множители (с помощью алгоритмов, которые вы готовили на доклады)+приложить презентацию
# Метод: Факторизация Ферма
import math

#является ли число n полным квадратом
def is_perfect_square(n):
    root = int(math.isqrt(n))
    return root * root == n

def fermat_factorization(n):
    # Проверка на четность
    if n % 2 == 0:
        print("Внимание: Алгоритм факторизации Ферма работает только с нечетными числами.")
        return None, None

    x = int(math.sqrt(n))
    print(f"Исходное число n: {n}")
    print(f"Начальное значение x: {x}")

    k = 1
    while True:
        x_k = x + k
        y_squared = x_k * x_k - n
        print(f"Шаг k={k}: x={x_k}, y^2={y_squared}")

        if is_perfect_square(y_squared):
            y = int(math.isqrt(y_squared))
            print(f"Берем квадратный корень из y^2 => y = {y}")
            a = x_k + y
            b = x_k - y
            print(f"Найдены множители: n = {x_k}^2 - {y}^2 = ({x_k}+{y})({x_k}-{y}) = {a}*{b}")
            return a, b

        k += 1

def canonical_decomposition(n):
    factors = []
    #Факторизуем число n
    a, b = fermat_factorization(n)
    if a is None or b is None:
        return "Невозможно разложить на множители с использованием метода факторизации Ферма."

    factors.append(a)
    factors.append(b)
    factors.sort()

    #Создаем словарь для подсчета степеней каждого простого множителя
    factor_count = {}
    for factor in factors:
        if factor in factor_count:
            factor_count[factor] += 1
        else:
            factor_count[factor] = 1

    canonical_form = " * ".join([f"{factor}^{count}" if count > 1 else f"{factor}" for factor, count in factor_count.items()])
    return canonical_form

n = int(input("Введите число n: "))
canonical_form = canonical_decomposition(n)
print(f"Каноническое разложение числа {n}: {canonical_form}")

# ===================================================================================
# 4.	расчет функции Эйлера для m
def euler(m):
    def prime(n):
        f = {}
        i = 2
        while i * i <= n:
            while (n % i) == 0:
                if i in f:
                    f[i] += 1
                else:
                    f[i] = 1
                n //= i
            i += 1
        if n > 1:
            f[n] = 1
        return f

    f = prime(m)
    phi = m
    factor_str = " * ".join([f"{factor}^{f[factor]}" if f[factor] > 1 else f"{factor}" for factor in f])
    res = f"φ({m}) = φ({factor_str}) = "
    for factor in f:
        phi *= (1 - 1/factor) 
    res += " * ".join([f"({factor}^{f[factor]}-{factor}^{f[factor]-1})" if f[factor] > 1 else f"({factor}-1)" for factor in f])
    res += f" = {int(phi)}"  
    return res

m = int(input("Введите число: "))
result = euler(m)
print(f"Функция Эйлера: {result}")

# ===================================================================================
# 5.	нахождение обратного элемента в Zm
def extended_gcd(a, b):
    table = []
    x0, x1, y0, y1 = 1, 0, 0, 1
    r0, r1 = a, b  
    while r1 != 0:
        q = r0 // r1 
        r0, r1 = r1, r0 - q * r1
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        table.append((r0, q, x0, y0))
    return r0, x0, y0, table

def find_inverse_element(a, m):
    gcd, x, y, table = extended_gcd(a, m)
    print("\n|  r  |  q  |  x  |  y  |")
    print("|-----|-----|-----|-----|")
    for row in table:
        print(f"| {row[0]:3} | {row[1]:3} | {row[2]:3} | {row[3]:3} |")
    x_str = f"({x})" if x < 0 else f"{x}"
    y_str = f"({y})" if y < 0 else f"{y}"
    print(f"\nИтоговый расчет: {gcd} = {a} * {x_str} + {m} * {y_str}")
    if gcd == 1:
        #Если НОД(a, m) = 1, то x - обратный элемент
        inverse = x % m
        print(f"\nОбратный элемент к {a} по модулю {m} равен {inverse}")
    else:
        print(f"\nОбратный элемент не существует, так как НОД({a}, {m}) = {gcd} ≠ 1")
a = int(input("Введите число: "))
m = int(input("Введите модуль: "))
find_inverse_element(a, m)


# ===================================================================================
# 6.	решение сравнений (для простого и составного m)
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

#обратный элемент a по модулю m
def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise ValueError(f"Обратный элемент не существует, так как НОД({a}, {m}) = {gcd} != 1")
    else:
        return x % m

def sravn(a, b, m):
    gcd, _, _ = gcd_extended(a, m)
    
    if gcd != 1:
        print(f"НОД({a}, {m}) = {gcd} != 1, сравнение не имеет единственного решения.")
        return None
    
    print(f"НОД({a}, {m}) = 1, сравнение имеет единственное решение.")
    
    u = mod_inverse(a, m)
    print(f"Обратный элемент для {a} по модулю {m} равен {u}.")
    
    x = (u * b) % m
    print(f"Решение сравнения {a}*x ≡ {b} (mod {m}):")
    print(f"{u}*{a}x ≡ {u}*{b} (mod {m})")
    print(f"x ≡", u*b , f"(mod {m})")
    print(f"x ≡ {x} (mod {m})")
    print(f"Ответ: x = {x} + {m}k")
    
    return x

print(f"Решение сравнения вида a*x ≡ b(mod m):")
a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
m = int(input("Введите модуль m: "))
sravn(a, b, m)

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise ValueError(f"Обратный элемент не существует, так как НОД({a}, {m}) = {gcd} != 1")
    else:
        return x % m

def solve_linear_congruence(a, b, m):
    gcd, _, _ = gcd_extended(a, m)
    
    if b % gcd != 0:
        print(f"НОД({a}, {m}) = {gcd}, но {b} не делится на {gcd}, сравнение не имеет решений.")
        return None
    
    print(f"НОД({a}, {m}) = {gcd}, сравнение имеет {gcd} решений.")
    
    #Делим все уравнение на gcd
    a //= gcd
    b //= gcd
    m //= gcd
    print(f"После деления на {gcd}: {a}*x ≡ {b} (mod {m})")
    u = mod_inverse(a, m)
    print(f"Обратный элемент для {a} по модулю {m} равен {u}.")
    x0 = (u * b) % m
    print(f"Решение сравнения {a}*x ≡ {b} (mod {m}):")
    print(f"U*{a}*x ≡ U*{b} (mod {m})")
    print(f"x ≡ {x0} (mod {m})")
    solutions = []
    for k in range(gcd):
        x = x0 + k * m
        solutions.append(x)
        print(f"x{k+1} = {x0} + {k}*{m} = {x} (mod {m * gcd})")
    return solutions

a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
m = int(input("Введите модуль m: "))
solve_linear_congruence(a, b, m)

# ===================================================================================
# 7.	решение системы сравнений китайским алгоритмом
# Первый способ:
from math import gcd

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Обратный элемент не существует, так как a и m не взаимно просты.")
    return x % m

def solve_congruences(a, m, b, n):
    print(f"Решаем систему сравнений:")
    print(f"x ≡ {a} (mod {m})")
    print(f"x ≡ {b} (mod {n})")
    
    if gcd(m, n) != 1:
        raise ValueError("Система не имеет единственного решения, так как НОД(m, n) ≠ 1.")
    
    print(f"НОД({m}, {n}) = 1 -> решение единственное по mod {m*n}")
    print("\n")
    
    #Решаем первое сравнение: x = a + m*k
    print(f"(1). Решаем первое сравнение:\n x = {a} + {m}*k")
    
    #Подставляем во второе сравнение: a + m*k ≡ b (mod n)
    print(f"(2). Подставляем x во второе сравнение:\n {a} + {m}*k ≡ {b} (mod {n})")
    
    k_coeff = m % n
    k_const = (b - a) % n
    print(f"Получаем: {k_coeff}*k ≡ {k_const} (mod {n})")
    
    #Находим обратный элемент к k_coeff по модулю n
    k_inverse = mod_inverse(k_coeff, n)
    print(f"(3). Находим обратный элемент к {k_coeff} по модулю {n}: {k_inverse}")
    
    print(f"Умножаем предыдущее уравнение на {k_inverse} и получаем:")
    print(f"{k_inverse}*{k_coeff}*k ≡ {k_const}*{k_inverse} (mod {n}) ")
    
    #Решаем сравнение k ≡ k_inverse * k_const (mod n)
    k = (k_inverse * k_const) % n
    print(f"(4). Решаем сравнение:\n k ≡ {k_inverse} * {k_const} (mod {n})")
    print(f"k ≡ {k} (mod {n})")
    
    #Подставляем k обратно в решение первого сравнения
    print(f"(5).Подставляем k = {k} обратно в первое сравнение:\n x = {a} + {m}*{k}")
    x = a + m * k
    print(f"x = {x} + {m*n}*t")
    
    #Решение по модулю m*n
    print(f"Решение системы сравнений: x ≡ {x % (m * n)} (mod {m*n})")
    print(f"Ответ: x ≡ {x % (m * n)} + {m*n}k")
    return x % (m * n)

a = 1
m = 7
b = 4
n = 5

solution = solve_congruences(a, m, b, n)

# Второй способ:
from math import gcd
def gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inverse(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        raise ValueError("Обратный элемент не существует, так как a и m не взаимно просты.")
    return x % m

def result(system):
    n = len(system)
    M = 1
    for a, m in system:
        M *= m 
    table = []
    for i, (a, m) in enumerate(system):
        Mi = M // m
        yi = mod_inverse(Mi, m)
        table.append((a, Mi, yi, m))
        print(f"Строка {i+1}: bi = {a}, Mi = {Mi}, yi = {yi}, mi = {m}")
        print(f"y{i+1} - это обратный элемент для {Mi} по модулю {m}")
    print("\nТаблица:")
    print("| bi | Mi | yi | mi |")
    for bi, Mi, yi, mi in table:
        print(f"| {bi}  | {Mi}  | {yi}  | {mi}  |")
    x = 0
    print("\nВычисление x:")
    print(f"\nОбщий модуль M = Пmi = {M}") 
    for bi, Mi, yi, mi in table:
        term = bi * Mi * yi
        x += term
        print(f"->: bi * Mi * yi = {bi} * {Mi} * {yi} = {term}")
    
    x %= M
    print(f"Сумма предыдущих значений: {x} (mod {M})")
    print(f"Решение системы сравнений: x ≡ {x} + {M}k")
    return x

def main():
    choise = int(input("Введите количество уравнений (от 2 до 4): "))
    if choise < 2 or choise > 4:
        print("Количество уравнений должно быть от 2 до 4.")
        return
    system = []
    for i in range(choise):
        a = int(input(f"Введите a{i+1}: "))
        m = int(input(f"Введите m{i+1}: "))
        system.append((a, m)) 
    print("\n")
    result(system)

if __name__ == "__main__":
    main()

# ===================================================================================
# 8.	нахождение вычета a^k(mod m) для простого и составного m
from math import gcd
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#возведение в степень по мод
def mod_exp(a, k, m):
    result = 1
    base = a % m
    while k > 0:
        if k % 2 == 1:
            result = (result * base) % m
        base = (base * base) % m
        k //= 2
    return result

#малая теорема ферма для простого m
def fermat_mod_exp(a, k, m):
    if is_prime(m):
        reduced_k = k % (m - 1)
        print(f"{a}^{k} (mod {m}) = {k} (mod {m - 1}) = {reduced_k} (mod {m - 1})")
        result = mod_exp(a, reduced_k, m)
        print(f"= {a}^{reduced_k} (mod {m}) = {result}")
        return result
    return mod_exp(a, k, m)

def gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inverse(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        raise ValueError("Обратный элемент не существует, так как a и m не взаимно просты.")
    return x % m

#КТО для составного m
def crt(system):
    n = len(system)
    M = 1
    for a, m in system:
        M *= m
        
    print("\n")
    table = []
    for i, (a, m) in enumerate(system):
        Mi = M // m
        yi = mod_inverse(Mi, m)
        table.append((a, Mi, yi, m))
        print(f"Строка {i+1}: bi = {a}, Mi = {Mi}, yi = {yi}, mi = {m}")
        print(f"y{i+1} - это обратный элемент для {Mi} по модулю {m}")
    
    print("\nТаблица:")
    print("| bi | Mi | yi | mi |")
    for bi, Mi, yi, mi in table:
        print(f"| {bi}  | {Mi}  | {yi}  | {mi}  |")
    
    x = 0
    print("\nВычисление x:")
    print(f"\nОбщий модуль M = Пmi = {M}")
    
    for bi, Mi, yi, mi in table:
        term = bi * Mi * yi
        x += term
        print(f"->: bi * Mi * yi = {bi} * {Mi} * {yi} = {term}")
    
    x %= M
    print(f"Сумма предыдущих значений: {x} (mod {M})")
    print(f"Решение системы сравнений: x ≡ {x} + {M}k")
    return x

# Вычисление a^k(mod m) для составного m с использованием КТО
def composite_mod_exp(a, k, m):
    if is_prime(m):
        return fermat_mod_exp(a, k, m)
    
    #Разложение m на простые множители
    factors = []
    temp = m
    for i in range(2, int(m**0.5) + 1):
        while temp % i == 0:
            factors.append(i)
            temp //= i
    if temp > 1:
        factors.append(temp)
    
    #Вычисление остатков по модулям простых множителей
    system = []
    for factor in factors:
        remainder = fermat_mod_exp(a, k, factor)
        system.append((remainder, factor))
    
    #КТО
    return crt(system)

def main():
    a = int(input("Введите число a: "))
    k = int(input("Введите степень k: "))
    m = int(input("Введите модуль m: "))
    
    if is_prime(m):
        result = fermat_mod_exp(a, k, m)
        print(f"{a}^{k} mod {m} = {result}")
    else:
        result = composite_mod_exp(a, k, m)
        print(f"{a}^{k} mod {m} = {result}")

if __name__ == "__main__":
    main()

# ===================================================================================
# 9.	нахождение первообразного корня (образующего элемента) и формирование с его помощью приведенной системы вычетов
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def f_eulr(phi):
    f = {}
    div = 2
    while phi > 1:
        while phi % div == 0:
            if div in f:
                f[div] += 1
            else:
                f[div] = 1
            phi //= div
        div += 1
    return f

def is_primitive_root(a, p, f):
    for factor in f:
        power = (p - 1) // factor
        result = pow(a, power, p)
        print(f"   {a}^{power} ≡ {result} (mod {p})")
        if result == 1:
            return False
    return True

def find_pr_root(p):
    phi = p - 1
    f = f_eulr(phi)
    for a in range(2, p):
        if gcd(a, p) == 1:
            print(f"Проверка {a}:")
            if is_primitive_root(a, p, f):
                return a
            print(f"   {a} не является первообразным корнем!")
    return None

def vichet_sys(p, g):
    rrs = []
    for i in range(p - 1):
        rrs.append(pow(g, i, p))
    return sorted(rrs)

def main():
    p = int(input("Введите простое число m: "))
    
    print(f"1. Факторизация функции Эйлера φ({p}) = {p-1}")
    phi = p - 1
    f = f_eulr(phi)
    print(f"   Факторизация: {f}")
    
    g = find_pr_root(p)
    if g is None:
        print(f"Первообразный корень для {p} не найден.")
        return
    
    print(f"2. Найден первообразный корень: {g}")
    rrs = vichet_sys(p, g)
        powers = ', '.join([f"{g}^{i}" for i in range(p - 1)])
    values = ', '.join(map(str, rrs))
    print(f"   Приведенная система вычетов U({p}) = {{ {powers} }} = {{ {values} }}")
if __name__ == "__main__":
    main()

# ===================================================================================
# 10.	решение степенного (показательного) сравнения
import math
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def modular_inverse(a, m):
    g, x, y = gcd_extended(a, m)
    if g != 1:
        raise ValueError("Обратный элемент не существует, так как a и m не взаимно просты.")
    return x % m

def mod_n(a, m):
    return a % m

def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def find_primitive_root(m):
    if m == 2:
        return 1
    phi = euler_totient(m)
    prime_factors = set()
    n = phi
    p = 2
    while p * p <= n:
        if n % p == 0:
            prime_factors.add(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        prime_factors.add(n)
    
    for g in range(2, m):
        is_primitive = True
        for factor in prime_factors:
            if pow(g, phi // factor, m) == 1:
                is_primitive = False
                break
        if is_primitive:
            return g
    return None

def solve_congruence(g, m):
    system = {}
    phi = euler_totient(m)
    for i in range(1, phi + 1):
        system[pow(g, i, m)] = i
    return system

def solve_a_power_x():
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    m = int(input("Введите m: "))
    a = mod_n(a, m)
    b = mod_n(b, m)
    fi = euler_totient(m)
    g = find_primitive_root(m)
    system = solve_congruence(g, m)
    print("\n==Решение==\n")
    print(f"ind{a}*x = ind{b}(mod {fi})")
    for key, value in system.items():
        if key == a:
            a_new = value
            break
    for key, value in system.items():
        if key == b:
            b_new = value
            break
    print(f"{a_new}*x = {b_new}(mod {fi})")
    nod = gcd_extended(a_new, fi)[0]
    if b_new % nod == 0:
        a_new = a_new // nod
        b_new = b_new // nod
        m_new = fi // nod
        a_inv = modular_inverse(a_new, m_new)
        a_new = mod_n(a_new * a_inv, m_new)
        b_new = mod_n((b_new * a_inv), m_new)
        print(f"Ответ: {b_new} + {m_new}k\n")
    else:
        print("Нет решения\n")

def solve_ax_power_p():
    n = int(input("Введите a: "))
    a = int(input("Введите p: "))
    b = int(input("Введите b: "))
    m = int(input("Введите m:"))
    n = mod_n(n, m)
    a = mod_n(a, m)
    b = mod_n(b, m)
    fi = euler_totient(m)
    g = find_primitive_root(m)
    system = solve_congruence(g, m)
    if n != 1:
        n_inv = modular_inverse(n, m)
        n = mod_n(n * n_inv, m)
        b = mod_n(b * n_inv, m)
        print("\n==Решение==\n")
        print(f"{n}*x^{a} = {b}(mod {m})")
        print(f"{a}*ind x = ind{b}(mod {fi})")
    else:
        print("\n==Решение==\n")
        print(f"{a}*ind x = ind{b}(mod {fi})")
    
    nod = gcd_extended(a, fi)[0]
    for key, value in system.items():
        if key == b:
            b_new = value
            break
    if b_new % nod == 0:
        a = a // nod
        b_new = b_new // nod
        m_new = fi // nod
        a_inv = modular_inverse(a, m_new)
        a = mod_n(a * a_inv, m_new)
        b_new = mod_n((b_new * a_inv), m_new)
        print(f"Ответ: {g}^({b_new}+{m_new}*k)\n")
    else:
        print("Нет решения\n")

def main():
    print("Выберите тип сравнения:")
    print("1. a^x = b(mod m)")
    print("2. a*x^p = b(mod m)")
    choice = input("Введите номер типа сравнения: ")
    if choice == '1':
        solve_a_power_x()
    elif choice == '2':
        solve_ax_power_p()
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()

# ===================================================================================
# 11.	нахождение символа Лежандра и символа Якоби
# Сначала проверяет простое ли p. Если да, тогда используется символ Лежандра. Если p-составное, используется символ Якоби.
import math
def erat(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 и 1 не являются простыми числами
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

def is_prime_erat(n):
    primes = erat(n)
    return n in primes
def legendre_symbol(a, p):
    if p < 2:
        raise ValueError("p должно быть больше 1")
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a % 2 == 0:
        return legendre_symbol(a // 2, p) * (-1) ** ((p ** 2 - 1) // 8)
    if a % p == 0:
        return 0
    return legendre_symbol(p % a, a) * (-1) ** ((a - 1) * (p - 1) // 4)

def jacobi_symbol(a, n):
    if n < 1 or n % 2 == 0:
        raise ValueError("n должно быть положительным нечетным числом")
    a = a % n
    t = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a = a % n
    if n == 1:
        return t
    return 0

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = 1
    return factors

def extended_legendre_symbol(a, p):
    if a < 0:
        return (-1) ** ((p - 1) // 2) * extended_legendre_symbol(-a, p)
    a = a % p
    factors = factorize(a)
    result = 1
    for pi, ki in factors.items():
        if ki % 2 == 0:
            result *= 1
        else:
            if pi == 2:
                result *= (-1) ** ((p ** 2 - 1) // 8)
            else:
                result *= legendre_symbol(pi, p)
    return result

def main():
    print("Решение примеров вида (a/p)\n")
    a = int(input("Введите число a: "))
    p = int(input("Введите модуль p: "))
    is_prime = is_prime_erat
    if is_prime(p):
        result = extended_legendre_symbol(a, p)
        print(f"Символ Лежандра ({a}/{p}) = {result}")
    else:
        result = jacobi_symbol(a, p)
        print(f"Символ Якоби ({a}/{p}) = {result}")

if __name__ == "__main__":
    main()

# ===================================================================================
# 12.	нахождение порядка всех элементов в группе Z +m , Z *m
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def order_in_addition_group(m, a):
    order = 1
    while (a * order) % m != 0:
        order += 1
    return order

def order_in_multiplication_group(m, a):
    if gcd(m, a) != 1:
        return None  # Элемент не обратим, порядок не определен
    order = 1
    while (a ** order) % m != 1:
        order += 1
    return order

def find_orders_in_addition_group(m):
    orders = {}
    for a in range(m):
        orders[a] = order_in_addition_group(m, a)
    return orders

def find_orders_in_multiplication_group(m):
    orders = {}
    for a in range(1, m):  # 0 не обратим в группе умножения
        order = order_in_multiplication_group(m, a)
        if order is not None:
            orders[a] = order
    return orders

def print_orders_in_addition_group(m):
    orders = find_orders_in_addition_group(m)
    print(f"|Z{m}^+|={m}", end="")
    for prime_factor in sorted(set(factorize(m))):
        print(f"={m//prime_factor}*{prime_factor}", end="")
    print()
    print("a\tord a")
    for a in range(m):
        print(f"{a}\t{orders[a]}")

def print_orders_in_multiplication_group(m):
    orders = find_orders_in_multiplication_group(m)
    factors = factorize(m)
    unique_factors = sorted(set(factors))
    factor_counts = {factor: factors.count(factor) for factor in unique_factors}
    
    if len(unique_factors) == 1 and unique_factors[0] == 2:
        factor_str = f"2^{factor_counts[2]}"
    else:
        factor_str = "*".join(f"{factor}^{factor_counts[factor]}" if factor_counts[factor] > 1 else f"{factor}" for factor in unique_factors)
    
    print(f"|Z*{m}|={factor_str}")
    print("a\tord a")
    for a in range(1, m):
        print(f"{a}\t{orders.get(a, '')}")

def factorize(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

m = int(input("Введите модуль: "))
print("1.нахождение порядка всех элементов в группе Z+\n" 
    "2.нахождение порядка всех элементов в группе Z*")
choise = int(input("Что вы хотите: "))
if choise == 1:
    print("Группа Z/mZ (сложение по модулю m):")
    print_orders_in_addition_group(m)
elif choise == 2:
    print("\nГруппа Z*m (умножение по модулю m):")
    print_orders_in_multiplication_group(m)
else:
    print("Неверный выбор")


# ===================================================================================
# 13.	разложение группы на подгруппы и формирование для каждой подгруппы смежных классов (для Z +m , Z *m )
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_subgroups(group, operation):
    subgroups = [set()]  # Пустая подгруппа всегда существует
    for i in range(1, 1 << len(group)):  # Перебор всех подмножеств
        subset = set([group[j] for j in range(len(group)) if (i >> j) & 1])
        is_subgroup = True
        if len(subset) > 0:
            if 0 in subset and len(subset)>1: #для аддитивной группы обязательно должен быть 0
                if operation == '+':
                    if 0 not in subset:
                        is_subgroup = False
                else:
                    if 1 not in subset:
                        is_subgroup = False
            if is_subgroup:
                for a in subset:
                    for b in subset:
                        if operation == '+':
                            if (a + b) % 7 not in subset:
                                is_subgroup = False
                                break
                        else:
                            if (a * b) % 7 not in subset:
                                is_subgroup = False
                                break
                    if not is_subgroup:
                        break
        if is_subgroup:
            subgroups.append(subset)
    return subgroups


def generate_cosets(group, subgroup, operation):
    representatives = []
    cosets = []
    used = set()

    for g in group:
        if g not in used:
            coset = set()
            representatives.append(g)
            for h in subgroup:
                if operation == '+':
                    coset.add((g + h) % 7)
                else:
                    coset.add((g * h) % 7)
            cosets.append(sorted(list(coset)))
            used.update(coset)
    return cosets



def additive_group_decomposition(m):
    elements = list(range(m))
    subgroups = find_subgroups(elements, '+')
    for subgroup in subgroups:
        if len(subgroup) > 0:
            print(f"Подгруппа порядка {len(subgroup)}: {sorted(list(subgroup))}")
            cosets = generate_cosets(elements, subgroup, '+')
            print("Смежные классы:")
            for coset in cosets:
                print(f"  + H: {coset}")
            print()


def multiplicative_group_decomposition(m):
    elements = [a for a in range(1, m) if gcd(a, m) == 1]
    subgroups = find_subgroups(elements, '*')
    for subgroup in subgroups:
        if len(subgroup) > 0:
            print(f"Подгруппа порядка {len(subgroup)}: {sorted(list(subgroup))}")
            cosets = generate_cosets(elements, subgroup, '*')
            print("Смежные классы:")
            for coset in cosets:
                print(f"  * H: {coset}")
            print()

n = int(input("Введите модуль m: "))

choise = int(input("Выберите: 1.Z^+m 2.Z^*m:  "))
if choise == 1:
    additive_group_decomposition(n)
elif choise == 2:
    multiplicative_group_decomposition(n)
else:
    print("Ошибка, введите 1 или 2")


# ===================================================================================
# 15.	задать неприводимый многочлен g(x) над полем GF2 и сформировать поле многочленов F[X]/g(x) 
# как конечное расширение поля GF2, построить таблицы Кэли для «+» и «*» групп поля
from sympy import GF, Poly, Symbol

x = Symbol('x')
F = GF(2)
g = Poly(x**2 + x + 1, x, domain=F)
g_deg = g.degree()

elements = []
for i in range(2**g_deg):
    coeffs = [(i >> j) & 1 for j in range(g_deg)]
    poly = Poly(sum(F(c) * x**j for j, c in enumerate(coeffs)), x, domain=F) # ИСПОЛЬЗУЕМ GF(2)
    elements.append(poly)

# таблица Кэли для сложения
addition_table = [[None] * len(elements) for _ in range(len(elements))]
for i, a in enumerate(elements):
    for j, b in enumerate(elements):
        addition_table[i][j] = (a + b).rem(g)

# таблица Кэли для умножения
multiplication_table = [[None] * len(elements) for _ in range(len(elements))]
for i, a in enumerate(elements):
    for j, b in enumerate(elements):
        multiplication_table[i][j] = (a * b).rem(g)

print("Таблица Кэли для сложения:")
for row in addition_table:
    print(row)

print("\nТаблица Кэли для умножения:")
for row in multiplication_table:
    print(row)


# ===================================================================================
# 18.	Умножение Монтгомери 
# Это код для возведения в степень:
def montgomery_multiply(a, b, n, R):
    R_inv = pow(R, -1, n)
    t = a * b
    m = t * R_inv % n
    u = (t + m * n) // R
    if u >= n:
        return u - n
    return u

def montgomery_exponentiation(base, exponent, modulus, R):
    base_mont = (base * R) % modulus
    result_mont = (1 * R) % modulus
    
    while exponent > 0:
        if exponent % 2 == 1:
            result_mont = montgomery_multiply(result_mont, base_mont, modulus, R)
        base_mont = montgomery_multiply(base_mont, base_mont, modulus, R)
        exponent //= 2
    
    R_inv = pow(R, -1, modulus)
    result = montgomery_multiply(result_mont, 1, modulus, R)
    return result

base = 123
exponent = 98
modulus = 1998244353
R = 2**30
result = montgomery_exponentiation(base, exponent, modulus, R)
print(f"{base}^{exponent} mod {modulus} = {result}")

# Код умножения М:
def mon_pro(a, b, n, r, r_inv, n_prime):
    t = a * b
    m = (t * n_prime) % r
    u = (t + m * n) // r
    if u >= n:
        return u - n
    return u
#редукция Монтгомери для t mod n.
def mon_reduce(t, n, r, r_inv, n_prime):
    m = (t * n_prime) % r
    u = (t + m * n) // r
    if u >= n:
        return u - n
    return u
# Преобразует число a в форму Монтгомери
def mon_convert(a, r, n):
    return (a * r) % n
#умножение a*b(mod n) с использованием алгоритма М
def mon_multiply(a, b, n):
    #Выбираем R
    r = 1 << (n.bit_length())

    #Вычисляем r_inv и n_prime
    r_inv = pow(r, -1, n)
    n_prime = -pow(n, -1, r) % r

    # Преобразуем a и b в форму Монтгомери
    a_mon = mon_convert(a, r, n)
    b_mon = mon_convert(b, r, n)

    #умножение Монтгомери
    result_mon = mon_pro(a_mon, b_mon, n, r, r_inv, n_prime)

    #Возвращаем результат в обычном представлении
    return mon_reduce(result_mon, n, r, r_inv, n_prime)

a = 123456789
b = 987654321
m = 1000000007
result = mon_multiply(a, b, m)
print(f"{a} * {b} mod {m} = {result}")


# ===================================================================================
# 19.	Тест Пепина
import sympy
def is_fermat_prime(n):
    # Вычисляем число Ферма
    F_n = 2 ** (2 ** n) + 1
    exponent = (F_n - 1) // 2
    result = pow(3, exponent, F_n)

    # Проверяем, равно ли результат -1 mod F_n
    if result == F_n - 1:
        return True
    else:
        return False


n = int(input("Введите n: "))
if is_fermat_prime(n):
    print(f"F_{n} = {2 ** (2 ** n) + 1} - простое")
else:
    print(f"F_{n} = {2 ** (2 ** n) + 1} - не простое")
