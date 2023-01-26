# Desafio 040: Média das notas e mensagem de resultado
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input("Qual a segunda nota? "))
media = (nota1 + nota2) / 2
if media > 7:
    print('Com as notas {} e {}, o aluno foi \033[31mAPROVADO\033[m com media {}'.format(nota1, nota2, media))
elif 7 > media >= 5:
    print('Com as notas {} e {}, o aluno tem média {}, logo ele está de \033[31mRECUPERAÇÃO\033[M.'.format(nota1, nota2, media))
else:
    print('Com as notas {} e {}, o aluno fica com média {}, logo está \033[4:31mREPROVADO\033[M.'.format(nota1, nota2, media))
