import matplotlib.pyplot as plt

# Função já definida:
def Regra_Extremidade_Esquerda(a = 0, b = 0, c = 0, d = 0, e = 0, f = 0,
                                x_i = 0, x_f = 0, passo = 0,
                                plot = False, Salvar_png = False, dpi = 1200,
                                Salvar_pdf = False, Diretorio = '\content\\'):

    intervalo = []
    for i in range(int((x_f - x_i)/passo)):
        intervalo.append(x_i + i*passo)

    fxi = []
    ci_fxi = []
    for i in range(len(intervalo)):
        x = intervalo[i]
        f_x_i = a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f
        ci_fxi.append(f_x_i*passo)
        fxi.append(f_x_i)

    somatoria = sum(ci_fxi)

    integral_xi = (a/6)*x_i**6 + (b/5)*x_i**5 + (c/4)*x_i**4 + (d/3)*x_i**3 + (e/2)*x_i**2 + f*x_i
    integral_xf = (a/6)*x_f**6 + (b/5)*x_f**5 + (c/4)*x_f**4 + (d/3)*x_f**3 + (e/2)*x_f**2 + f*x_f
    integral_analitica = integral_xf - integral_xi

    dicionario = {
        'Intervalo': intervalo,
        'f(x)': fxi,
        'Integral Numérica': somatoria,
        'Integral Analítica': integral_analitica}

    if plot:
        plt.figure(figsize=(10,6))
        plt.plot(intervalo, fxi, 'b',
                 label = rf'$f (x) = {a}x^5 + {b}x^4 + {c}x^3 + {d}x^2 + {e}x + {f}$')

        for i in range(len(intervalo)):
            x0 = intervalo[i]
            plt.bar(x0, fxi[i], width=passo, align='edge',
                    color='orange', edgecolor='black', alpha=0.5)

        plt.title('Integração Numérica - Regra da Extremidade Esquerda')
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.legend()
        if Salvar_png:
            plt.savefig(Diretorio + 'integracao_extremidade_esquerda.png', dpi = dpi)
        elif Salvar_pdf:
            plt.savefig(Diretorio + 'integracao_extremidade_esquerda.pdf')
        plt.show()

    return dicionario


# --- Para f(x) = x³ ---
resultado = Regra_Extremidade_Esquerda(
    c = 1,
    x_i = 0,
    x_f = 2,
    passo = 0.1,
    plot = True
)

print("Integral Numérica =", resultado["Integral Numérica"])
print("Integral Analítica =", resultado["Integral Analítica"])
