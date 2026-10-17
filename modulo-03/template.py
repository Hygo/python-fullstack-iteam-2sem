"""
=============================================================
AVALIAÇÃO — Módulo 03: Estrutura de Dados
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
  5. Salve este arquivo como modulo-03/respostas.py, na sua cópia
     do repositório do curso.

COMO VERIFICAR O PREENCHIMENTO:
  python respostas.py
=============================================================
"""

# ──────────────────────────────────────────────────────────────
# ESTRUTURA DE DADOS (10 questões)
# ──────────────────────────────────────────────────────────────

# ------------------------------------------------------------
# Q01 🟢 — Listas: indexação negativa
#
# frutas = ["maçã", "banana", "uva", "laranja"]
# frutas[1] = "abacaxi"
# frutas.append("manga")
# print(frutas[-2])
#
# A) "laranja"
# B) "manga"
# C) "abacaxi"
# D) IndexError: list index out of range
# E) "uva"
# ------------------------------------------------------------
Q01 = "?"   # substitua pela sua resposta


# ------------------------------------------------------------
# Q02 🟢 — Tuplas: imutabilidade
#
# coordenadas = (10, 20, 30)
# coordenadas[1] = 99
# print(coordenadas)
#
# A) ValueError: índice inválido
# B) (10, 20, 30) — atribuição ignorada silenciosamente
# C) (10, 99, 30)
# D) (99, 20, 30) — índice 0 é substituído
# E) TypeError: 'tuple' object does not support item assignment
# ------------------------------------------------------------
Q02 = "?"


# ------------------------------------------------------------
# Q03 🟢 — Dicionários: método .get() com valor padrão
#
# aluno = {"nome": "Ana", "nota": 9.5, "ativo": True}
# resultado = aluno.get("email", "não informado")
# print(resultado)
#
# A) KeyError: 'email'
# B) False
# C) "não informado"
# D) "Ana"
# E) None
# ------------------------------------------------------------
Q03 = "?"


# ------------------------------------------------------------
# Q04 🟢 — Conjuntos: eliminação de duplicatas
#
# numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# unicos = set(numeros)
# print(len(unicos))
#
# A) 10
# B) 7
# C) 9
# D) 8
# E) 6
# ------------------------------------------------------------
Q04 = "?"


# ------------------------------------------------------------
# Q05 🟡 — Listas: .sort(reverse=True) + slicing
#
# notas = [7.0, 8.5, 6.0, 9.0, 5.5]
# notas.sort(reverse=True)
# print(notas[1:3])
#
# A) [8.5, 6.0]
# B) [7.0, 6.0]
# C) [8.5, 7.0]
# D) [9.0, 8.5]
# E) [9.0, 7.0]
# ------------------------------------------------------------
Q05 = "?"


# ------------------------------------------------------------
# Q06 🟡 — Dicionários: list comprehension com .items()
#
# estoque = {"caneta": 10, "caderno": 5, "borracha": 0}
# vazios = [item for item, qtd in estoque.items() if qtd == 0]
# print(vazios)
#
# A) ["caneta", "caderno"]
# B) ["borracha"]
# C) {"borracha": 0}
# D) [0]
# E) []
# ------------------------------------------------------------
Q06 = "?"


# ------------------------------------------------------------
# Q07 🟡 — Conjuntos: operação .difference()
#
# turma_a = {"Ana", "Bruno", "Carlos", "Diana"}
# turma_b = {"Carlos", "Diana", "Eduardo", "Flávia"}
# resultado = turma_a.difference(turma_b)
# print(len(resultado))
#
# A) 6
# B) 4
# C) 3
# D) 8
# E) 2
# ------------------------------------------------------------
Q07 = "?"


# ------------------------------------------------------------
# Q08 🟡 — List comprehension com filtro e transformação
#
# numeros = range(1, 11)
# pares_quadrados = [n ** 2 for n in numeros if n % 2 == 0]
# print(pares_quadrados)
#
# A) [4, 8, 12, 16, 20]
# B) [2, 4, 6, 8, 10]
# C) [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# D) [4, 16, 36, 64, 100]
# E) [1, 9, 25, 49, 81]
# ------------------------------------------------------------
Q08 = "?"


# ------------------------------------------------------------
# Q09 🔴 — Dicionários aninhados + sum() + generator
#
# empresa = {
#     "nome": "ITEAM",
#     "equipes": {
#         "backend":  {"lider": "Hygo", "membros": 5},
#         "frontend": {"lider": "Ana",  "membros": 3},
#     }
# }
# total = sum(
#     equipe["membros"]
#     for equipe in empresa["equipes"].values()
# )
# print(total)
#
# A) 8
# B) {"backend": 5, "frontend": 3}
# C) 2
# D) 5
# E) 3
# ------------------------------------------------------------
Q09 = "?"


# ------------------------------------------------------------
# Q10 🔴 — Estruturas combinadas: lista de dicts + comprehension
#
# dados = [
#     {"nome": "Carlos",  "notas": [7, 8, 9]},
#     {"nome": "Beatriz", "notas": [10, 10, 9]},
#     {"nome": "Diego",   "notas": [5, 6, 4]},
# ]
# aprovados = [
#     d["nome"]
#     for d in dados
#     if sum(d["notas"]) / len(d["notas"]) >= 7.0
# ]
# print(aprovados)
#
# A) []
# B) ["Beatriz"]
# C) ["Carlos", "Diego"]
# D) ["Carlos", "Beatriz"]
# E) ["Carlos", "Beatriz", "Diego"]
# ------------------------------------------------------------
Q10 = "?"


# ──────────────────────────────────────────────────────────────
# VERIFICADOR AUTOMÁTICO
# Execute este arquivo após preencher todas as respostas.
# Ele vai conferir o formato e avisar se algum campo ficou em branco.
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    respostas = {
        "Q01": Q01, "Q02": Q02, "Q03": Q03, "Q04": Q04, "Q05": Q05,
        "Q06": Q06, "Q07": Q07, "Q08": Q08, "Q09": Q09, "Q10": Q10,
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
    print(f"\n✅  Respondidas : {len(respondidas)}/10")
    print(f"⚠️   Pendentes   : {len(pendentes)}/10")

    if not pendentes and not invalidas:
        print("\n🎉 Todas as respostas preenchidas! Pronto para enviar.")
    else:
        print("\nComplete as respostas antes de fazer o commit.")
        sys.exit(1)
