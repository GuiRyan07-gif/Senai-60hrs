print('sistema de notas')
print( '...' * 10 )

nome_aluno = input('nome do aluno: ')

n1_port = float (input('nota Portugues: '))
n2_mat  = float (input('nota matemática: '))
n3_ing  = float (input('nota ingles: '))

media = (n1_port + n2_mat + n3_ing)/3
print ('situação do aluno: ')
aprovado = media >= 7
reprovado = media < 5
recuperacao = media >=5 and media < 7
print ()
print (nome_aluno,'aprovado? -', aprovado)
print (nome_aluno,'reprovado? -', reprovado)
print (nome_aluno,'recuperacao? -',recuperacao)
                   
