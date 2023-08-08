''' Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos minutos atuais.
Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor'''

# Solicita o valor da conta ao usuário
valor_conta = float(input("Digite o valor da conta a ser paga: "))

# Calcula o valor da gorjeta 10%
gorjeta = valor_conta * 0.10

# Calcula o total a ser pago somando a gorjeta ao valor da conta
total_a_pagar = valor_conta + gorjeta

# Exibe o total a ser pago incluindo a gorjeta
print(f"O total a ser pago, incluindo 10% de gorjeta, é R${total_a_pagar:.2f}")