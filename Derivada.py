# Derivada numérica pelo método das diferenças centrais
delta_x = 0.001
x = 1

# Função f(x) = x^3
def f(x):
    return x**3

# Derivada numérica (diferença central)
derivada = (f(x + delta_x) - f(x - delta_x)) / (2 * delta_x)

# Derivada real: f'(x) = 3x^2
derivada_real = 3 * x**2

print(f"Derivada Numérica: {derivada:.6f}")
print(f"Derivada Real:     {derivada_real:.6f}")





# Definição da função
def f(x):
    return x**3

# Parâmetros
x = 1
h = 0.1

# Segunda derivada numérica (diferença central)
segunda_derivada = (f(x + h) - 2*f(x) + f(x - h)) / (h**2)

# Segunda derivada real (analítica)
segunda_derivada_real = 6 * x

print(f"Segunda derivada numérica: {segunda_derivada:.6f}")
print(f"Segunda derivada real:     {segunda_derivada_real:.6f}")
