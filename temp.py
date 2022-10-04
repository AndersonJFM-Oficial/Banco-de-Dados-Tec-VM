#Feito por Anderson(N°4), Gabriel(N°13) e Luiz(N°22)


def menu_inicial():
  print('Programa para Conversão de Temperaturas')
  print('')
  print('1. Fahrenheit')
  print('2. Celsius')
  print('3. Kelvin')
  print('')

if __name__=='__main__':
  menu_inicial()
  print('')
  escolha = input('Escolha um tipo de temperatura: ')

  if escolha == '1':
    print('')
    print('Escolha para qual temperatura deseja converter')
    print('')
    print('1.Celsius')
    print('2.Kelvin')
    print('')
    escolha = input('Escolha para qual deseja converter: ')

    if escolha == '1':
      print('')
      temp_F = float(input("Informe um valor da escala Fahrenheit: "))
      temp_C = 5 * (temp_F - 32)/9
      print('')
      print('Valor em Celsius:',round(temp_C,3))

      if temp_C<=0:
        print('')
        print("A essa temperatura, a água está no estado sólido")
      elif temp_C>=100:
        print('')
        print("A essa tempera, a água está no estado Gasoso")
      else:
        print('')
        print("A essa temperatura,a água esta no estado Liquido")
    
    elif escolha == '2':
      print('')
      temp_F = float(input("Informe um valor da escala Fahrenheit: "))
      print('')
      temp_K = 5 * (temp_F - 32)/9 + 273.15
      print('')
      print('Valor em Kelvin:',round(temp_K,3))

      if temp_K<=273.15:
        print('')
        print("A essa temperatura, a água está no estado sólido")
      elif temp_K>=373.15:
        print('')
        print("A essa tempera, a água está no estado Gasoso")
      else:
        print('')
        print("A essa temperatura,a água esta no estado Liquido")

    else:
      print('')
      print('Essa opção não consta na lista')
      print('')
    print('')
    print('Programa finalizado!')
    
  elif escolha == '2':
    print('')
    print('Escolha para qual temperatura deseja converter')
    print('')
    print('1.Fahrenheit')
    print('2.Kelvin')
    print('')
    escolha = input('Escolha para qual deseja converter: ')

    if escolha == '1':
      print('')
      temp_C = float(input("Informe um valor da escala Celsius: "))
      print('')
      temp_F = (temp_C * 9)/5 + 32
      print('')
      print('Valor em Fahrenheit:',round(temp_F,3))

      if temp_F<=32:
        print('')
        print("A essa temperatura, a água está no estado sólido")
      elif temp_F>=212:
        print('')
        print("A essa tempera, a água está no estado Gasoso")
      else:
        print('')
        print("A essa temperatura,a água esta no estado Liquido")

    elif escolha == '2':
      print('')
      temp_C = float(input("Informe um valor da escala Celsius: "))
      print('')
      temp_K = temp_C + 273.15
      print('')
      print('Valor em Kelvin:',round(temp_K,3))

      if temp_K<=273.15:
        print('')
        print("A essa temperatura, a água está no estado sólido")
      elif temp_K>=373.15:
        print('')
        print("A essa tempera, a água está no estado Gasoso")
      else:
        print('')
        print("A essa temperatura,a água esta no estado Liquido")

    else:
      print('')
      print('Essa opção não consta na lista')
      print('')
    print('')
    print('Programa finalizado!')
    
  elif escolha == '3':
    print('')
    print('Escolha para qual temperatura deseja converter')
    print('')
    print('1.Celsius')
    print('2.Fahrenheit')
    print('')
    escolha = input('Escolha para qual deseja converter: ')

    if escolha == '1':
      print('')
      temp_K = float(input("Informe um valor da escala Kelvin: "))
      print('')
      temp_C = temp_K - 273.15
      print('')
      print('Valor em Celsius:',round(temp_C,3))

      if temp_C<=0:
        print('')
        print("A essa temperatura, a água está no estado sólido")
      elif temp_C>=100:
        print('')
        print("A essa tempera, a água está no estado Gasoso")
      else:
        print('')
        print("A essa temperatura,a água esta no estado Liquido")

    elif escolha == '2':
      print('')
      temp_K = float(input("Informe um valor da escala Kelvin: "))
      print('')
      temp_F =  (temp_K - 273.15) * 1.8 + 32 
      print('')
      print('Valor em Fahrenheit:',round(temp_F,3))

      if temp_F<=32:
        print('')
        print("A essa temperatura, a água está no estado sólido")
      elif temp_F>=212:
        print('')
        print("A essa tempera, a água está no estado Gasoso")
      else:
        print('')
        print("A essa temperatura,a água esta no estado Liquido")
        
    else:
      print('')
      print('Essa opção não consta na lista')
      print('')
    print('')
    print('Programa finalizado!')

  else:
    print('')
    print('Essa opção não consta na tabela')
    print('')
    print('programa finalizado!')
