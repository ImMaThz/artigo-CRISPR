"""Gera as imagens do artigo 'CRISPR: Como a Ciência Está Aprendendo a Editar o DNA'."""
import math, os, random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Polygon
import numpy as np

OUT = "imagens"
os.makedirs(OUT, exist_ok=True)

BG = "#0B1020"
CYAN = "#2EE6D6"
MAG = "#FF4F9A"
YEL = "#FFD447"
WHITE = "#F4F6FB"
GREY = "#8A93B2"
plt.rcParams["font.family"] = "DejaVu Sans"


def helix(ax, x0, x1, amp, yc, turns, lw=3, alpha=1.0, highlight=None):
    x = np.linspace(x0, x1, 900)
    ph = (x - x0) / (x1 - x0) * turns * 2 * math.pi
    y1 = yc + amp * np.sin(ph)
    y2 = yc + amp * np.sin(ph + math.pi)
    # pares de bases
    for i in range(0, 900, 18):
        c = MAG if (highlight and highlight[0] <= x[i] <= highlight[1]) else GREY
        a = 0.95 if c == MAG else 0.35 * alpha
        ax.plot([x[i], x[i]], [y1[i], y2[i]], color=c, lw=lw * 0.6, alpha=a, solid_capstyle="round")
    ax.plot(x, y1, color=CYAN, lw=lw, alpha=alpha)
    ax.plot(x, y2, color="#6C7BFF", lw=lw, alpha=alpha)


# ---------- 1) CAPA ----------
fig = plt.figure(figsize=(16, 9), dpi=100)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 9); ax.axis("off")
fig.patch.set_facecolor(BG)
random.seed(4)
for _ in range(160):
    ax.add_patch(Circle((random.uniform(0, 16), random.uniform(0, 9)), random.uniform(0.01, 0.05),
                        color=random.choice([CYAN, WHITE, MAG]), alpha=random.uniform(0.15, 0.6)))
# brilho
for r, a in [(4.5, 0.05), (3.2, 0.07), (2.0, 0.09)]:
    ax.add_patch(Circle((11.2, 3.0), r, color=MAG, alpha=a, lw=0))
helix(ax, 6.5, 16.5, 1.15, 3.0, 3.2, lw=5, highlight=(10.6, 11.8))
# "tesoura" estilizada no ponto de corte
ax.plot([10.9, 11.5], [5.0, 4.15], color=YEL, lw=6, solid_capstyle="round")
ax.plot([11.5, 10.9], [5.0, 4.15], color=YEL, lw=6, solid_capstyle="round")
ax.add_patch(Circle((10.8, 5.12), 0.22, fill=False, ec=YEL, lw=5))
ax.add_patch(Circle((11.6, 5.12), 0.22, fill=False, ec=YEL, lw=5))
ax.text(0.8, 7.35, "CRISPR", color=CYAN, fontsize=88, fontweight="bold")
ax.text(0.85, 6.45, "Como a ciência está aprendendo", color=WHITE, fontsize=34, fontweight="bold")
ax.text(0.85, 5.75, "a editar o DNA", color=WHITE, fontsize=34, fontweight="bold")
ax.text(0.88, 5.0, "Da defesa das bactérias às primeiras curas genéticas", color=GREY, fontsize=19)
ax.add_patch(FancyBboxPatch((0.85, 0.65), 4.6, 0.6, boxstyle="round,pad=0.05,rounding_size=0.25",
                            fc=MAG, ec="none"))
ax.text(3.15, 0.95, "Biotecnologia • Genética • Saúde", color=WHITE, fontsize=15,
        fontweight="bold", ha="center", va="center")
fig.savefig(f"{OUT}/01-capa.png", facecolor=BG)
plt.close(fig)


# ---------- 2) COMO FUNCIONA (3 passos) ----------
fig = plt.figure(figsize=(16, 8), dpi=100)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 8); ax.axis("off")
fig.patch.set_facecolor(BG)
ax.text(8, 7.3, "Como o CRISPR-Cas9 edita o DNA", color=WHITE, fontsize=30, fontweight="bold", ha="center")
titles = ["1. Encontrar", "2. Cortar", "3. Reparar"]
descs = ["O RNA-guia (gRNA) leva a Cas9\naté a sequência exata no genoma",
         "A Cas9 corta as duas fitas\ndo DNA naquele ponto",
         "A célula conserta o corte:\no gene é desligado ou corrigido"]
for i in range(3):
    cx = 2.9 + i * 5.1
    ax.add_patch(FancyBboxPatch((cx - 2.3, 0.6), 4.6, 5.9, boxstyle="round,pad=0.05,rounding_size=0.3",
                                fc="#141B33", ec=CYAN if i != 1 else MAG, lw=2))
    ax.text(cx, 5.9, titles[i], color=CYAN if i != 1 else MAG, fontsize=24, fontweight="bold", ha="center")
    ax.text(cx, 1.3, descs[i], color=WHITE, fontsize=14, ha="center", va="center", linespacing=1.5)
    # DNA simples (duas fitas)
    y_top, y_bot = 3.9, 3.1
    if i == 1:
        for (a, b) in [(cx - 1.9, cx - 0.12), (cx + 0.12, cx + 1.9)]:
            ax.plot([a, b], [y_top, y_top], color=CYAN, lw=5)
            ax.plot([a, b], [y_bot, y_bot], color="#6C7BFF", lw=5)
        ax.plot([cx, cx], [2.8, 4.25], color=YEL, lw=3, ls="--")
        ax.text(cx, 4.45, "✂", color=YEL, fontsize=30, ha="center")
    else:
        ax.plot([cx - 1.9, cx + 1.9], [y_top, y_top], color=CYAN, lw=5)
        ax.plot([cx - 1.9, cx + 1.9], [y_bot, y_bot], color="#6C7BFF", lw=5)
    for k in np.linspace(cx - 1.8, cx + 1.8, 13):
        if i == 1 and abs(k - cx) < 0.2:
            continue
        hl = (i == 2 and abs(k - cx) < 0.35)
        ax.plot([k, k], [y_bot, y_top], color=YEL if hl else GREY, lw=3 if hl else 2, alpha=1 if hl else 0.5)
    if i == 0:
        ax.add_patch(FancyBboxPatch((cx - 1.0, 4.15), 2.0, 0.75, boxstyle="round,pad=0.05,rounding_size=0.35",
                                    fc=MAG, ec="none", alpha=0.9))
        ax.text(cx, 4.52, "Cas9 + gRNA", color=WHITE, fontsize=13, fontweight="bold", ha="center", va="center")
    if i == 2:
        ax.text(cx, 4.4, "DNA editado", color=YEL, fontsize=14, fontweight="bold", ha="center")
    if i < 2:
        ax.add_patch(FancyArrowPatch((cx + 2.35, 3.5), (cx + 2.75, 3.5), arrowstyle="-|>", mutation_scale=28,
                                     color=WHITE))
fig.savefig(f"{OUT}/02-como-funciona.png", facecolor=BG)
plt.close(fig)


# ---------- 3) LINHA DO TEMPO ----------
events = [("1987", "Sequências repetidas\nsão vistas em E. coli"),
          ("2005", "Descobre-se que são\nmemória imunológica\ndas bactérias"),
          ("2012", "Doudna e Charpentier\ntransformam o sistema\nem ferramenta"),
          ("2016", "Edição de bases\n(sem cortar as\nduas fitas)"),
          ("2019", "Prime editing:\n'buscar e substituir'"),
          ("2020", "Prêmio Nobel\nde Química"),
          ("2023", "Casgevy: 1ª terapia\nCRISPR aprovada\n(Reino Unido e EUA)"),
          ("2025", "Bebê KJ: 1ª terapia\nCRISPR personalizada"),
          ("2026", "1ª terapia CRISPR\n'dentro do corpo' sob\nrevisão no FDA")]
fig = plt.figure(figsize=(18, 7), dpi=100)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 18); ax.set_ylim(0, 7); ax.axis("off")
fig.patch.set_facecolor(BG)
ax.text(9, 6.35, "Linha do tempo do CRISPR", color=WHITE, fontsize=30, fontweight="bold", ha="center")
ax.plot([0.8, 17.2], [3.5, 3.5], color=CYAN, lw=4)
xs = np.linspace(1.3, 16.7, len(events))
for j, (x, (yr, txt)) in enumerate(zip(xs, events)):
    up = j % 2 == 0
    col = MAG if yr in ("2012", "2023", "2025") else CYAN
    ax.add_patch(Circle((x, 3.5), 0.18, color=col, zorder=3))
    ax.plot([x, x], [3.5, 4.2 if up else 2.8], color=col, lw=2)
    ax.text(x, 4.35 if up else 2.65, yr, color=col, fontsize=18, fontweight="bold",
            ha="center", va="bottom" if up else "top")
    ax.text(x, 4.95 if up else 2.05, txt, color=WHITE, fontsize=11.5, ha="center",
            va="bottom" if up else "top", linespacing=1.35)
fig.savefig(f"{OUT}/03-linha-do-tempo.png", facecolor=BG)
plt.close(fig)


# ---------- 4) GERAÇÕES DA FERRAMENTA ----------
fig = plt.figure(figsize=(16, 8), dpi=100)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 16); ax.set_ylim(0, 8); ax.axis("off")
fig.patch.set_facecolor(BG)
ax.text(8, 7.3, "As 3 gerações da edição genética", color=WHITE, fontsize=30, fontweight="bold", ha="center")
cards = [("Tesoura", "CRISPR-Cas9", "Corta as duas fitas\ndo DNA", "Ótimo para DESLIGAR\num gene", CYAN),
         ("Lápis", "Edição de bases", "Troca UMA letra\n(ex.: C→T, A→G)", "Corrige mutações\npontuais", YEL),
         ("Processador\nde texto", "Prime editing", "Busca e reescreve\num trecho", "Inserções, deleções\ne trocas maiores", MAG)]
for i, (met, nome, como, uso, col) in enumerate(cards):
    cx = 2.9 + i * 5.1
    ax.add_patch(FancyBboxPatch((cx - 2.3, 0.6), 4.6, 5.9, boxstyle="round,pad=0.05,rounding_size=0.3",
                                fc="#141B33", ec=col, lw=2.5))
    ax.text(cx, 5.75, f"{i+1}ª geração", color=GREY, fontsize=14, ha="center")
    ax.text(cx, 5.05, nome, color=col, fontsize=23, fontweight="bold", ha="center")
    ax.text(cx, 4.0, f"Metáfora: {met.replace(chr(10), ' ')}", color=WHITE, fontsize=13, ha="center", style="italic")
    ax.text(cx, 2.95, como, color=WHITE, fontsize=15, ha="center", va="center", linespacing=1.4)
    ax.plot([cx - 1.6, cx + 1.6], [2.15, 2.15], color=col, lw=1, alpha=0.5)
    ax.text(cx, 1.4, uso, color=col, fontsize=14, ha="center", va="center", fontweight="bold", linespacing=1.4)
fig.savefig(f"{OUT}/04-geracoes.png", facecolor=BG)
plt.close(fig)
print("ok")
