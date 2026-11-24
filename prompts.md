# 🤖 Prompts utilizados na criação do artigo

Este arquivo documenta os prompts usados com IA generativa (Claude, da Anthropic) para criar o artigo **"CRISPR: Como a Ciência Está Aprendendo a Editar o DNA"** e suas imagens.

---

## 1. Prompt inicial (briefing do projeto)

```
Próximo projeto nosso é:
- Crie um repositório no GitHub com os prompts que você utilizou na criação do projeto;
- Salve nesse mesmo repositório as imagens geradas na construção do seu artigo;
- Coloque o link do seu artigo no README do seu GitHub;
- Envie para gente o link do seu repositório.

CHECKLIST PARA GERAR ARTIGOS DE QUALIDADE
- Assunto: CRISPR: Como a Ciência Está Aprendendo a Editar o DNA
- Título chamativo: headline
- Imagem de capa chamativa
- Blocos do artigo
- Postar o artigo com um call to action
```

---

## 2. Pesquisa e checagem de fatos

```
Pesquise na web as informações mais atuais sobre CRISPR:
- terapias já aprovadas (Casgevy) e datas de aprovação;
- o caso do bebê KJ (primeira terapia CRISPR personalizada);
- terapias CRISPR "in vivo" em análise na FDA em 2026.
Use fontes primárias (FDA, hospitais, revistas científicas, empresas)
e não invente dados.
```

---

## 3. Headline (título chamativo)

```
Crie 5 opções de título chamativo para um artigo de divulgação científica
sobre CRISPR, para público leigo, em português do Brasil.
O título deve despertar curiosidade, mostrar que a tecnologia já é real
e ter no máximo 80 caracteres. Escolha a melhor e explique por quê.
```

**Título escolhido:** *CRISPR: A "Tesoura Genética" Que Já Está Curando Doenças — e Como Ela Funciona*

---

## 4. Estrutura do artigo (blocos)

```
Monte a estrutura de um artigo de ~1.200 palavras sobre
"CRISPR: Como a Ciência Está Aprendendo a Editar o DNA", dividido em blocos:
1. Gancho de abertura
2. O que é CRISPR
3. Origem (sistema imune das bactérias + Nobel 2020)
4. Como funciona em 3 passos
5. Evolução da ferramenta (Cas9, edição de bases, prime editing)
6. Aplicações reais (Casgevy, bebê KJ, terapia in vivo, agricultura)
7. Limites e dilemas éticos
8. Conclusão
9. Call to action
Linguagem simples, com analogias, sem jargão desnecessário.
```

---

## 5. Redação do texto

```
Escreva o artigo completo seguindo a estrutura aprovada, em Markdown,
português do Brasil, tom de divulgação científica.
Use analogias do dia a dia (editor de texto, tesoura, GPS),
uma tabela comparando as 3 gerações de editores,
emojis com moderação nos subtítulos,
e uma lista de referências no final.
Termine com um call to action que convide o leitor a comentar,
compartilhar e seguir o autor.
```

---

## 6. Imagens

As imagens foram geradas pelo Claude por meio de código Python (biblioteca matplotlib), a partir dos prompts abaixo. O script está em [`gerar_imagens.py`](gerar_imagens.py).

### 6.1 Capa — `imagens/01-capa.png`

```
Crie uma imagem de capa 16:9 (1600x900) para o artigo sobre CRISPR.
Estilo: fundo azul-escuro espacial com partículas brilhantes,
uma dupla hélice de DNA em ciano e azul-violeta atravessando a lateral direita,
um trecho da hélice destacado em rosa com uma tesoura amarela acima,
indicando o ponto de corte.
À esquerda: "CRISPR" em letras grandes ciano, o subtítulo
"Como a ciência está aprendendo a editar o DNA" em branco
e uma etiqueta rosa "Biotecnologia • Genética • Saúde".
```

### 6.2 Infográfico — `imagens/02-como-funciona.png`

```
Crie um infográfico horizontal em 3 cartões explicando como o CRISPR-Cas9 edita o DNA:
1. Encontrar (Cas9 + RNA-guia sobre a fita de DNA),
2. Cortar (DNA partido com tesoura e linha tracejada),
3. Reparar (DNA inteiro com as bases editadas em destaque).
Mesma paleta da capa, setas entre os cartões, texto curto em português.
```

### 6.3 Linha do tempo — `imagens/03-linha-do-tempo.png`

```
Crie uma linha do tempo horizontal do CRISPR com os marcos:
1987, 2005, 2012, 2016, 2019, 2020, 2023, 2025 e 2026,
alternando os textos acima e abaixo da linha
e destacando em rosa 2012, 2023 e 2025.
```

### 6.4 Comparativo — `imagens/04-geracoes.png`

```
Crie um card comparativo com as 3 gerações da edição genética:
CRISPR-Cas9 (tesoura), edição de bases (lápis) e prime editing
(processador de texto), mostrando o que cada uma faz e para que serve.
```

---

## 7. Prompts alternativos para geradores de imagem (opcional)

Caso queira gerar uma capa fotorrealista em ferramentas como Midjourney, DALL·E, Leonardo ou Gemini:

```
A glowing DNA double helix floating in a dark blue cosmic laboratory background,
one segment of the helix highlighted in neon pink being precisely cut by
tiny golden molecular scissors, cyan and violet light, scientific yet cinematic,
high detail, 16:9, no text
```

```
Minimalist flat illustration of the CRISPR-Cas9 protein (pink blob)
holding a guide RNA and attaching to a DNA strand, dark navy background,
cyan and yellow accents, clean infographic style, 16:9, no text
```

---

## 8. README e organização do repositório

```
Crie um README.md para o repositório no GitHub com:
título, imagem de capa, link para o artigo publicado,
resumo do artigo, estrutura de pastas, ferramentas usadas
e link para o arquivo de prompts.
```
