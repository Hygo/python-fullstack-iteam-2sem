# 🐍 Avaliação — Módulos 03 e 04
**Curso de Capacitação em Desenvolvimento Full Stack — ITEAM**
Professor: Msc. Hygo Sousa De Oliveira

---

## 📌 Sobre esta avaliação

Esta avaliação cobre os dois módulos centrais da primeira metade do curso:

| Módulo | Tema | Questões |
|--------|------|----------|
| **Módulo 03** | Estrutura de Dados | 10 questões |
| **Módulo 04** | Definição e Chamada de Funções | 7 questões |

As questões são de **múltipla escolha (A/B/C/D/E)** e testam tanto
a leitura de código quanto o raciocínio sobre comportamento em runtime.
A progressão vai do básico ao avançado dentro de cada módulo.

---

## 📁 Arquivos

```
modulo-03_04/
├── README.md          ← você está aqui — contexto e instruções
└── template.py        ← copie e preencha as respostas
```

---

## 🎯 Como responder

### 1. Copie o template

Dentro da pasta `modulo-03_04/` da sua cópia do repositório:

```bash
cp template.py mod03-mod04.py
```

### 2. Preencha suas respostas

Abra o arquivo copiado e substitua cada `"?"` pela letra da alternativa
que você considera correta:

```python
# Exemplo
Q01 = "B"   # ← sua resposta aqui
```

### 3. Salve na sua cópia

```bash
git add modulo-03_04/mod03-mod04.py
git commit -m "feat: respostas avaliação módulos 03 e 04"
git push origin main
```

Para a entrega ao professor, veja a seção **Entregar uma atividade** de
[COMO-OBTER-AS-ATIVIDADES.md](../COMO-OBTER-AS-ATIVIDADES.md).

---

## 📚 Conteúdo coberto

### Módulo 03 — Estrutura de Dados

O módulo apresenta as quatro estruturas nativas mais utilizadas em Python
e suas características fundamentais. As questões avaliam:

- **Listas** (`list`): mutabilidade, indexação, slicing, métodos como
  `.sort()` e `.append()`
- **Tuplas** (`tuple`): imutabilidade, desempacotamento, uso como
  chave de dicionário
- **Dicionários** (`dict`): acesso por chave, método `.get()`,
  iteração com `.items()`, aninhamento
- **Conjuntos** (`set`): eliminação de duplicatas, operações de
  união, interseção e diferença
- **Comprehensions**: list comprehension com filtro e transformação,
  dict comprehension

### Módulo 04 — Definição e Chamada de Funções

O módulo aprofunda o uso de funções como blocos reutilizáveis e
objetos de primeira classe. As questões avaliam:

- **Retorno de funções**: `return` explícito vs retorno implícito `None`
- **Parâmetros padrão**: valores default e sua sobrescrita na chamada
- **Escopo**: variáveis locais vs globais, `global` keyword
- **`*args` e `**kwargs`**: captura de argumentos arbitrários
- **Funções de primeira classe**: passagem como argumento (callback)
- **Recursividade**: caso base, pilha de chamadas
- **Docstrings**: acesso via `__doc__`

---

## ⚠️ Regras

- Marque **uma única alternativa** por questão.
- Analise o código **mentalmente** antes de executar — isso treina
  leitura de código, habilidade essencial no dia a dia.
- Não apague as questões do template — apenas substitua o `"?"`.
- Dúvidas? Anote no comentário ao lado da sua resposta.

---

*"In the face of ambiguity, refuse the temptation to guess." — Zen of Python 🐍*
