
#importar a biblioteca math e a biblioteca para limpar o cosole
import math
import os

#define as variaveis utilizadas posteriormente
total_quedas = 0
entrada = 0
total_meteoros = 0 
primeiro_quad = 0
segundo_quad  = 0
terceiro_quad = 0
quarto_quad  = 0
quedas_casa  = 0
centro = 0


#função que converte as coordenadas polares em valores de x e y 
def conversaoPolar(dist, ang): 
      global x_meteoro, y_meteoro 
      x_meteoro = int(dist * math.cos(ang))    
      y_meteoro = int(dist * math.sin(ang))
#função que analisa o centro do terreno       
def centro_terreno(p1_terreno_x , p1_terreno_y , p2_terreno_x , p2_terreno_y):
    global centro_x , centro_y
    centro_x = (p1_terreno_x + p2_terreno_x) / 2
    centro_y = (p1_terreno_y + p2_terreno_y) / 2

#menu inicial 
print("-:: Sistema para Análise de Chuva de Meteoros ::-\n" )
print("-::Primeiramente defina os valores para o perímetro do terreno::-\n")

#coleta de variáveis para definição do terreno 
ponto1_terreno_x = float(input("Digite o valor x do canto superior esquerdo do terreno: "))
ponto1_terreno_y = float(input("Digite o valor y do canto superior esquerdo do terreno: "))
ponto2_terreno_x = float(input("Digite o valor x do canto inferior direito do terreno: "))
ponto2_terreno_y = float(input("Digite o valor y do canto inferior direito do terreno: "))

print("\n-::Digite os valores para o perímetro da casa::-\n")

#coleta variáveis para a definição do a area da casa
ponto1_casa_x = float(input("Digite o valor x do canto superior esquerdo do casa: "))
ponto1_casa_y = float(input("Digite o valor y do canto superior esquerdo do casa: "))
ponto2_casa_x = float(input("Digite o valor x do canto inferior direito do casa: "))
ponto2_casa_y = float(input("Digite o valor y do canto inferior direito do casa: "))


#realiza a verificação se o tamanho da casa é valido
while ponto1_casa_x < ponto1_terreno_x or ponto2_casa_x > ponto2_terreno_x:
  print("\nValores inválidos para a casa.\n")
  print("-::Digite novamente os valores do terreno::-\n")
  ponto1_terreno_x = float(input("Digite o valor x do canto superior direito do terreno: "))
  ponto1_terreno_y = float(input("Digite o valor y do canto superior direito do terreno: "))
  ponto2_terreno_x = float(input("Digite o valor x do canto inferior direito do terreno: "))
  ponto2_terreno_y = float(input("Digite o valor y do canto inferior esquerdo do terreno: "))
  print("\n-::Digite novamente os valores da casa::-\n")
  ponto1_casa_x = float(input("Digite o valor x do canto superior direito do casa: "))
  ponto1_casa_y = float(input("Digite o valor y do canto superior direito do casa: "))
  ponto2_casa_x = float(input("Digite o valor x do canto inferior direito do casa: "))
  ponto2_casa_y = float(input("Digite o valor y do canto inferior esquerdo do casa: "))


#caso for valido dê continuidade ao programa
while entrada != 3:
  os.system('clear')
  #cria um segundo menu para coleta de informações do usuário 
  print("\n-:: Sistema para Análise de Chuva de Meteoros ::-\n")
  print("1. Processar registros de chuva de meteoros")
  print("2. Apresentar estatísticas")
  print("3. Sair\n")
  #coleta a informação do que o usuário deseja, validando-a
  entrada = int(input("Opção: "))
  while (entrada != 1) and (entrada != 2) and (entrada != 3):
    entrada = int(input("Opção, inválida, tente novamente: "))
  
  
  while entrada != 3:
    if entrada == 623:
      # para coleta de mais de uma informação, cria-se esse clone do menu
      print("-:: Sistema para Análise de Chuva de Meteoros ::-")
      print("1. Processar registros de chuva de meteoros")
      print("2. Apresentar estatísticas")
      print("3. Sair\n")
      entrada = int(input("Opção: "))
      #valida se a entrada é valida ou não 
      while (entrada != 1) and (entrada != 2) and (entrada != 3):
        entrada = int(input("Opção, inválida, tente novamente: "))
  
    elif entrada == 1:
      #coleta de dados da queda do meteoro 
      dist = float(input("Digite a distância do meteoro: "))  
      #realiza a verificação se a distancia possui valor valido, ou seja, positiva
      while dist < 0: 
        print("Digite um valor válido para a distância.")
        dist = float(input("Digite a distância do meteoro novamente: ")) 
      #caso for valida, colete o angulo da queda  
      ang = float(input("Digite o ângulo de queda: "))
      #converta os dados coletados utilizando a função criada anteriormente
      conversaoPolar(dist, ang)
      #registra o número total de quedas
      total_meteoros += 1
      #realiza a verificação se o meteoro esta dentro dos parametros do tereno
      if (ponto1_terreno_x <= x_meteoro and x_meteoro <= ponto2_terreno_x) and (y_meteoro <= ponto1_terreno_y and ponto2_terreno_y <= y_meteoro):
        #caso esteja no terreno, primeiramente verifique se atingiu a casa
        if (ponto1_casa_x <= x_meteoro and x_meteoro <= ponto2_casa_x) and (y_meteoro <= ponto1_casa_y and ponto2_casa_y <= y_meteoro):
          print("O meteoro atingiu a casa. ")
          #realiza uma soma a variável vazia, para coleta de dados
          quedas_casa =+ 1 
        else:  
          #como o meteoro ja esta no terreno, e nao esta na casa, apenas demonstre que atingiu o terreno
          print("O meteoro atingiu o terreno. ")
        #contabiliza os dados obtidos para realização dos calculos  
        total_quedas += 1 
        #para verificar em qual quadrante o meteoro caiu, utiliza a função 'centro_terreno'
        centro_terreno(ponto1_terreno_x, ponto1_terreno_y, ponto2_terreno_x, ponto2_terreno_y)
        if x_meteoro > centro_x and y_meteoro > centro_y:
          primeiro_quad += 1 
        elif x_meteoro < centro_x and y_meteoro > centro_y:
          segundo_quad += 1 
        elif x_meteoro < centro_x and y_meteoro < centro_y:
          terceiro_quad += 1 
        elif x_meteoro == centro_x  and y_meteoro == centro_y:
          centro += 1
        else:
          quarto_quad =+ 1
      #caso nenhuma das verificações for verdadeira, logo o meteoro nao atingiu o terreno.
      else:
        print("Não atingiu o terreno")
      #limpa o console
      os.system('clear')
      #retorna para o menu, possibilitando que o usuario realize uma nova verificação  
      entrada = 623
    #demonstra todos os dados analisados até o momento
    elif entrada == 2:
      if total_quedas == 0: 
        print("\n Nenhum meteoro atingiu o terreno")
      else:
        #demonstra em porcentagem, quais quadrantes foram mais atingidos, dos meteoros que atingiram o terreno
        porcent_1 = (primeiro_quad / total_quedas)  * 100  
        porcent_2 = (segundo_quad / total_quedas) * 100
        porcent_3 = (terceiro_quad / total_quedas) * 100
        porcent_4 = (quarto_quad / total_quedas) * 100
        porcent_centro = (centro / total_quedas) * 100
        porcent_terreno = (total_quedas / total_meteoros) *100
      #demonstra os dados obtidos
      print(f"-->Dados coletados:\nTotal de meteoros coletados: {total_meteoros} \nNúmero de quedas: {total_quedas} \nNúmero de meteoros que atingiu a casa: {quedas_casa:} \nPorcentagem que atingiu o terreno: {porcent_terreno:.2f}%\n \n-->Dados dos quadrantes: \n1º: {porcent_1:.2f}% \n2º:  {porcent_2:.2f}% \n3º {porcent_3:.2f}%  \n4º: {porcent_4:.2f}% \ncentro: {porcent_centro:.2f}%")
      #retorna o usuário para o menu
      entrada = 623 
#uma vez que o usuário desejar o programa se encerra
print("-::Obrigado por utilizar nosso sistema::-")