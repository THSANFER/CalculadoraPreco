#Dados para o cálcudo do preço do centavo/minuto
preco_tubo=float(input('\nInforme o preço do tubo: '))
duracao_tubo = float(input('\nInforme a duração do tubo: '))

#Cálculo do preço do centavo/minuto
hora_tubo = preco_tubo / (duracao_tubo/2)
min_tubo = hora_tubo/60

#Dados para o cálcudo dos minutos mensais trabalhados
horas_dia = float(input('\nInforme o as horas diárias trabalhadas: '))

#Cálculo dos minutos mensais trabalhados
horas_menasl = horas_dia * 30
minutos_mensal= horas_menasl * 60

#Dados sobre a conta de luz
luz = float(input('\nInforme o valor gasto com energia elétrica: '))

#Cálculo da conta de luz
conta_luz = luz/minutos_mensal

#Dados sobre a o valor salvo
valor_salvo = float(input('\nInforme o valor destinado a manutenções e raparos: '))

#Cálculo da reserva
reserva = valor_salvo / minutos_mensal

#Cálculo do valor do custo do laser
custo_laser = min_tubo + conta_luz + reserva

#---------------------------------------------------------------------------------------
#Dados do tamanho da placa
tamanho_placa = float(input('\nInforme o tamanho da placa (m^2): '))

#Dados de preço da placa
preco_placa = float(input('\nInforme o preço da placa (R$): '))

#Cálculo do preço do metro
preco_metro = preco_placa / tamanho_placa

#Cálculo do preço do centímetro
preco_cent = preco_metro / 10000

#---------------------------------------------------------------------------------------------
#Dados do tamanho da placa utilizada
tamanho_total = float(input('\nInforme o tamanho total utilizado de placa (cm^2): '))

#Cálculo do Valor Total do material
valor_material = tamanho_total * preco_cent

#---------------------------------------------------------------------------------------------
#Dados do tempo trabalhado
min_trabalho = float(input('\nInforme o tempo utilizado na produção do produto (min): '))

#Cálculo do Valor do Laser
valor_laser = custo_laser * min_trabalho

#---------------------------------------------------------------------------------------------
#Cálculo da soma total do valor do produto
total = valor_material + valor_laser

#---------------------------------------------------------------------------------------------
#Dados do lucro
valor_lucro = float(input('\nInforme o lucro desejado (%): '))
lucro = valor_lucro / 100

#----------------------------------------------------------------------------------------------
#Cálculo da soma total com o lucro
total_lucro = total + (total * lucro)

#----------------------------------------------------------------------------------------------
#Impressões
print('\nPreço da hora do tubo:',hora_tubo)

print('\nPreço do minuto do tubo:',min_tubo)

print('\nValor do minuto mensal:',minutos_mensal)

print('\nValor da conta de luz: ', conta_luz)

print('\nValor de reserva: ', reserva)

print('\nValor total do custo do laser: ', custo_laser)

print('\nValor do preço do centímetro da placa: ',preco_cent)

print('\nValor total do material: ', valor_material)

print('\nValor total do laser: ', valor_laser)

print('\nValor total do produto: ', total)

print('\nValor total do produto com o lucro: ',total_lucro)
