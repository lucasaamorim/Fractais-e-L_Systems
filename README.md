# Vizualizador de Fractais com L-System

Este projeto em Python é um visualizador de fractais gerados a partir de sistemas formais chamados [L-Systems](https://en.wikipedia.org/wiki/L-system) (ou sistemas de Lindenmayer). O programa utiliza a biblioteca [`turtle`](https://docs.python.org/3/library/turtle.html) para desenhar as representações gráficas dos fractais e oferece também a capacidade de verificar se uma string pertence a um dado L-System.

Feito como projeto da Disciplina de LFA (Linguagens Formais e Autômatatos) do DIMAp/UFRN ministrada pelo professor Dr. Martin Alejandro Musicante.

## Funcionalidades

- **Visualizar fractais:**
  - A partir de um arquivo JSON contendo a definição de um L-System (axioma, regras de produção e ângulo de rotação), o programa desenha o fractal gerado até uma profundidade de recursão especificada.

- **Verificar strings:**
  - Dados uma string e um L-System, o programa verifica se a string é derivada do sistema até uma certa profundidade.

## Estrutura do Arquivo JSON

O arquivo JSON deve conter os seguintes campos:

```json
{
   "rules": {
      "X": [
         "F"
      ],
      "F": [
         "+F[-gF]/2F"
      ]
   },
   "angle": 90,
   "length": 10,
   "lineWidth": 10
}
```

- **`rules`**: Um dicionário onde cada símbolo tem uma regra de produção associada.
- **`angle`**: O ângulo de rotação usado na visualização com a biblioteca `turtle`.
- **`length`**: Profundidade da recursão.
- **`lineWidth`**: Comprimento da linha.
## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/lucasaamorim/Fractais-e-L_Systems.git
   ```

2. Execute o programa:
   ```bash
   python source/main.py caminho/para/arquivo.json
   ```

3. Para verificar se uma string pertence a um L-System:
   ```bash
   python source/main.py caminho/para/arquivo.json --verificar "sua_string" profundidade
   ```

## Exemplos

### Exemplo 1: Visualização de Fractal

Para um arquivo `rules.json` com o seguinte conteúdo:

```json
{
   "rules": {
      "X": [
         "F"
      ],
      "F": [
         "F+F-F"
      ]
   },
   "angle": 90,
   "length": 10,
   "lineWidth": 10
}
```

Ao executar:
```bash
python main.py rules.json
```
O programa gerará o desenho do fractal correspondente na janela do `turtle`.

### Exemplo 2: Verificação de String

Para verificar se a string `F+F-F` pertence ao L-System descrito em `rules.json`, execute:
```bash
python main.py rules.json --verificar "F+F-F" 2
```

O programa retornará:
```
A string pertence ao L-System.
```


---

Aproveite o projeto e explore o fascinante mundo dos fractais com L-Systems!

