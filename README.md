# Prática 3: O Módulo Central e a Resolução de Conflitos Complexos

Este repositório contém o código-base para a terceira etapa da prática de versionamento. O objetivo é demonstrar os impactos da falta de coordenação entre equipes, a dificuldade de revisar "commits monstros" e a resolução de conflitos lógicos no mesmo arquivo.

## 1. Código-Base Inicial

O repositório possui a branch `main` com o arquivo `analisador_dados.py` contendo a seguinte estrutura inicial:

```python
class AnalisadorDados:
    def __init__(self):
        self.historico = []

    def limpar_dados(self, dados_brutos):
        return [d for d in dados_brutos if d is not None]

    def processar_lista_aninhada(self, dados):
        # TODO: Implementar logica para achatar a lista e somar os valores
        pass

    def exibir_resultado(self, resultado):
        print(f"Resultado do processamento: {resultado}")

```

## 2. Preparação do Ambiente Local

A turma será dividida em dois grupos (Grupo A e Grupo B). Todos os alunos devem clonar o repositório e acessar o diretório:

```bash
# Clonar o repositório
git clone <URL_DO_REPOSITORIO>

# Acessar a pasta do projeto
cd <NOME_DA_PASTA>

```

## 3. Execução das Tarefas (Branches Paralelas)

Cada grupo desenvolverá uma solução diferente para o mesmo problema, no mesmo arquivo, sem comunicação prévia.

### Grupo A: Implementação Recursiva

**Objetivo:** Criar um método recursivo no início do arquivo e atualizar o método de processamento.

**Passo 1:** Criar a branch isolada.

```bash
git checkout -b feat/calculo-recursivo

```

**Passo 2:** Alterar o arquivo `analisador_dados.py`. Inserir o método `_calcular_rec` logo abaixo da declaração da classe e atualizar o método `processar_lista_aninhada`.

```python
class AnalisadorDados:
    def _calcular_rec(self, lista):
        total = 0
        for item in lista:
            if isinstance(item, list):
                total += self._calcular_rec(item)
            else:
                total += item
        return total

    def __init__(self):
        self.historico = []

    def limpar_dados(self, dados_brutos):
        return [d for d in dados_brutos if d is not None]

    def processar_lista_aninhada(self, dados):
        dados_limpos = self.limpar_dados(dados)
        return self._calcular_rec(dados_limpos)

    def exibir_resultado(self, resultado):
        print(f"Resultado do processamento: {resultado}")

```

**Passo 3:** Registrar e enviar as alterações.

```bash
git add analisador_dados.py
git commit -m "feat: implementa solucao recursiva para calculo de dados aninhados"
git push origin feat/calculo-recursivo

```

*(Após o push, o Grupo A deve abrir o Pull Request no GitHub e o professor fará o merge imediatamente).*

### Grupo B: Implementação Iterativa

**Objetivo:** Criar um método iterativo no final do arquivo e atualizar o mesmo método de processamento.

**Passo 1:** A partir da `main` original, criar a branch isolada.

```bash
git checkout main
git pull origin main
git checkout -b feat/calculo-iterativo

```

**Passo 2:** Alterar o arquivo `analisador_dados.py`. Inserir o método `_calcular_iter` no final da classe e atualizar o método `processar_lista_aninhada`.

```python
class AnalisadorDados:
    def __init__(self):
        self.historico = []

    def limpar_dados(self, dados_brutos):
        return [d for d in dados_brutos if d is not None]

    def processar_lista_aninhada(self, dados):
        dados_limpos = self.limpar_dados(dados)
        return self._calcular_iter(dados_limpos)

    def exibir_resultado(self, resultado):
        print(f"Resultado do processamento: {resultado}")

    def _calcular_iter(self, lista):
        total = 0
        pilha = list(lista)
        while pilha:
            item = pilha.pop()
            if isinstance(item, list):
                pilha.extend(item)
            else:
                total += item
        return total

```

**Passo 3:** Registrar e enviar as alterações.

```bash
git add analisador_dados.py
git commit -m "feat: adiciona algoritmo iterativo base em pilha"
git push origin feat/calculo-iterativo

```

*(Após o push, o Grupo B deve abrir o Pull Request no GitHub. Ocorrerá um conflito imediato).*

## 4. O Conflito e a Análise

Quando o Grupo B tentar atualizar sua branch local com as alterações já aprovadas do Grupo A na `main`, o Git acusará um conflito.

```bash
# Comando para puxar as atualizações da main para a branch atual do Grupo B
git pull origin main

```

*Saída esperada: `CONFLICT (content): Merge conflict in analisador_dados.py*`

Ao abrir o arquivo no editor, o bloco em conflito será exibido desta forma:

```python
<<<<<<< HEAD
    def processar_lista_aninhada(self, dados):
        dados_limpos = self.limpar_dados(dados)
        return self._calcular_iter(dados_limpos)
=======
    def processar_lista_aninhada(self, dados):
        dados_limpos = self.limpar_dados(dados)
        return self._calcular_rec(dados_limpos)
>>>>>>> main

```

A resolução exigirá que os desenvolvedores leiam o código inserido no topo (pelo Grupo A) e no final (pelo Grupo B), conversem para decidir qual algoritmo será mantido em produção, apaguem as marcações do Git (`<<<<<<<`, `=======`, `>>>>>>>`), apaguem o código redundante e realizem um novo commit de correção.
