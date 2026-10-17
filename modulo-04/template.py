"""
=============================================================
AVALIAÇÃO — Módulo 04: Definição e Chamada de Funções
Curso de Capacitação Full Stack – ITEAM
Professor: Msc. Hygo Sousa De Oliveira

Aluno(a): <SEU NOME COMPLETO>
Data    : <DATA DE ENTREGA>
=============================================================

INSTRUÇÕES:
  1. Substitua cada "?" pela letra da sua resposta (A, B, C, D ou E).
  2. O código e as alternativas de cada questão estão nos comentários,
     logo acima da linha da resposta.
  3. Analise o código mentalmente — evite executar antes de decidir.
  4. Você pode adicionar comentários justificando sua escolha.
  5. Salve este arquivo como modulo-04/respostas.py, na sua cópia
     do repositório do curso.

COMO VERIFICAR O PREENCHIMENTO:
  python respostas.py
=============================================================
"""

# ──────────────────────────────────────────────────────────────
# DEFINIÇÃO E CHAMADA DE FUNÇÕES (7 questões)
# ──────────────────────────────────────────────────────────────

# ------------------------------------------------------------
# Q01 🟢 — Retorno implícito None sem return
#
# def somar(a, b):
#     resultado = a + b
#
# valor = somar(3, 4)
# print(valor)
#
# A) 7
# B) 0
# C) None
# D) TypeError: somar() missing return
# E) NameError: resultado is not defined
# ------------------------------------------------------------
Q01 = "?"


# ------------------------------------------------------------
# Q02 🟢 — Parâmetros com valor padrão (default)
#
# def saudar(nome, mensagem="Olá"):
#     print(f"{mensagem}, {nome}!")
#
# saudar("Ana")
# saudar("Bruno", "Bom dia")
#
# A) "Olá, Ana!" e "Olá, Bruno!"
# B) "Ana, Olá!" e "Bruno, Bom dia!"
# C) "Olá, Ana!" e "Bom dia, Bruno!"
# D) TypeError: saudar() missing 1 required argument
# E) None e None
# ------------------------------------------------------------
Q02 = "?"


# ------------------------------------------------------------
# Q03 🟡 — Escopo de variáveis: local vs global
#
# x = 10
#
# def alterar():
#     x = 99
#     print(x)
#
# alterar()
# print(x)
#
# A) 99 e 99
# B) 10 e 10
# C) 99 e 10
# D) 10 e 99
# E) UnboundLocalError: x referenced before assignment
# ------------------------------------------------------------
Q03 = "?"


# ------------------------------------------------------------
# Q04 🟡 — *args: parâmetros arbitrários
#
# def resumo(*valores):
#     return max(valores) - min(valores)
#
# print(resumo(3, 7, 1, 9, 2))
#
# A) 3
# B) 7
# C) 8
# D) 9
# E) TypeError: max() takes 1 positional argument but 5 were given
# ------------------------------------------------------------
Q04 = "?"


# ------------------------------------------------------------
# Q05 🟡 — Funções de primeira classe: callback
#
# def dobrar(n):
#     return n * 2
#
# def aplicar(funcao, valores):
#     return [funcao(v) for v in valores]
#
# resultado = aplicar(dobrar, [1, 2, 3, 4])
# print(resultado)
#
# A) [1, 2, 3, 4]
# B) [2, 4, 6, 8]
# C) [1, 4, 9, 16]
# D) TypeError: 'function' object is not iterable
# E) 8
# ------------------------------------------------------------
Q05 = "?"


# ------------------------------------------------------------
# Q06 🔴 — Funções recursivas: fatorial
#
# def fatorial(n):
#     if n <= 1:
#         return 1
#     return n * fatorial(n - 1)
#
# print(fatorial(4))
#
# A) 4
# B) 10
# C) 16
# D) 24
# E) RecursionError: maximum recursion depth exceeded
# ------------------------------------------------------------
Q06 = "?"


# ------------------------------------------------------------
# Q07 🔴 — **kwargs + dict comprehension + docstring
#
# def registrar(**dados):
#     """Registra informações arbitrárias de um objeto."""
#     return {k.upper(): v for k, v in dados.items()}
#
# info = registrar(nome="Hygo", cargo="Professor", ativo=True)
# print(info.get("CARGO"))
# print(registrar.__doc__[:10])
#
# A) "Professor" e "Registra i"
# B) "cargo"     e "Registra informações"
# C) None        e "Registra i"
# D) "Professor" e None
# E) KeyError: "CARGO" e "Registra i"
# ------------------------------------------------------------
Q07 = "?"


# ──────────────────────────────────────────────────────────────
# VERIFICADOR AUTOMÁTICO
# Execute este arquivo após preencher todas as respostas.
# Ele vai conferir o formato e avisar se algum campo ficou em branco.
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    respostas = {
        "Q01": Q01, "Q02": Q02, "Q03": Q03, "Q04": Q04, "Q05": Q05,
        "Q06": Q06, "Q07": Q07,
    }

    validas   = set("ABCDE")
    pendentes = [q for q, r in respostas.items() if r == "?"]
    invalidas = [q for q, r in respostas.items() if r != "?" and r not in validas]

    print("=" * 50)
    print("  VERIFICADOR DE RESPOSTAS")
    print("=" * 50)

    if pendentes:
        print(f"\n⚠️  Questões sem resposta ({len(pendentes)}):")
        for q in pendentes:
            print(f"   {q} → ainda '?'")

    if invalidas:
        print(f"\n❌  Respostas inválidas (use apenas A-E):")
        for q in invalidas:
            print(f"   {q} → '{respostas[q]}'")

    respondidas = [q for q, r in respostas.items() if r != "?" and r in validas]
    print(f"\n✅  Respondidas : {len(respondidas)}/7")
    print(f"⚠️   Pendentes   : {len(pendentes)}/7")

    if not pendentes and not invalidas:
        print("\n🎉 Todas as respostas preenchidas! Pronto para enviar.")
    else:
        print("\nComplete as respostas antes de fazer o commit.")
        sys.exit(1)
