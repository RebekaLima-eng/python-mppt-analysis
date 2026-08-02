import matplotlib.pyplot as plt
import numpy as np #Biblioteca usada para multiplicar a VxI

#Fução para calcular a potência máx
def potmax(tensao, corrente):
    

    tensao = np.array(tensao)
    corrente = np.array(corrente)
    pot = tensao * corrente

    k = 1  # começa no segundo ponto
    direcao = 1  # começa aumentando tensão

    while True:
        k_prox = k + direcao

        # limites
        if k_prox <= 0 or k_prox >= len(tensao):
            break

        delta_p = pot[k_prox] - pot[k]

        if delta_p > 0:
            # continua na mesma direção
            k = k_prox
        else:
            # chegou no pico inverter direção
            direcao *= -1
            k_prox = k + direcao

            if k_prox <= 0 or k_prox >= len(tensao):
                break

            # se inverter e se passar do ponto também (achou MPP)
            if pot[k_prox] < pot[k]:
                break

            k = k_prox


    return tensao[k], corrente[k], pot[k], pot

#Codigo para adicionar os valores da tensão e corrente e gerar um grafico VxI
tensao = []
corrente = []
tensao = list(map(lambda x: float(x), input("Lista com os valores da tensão para a primeira curva I-V:\n").split(",")))
corrente = list(map(lambda x: float(x), input("Lista com os valores da corrente para a primeira curva I-V:\n").split(",")))

#codigo que faz o calculo da potencia 
V_mpp, I_mpp, P_mpp, pot = potmax(tensao, corrente)


print("Ponto de Máxima Potência (P&O):")
print(f"V = {V_mpp} V")
print(f"I = {I_mpp} A")
print(f"P = {P_mpp} W")

#codigo do layout dos graficos
fig, ax = plt.subplots(2, 1) #um grafico com 1 linha e 2 colunas

#Gráfico V x I
ax[0].plot(tensao, corrente, marker='.', linestyle='-', linewidth=2, markerfacecolor='lightgreen', markeredgecolor='lightgreen')
ax[0].set_title("Gráfico da Tensão x Corrente", fontsize=14, fontweight='bold', color='black', loc='center')
ax[0].set_xlabel("Tensão (V)")
ax[0].set_ylabel("Corrente (I)")
ax[0].grid(True, linestyle='--', alpha=0.6)

#Destaca ponto MPP da V X I
ax[0].plot(V_mpp, I_mpp, 'rd')
ax[0].annotate(f"Pmáx\nV={V_mpp:.2f} V\nI={I_mpp:.2f} A", (V_mpp, I_mpp), textcoords="offset points", xytext=(15,15), fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black"), arrowprops=dict(arrowstyle="->"))

#Gráfico V x P
ax[1].plot(tensao, pot, marker='.', linestyle='-', linewidth=2, markerfacecolor='yellow', markeredgecolor='yellow')
ax[1].set_title("Gráfico da Tensão x Potência", fontsize=14, fontweight='bold', color='black', loc='center' )
ax[1].set_xlabel("Tensão (V)")
ax[1].set_ylabel("Potência (W)")
ax[1].grid(True, linestyle='--', alpha=0.6)

#Destaca ponto MPP da V X P
ax[1].plot(V_mpp, P_mpp, 'rd')
ax[1].annotate(  f"Pmáx\nV={V_mpp:.2f} V\nP={P_mpp:.2f} W", (V_mpp, P_mpp), textcoords="offset points", xytext=(15,15), fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black"), arrowprops=dict(arrowstyle="->"))

plt.tight_layout()
plt.show()
