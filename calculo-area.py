n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
while True:
      print('[1] Triângulo\n'
            '[2] Quadrado\n'
            '[3] Retângulo\n'
            '[4] Trapézio\n'
            '[5] Círculo\n'
            '[6] Losango\n'
            '[7] Sair do Programa'
            )
      print()
      quest = int(input('Escolha a figura plana que deseja calcular a área: '))
      print(f'Sua escolha: {quest}')
      print()
      if quest == 1:
            n1 = int(input('Digite o valor da base: '))
            n2 = int(input('Digite o valor da altura: '))
            n3 = int(input('Digite o valor do primeiro lado do Triângulo: '))
            n4 = int(input('Digite o valor do segundo lado do Triângulo: '))
            n5 = int(input('Digite o valor do terceiro lado do Triângulo: '))
            val = [n3, n4, n5]
            val.sort()
            soma = val[0] + val[1]
            if n1 in val:
                  if soma > n5:
                        print()
                        print('Triângulo válido')
                        if n3 == n4 and n4 == n5:
                              print('Triângulo Equilátero.')
                        elif n3 == n4 or n3 == n5 or n4 == n5:
                              print('Triângulo Isósceles.')
                        else:
                              print('Triângulo Escaleno.')
                        print()
                        print(f'A área do Triângulo, é igual a: Base X Altura/2')
                        print(f'Desta forma, a área do Triângulo é igual a: {(n1 * n2) / 2}')
                        print()
                  else:
                        print()
                        print('Triângulo inválido.')
                        print()
            else:
                  print()
                  print('Triângulo inválido.')
                  print()
      elif quest == 2:
            n1 = int(input('Digite o lado do quadrado: '))
            print()
            print('A área do Quadrado é igual a: Lado²')
            print(f'Desta forma, a área do Quadrado é igual a: {n1**2}')
            print()
      elif quest == 3:
            n1 = int(input('Digite o valor da base do Retângulo: '))
            n2 = int(input('Digite o valor da altura do Retângulo: '))
            print()
            print('A área do Retângulo é igual a: Base X Altura')
            print(f'Desta forma, a área do Retângulo é igual a: {n1*n2}')
            print()
      elif quest == 4:
            n1 = int(input('Digite o valor da base maior do Trapézio: '))
            n2 = int(input('Digite o valor da base menor do Trapézio: '))
            n3 = int(input('Digite o valor da altura do Trapézio: '))
            print()
            if n1 < n2:
                  print('A base menor, não pode ser maior que a base maior. Insira os valores corretamente.')
                  n1 = int(input('Digite o valor da base maior do Trapézio: '))
                  n2 = int(input('Digite o valor da base menor do Trapézio: '))
                  n3 = int(input('Digite o valor da altura do Trapézio: '))
            print()
            print('A área do Trapézio, é igual a: Base maior + Base menor X altura/2')
            print(f'Desta forma, a área do Trapézio é igual a: {(n1+n2)*n3/2}')
            print()
      elif quest == 5:
            n1 = int(input('Digite o valor do raio da circunferência: '))
            print()
            print('A área do Círculo é igual a: π.raio²\nO perímetro do Círculo é igual a: 2π.raio\nO diâmetro do Círculo é igual a: r.2')
            print(f'Considerando π = 3,1415')
            print()
            print(f'Desta forma, a área do Círculo é igual a: {(n1**2)*3.1415:.2f}\nO perímetro do Círculo é igual a: {3.1415*2*n1:.2f}\nO diâmetro do Círculo é igual a: {n1*2}')
            print()
      elif quest == 6:
            n1 = int(input('Digite o valor da diagonal maior do Losango: '))
            n2 = int(input('Digite o valor da diagonal menor do Losango: '))
            if n1 < n2:
                  print()
                  print('A diagonal menor, não pode ser maior que a diagonal maior. Insira os valores corretamente.')
                  print()
                  n1 = int(input('Digite o valor da diagonal maior do Losango: '))
                  n2 = int(input('Digite o valor da diagonal menor do Losango: '))
                  print()
            print()
            print('A área do Losango é igual a: Diagonal maior X Diagonal menor/2')
            print()
            print(f'Desta forma, a área do Losango é igual a: {(n1*n2)/2}')
            print()
      elif quest == 7:
            print(f'Programa encerrado.')
            break
      elif quest > 7 or quest < 1:
            print(f'Por favor, insira valores somente de 1 a 7')
            print(f'Programa reiniciado.')
            print()
            quest == 0
