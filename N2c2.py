
#Gerador de senha
# w = write (escreve)
# r = read (ler)
# a - acrescent (acrescentar) 

#cabeçalho
print("                         Atividade N2C - Calculo de Salarios")
print("\nintegrantes do grupo: \nJuliana Marques \nTyago Wiesner \nLuis Augusto \nMatheus Costa")


#Abertura dos arquivos
arquivosal = open('salario.txt')
arquivocalc = open('calculos.txt', 'w')

arquivocalc.write("Bruto       AliqINSS     Val.INSS      Base          AliqIR       Val.IR       Liquido \n")

for linha in arquivosal:
    salario = float(linha)
    #Calculo INSS
    if salario >= 0.0 and salario <= 1751.81:
        inss = 0.08
        porcentagem = salario * inss
        salariotab1 = salario - porcentagem
    elif salario >= 1751.82 and salario <= 2919.72:
        inss = 0.09
        porcentagem = salario * inss
        salariotab1 = salario - porcentagem
    elif salario >= 2919.73 and salario <= 5839.45 :
        inss = 0.11
        porcentagem = salario * 0.11
        salariotab1 = salario - porcentagem
    elif salario > 5839.45:
        inss = 0.0
        porcentagem = 0.0
        salariotab1 = salario - 642.34

        #Calculo imposto de renda
    #Calculo IR
    if salariotab1 >= 0.0 and salariotab1 <= 1903.98:
        ir = 0.0
        porcentagem2 = 0.0
        if porcentagem2 <= 10.0:
            porcentagem2 = 0.0
        salariotab2 = salariotab1 - porcentagem2
    elif salariotab1 >= 1903.99 and salariotab1 <= 2826.65 :
        ir = 0.075
        porcentagem2 = salariotab1 * ir - 142.80
        if porcentagem2 <= 10.0:
            porcentagem2 = 0.0
        salariotab2 = salariotab1 - porcentagem2
    elif salariotab1 >= 2826.66  and salariotab1 <= 3751.05:
        ir = 0.15
        porcentagem2 = salariotab1 * ir - 354.80
        if porcentagem2 <= 10.0:
            porcentagem2 = 0.0
        salariotab2 = salariotab1 - porcentagem2
    elif salariotab1 >= 3751.06 and salariotab1 <= 4664.68:
        ir = 0.225
        porcentagem2 = salariotab1 * ir - 636.13
        if porcentagem2 <= 10.0:
            porcentagem2 = 0.0
        salariotab2 = salariotab1 - porcentagem2
    elif salariotab1 > 4664.68:
        ir = 0.227
        porcentagem2 = salariotab1 * ir - 869.36
        if porcentagem2 <= 10.0:
            porcentagem2 = 0.0
        salariotab2 = salariotab1 - porcentagem2

    arquivocalc.write("{:.2f}    {:.2f}            {:.2f}       {:.2f}      {:.2f}        {:.2f}            {:.2f} \n "
                      .format(salario, inss, porcentagem, salariotab1, ir, porcentagem2, salariotab2,))

arquivocalc.close()
arquivosal.close()