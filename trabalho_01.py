"""
    Atividade 1
    Disciplina: Lógica e Programação de Computadores IBMEC
    Nome: Lucas Trogo
    Matrícula: ----------
    ----- Exercício 3 -----
        INICIO
        leia fib
        term1 := 0, term2 := 1
        enquanto term1 <= fib, ... n faça
            imprima term1
            fibo := term1 + term2
            term1 := term2
            term2 := fibo
        FIM
"""


def exerc_04(fib):
    """Return non-recursive fibonacci sequence"""
    fib_term = [0] * (fib + 1)
    fib_term[0] = 0
    fib_term[1] = 1
    for i in range(2, fib + 1):
        fib_term[i] = fib_term[i - 1] + fib_term[i - 2]
    return fib_term[i]


def exerc_05(fib):
    """Return recursive fibonacci sequence"""
    if fib <= 1:
        return fib
    return exerc_05(fib - 1) + exerc_05(fib - 2)


def main():
    """Main aplication"""
    exerc_04(20)
    exerc_05(20)


if __name__ == "__main__":
    main()
