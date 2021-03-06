import matplotlib.pyplot as plt

n = 20 #aqui especifica-se a variável "n" para usarmos depois. São quantos números que temos dentro da lista (no caso, 20)

lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] #aqui especifica-se a variável "lista" para usarmos depois

x = range (0, n)
y = lista
plt.figure()
plt.title("Lista original")
plt.xlabel("Indices")
plt.ylabel("Numeros")
plt.plot(x,y,'ok')
plt.savefig("fig/bubble-inicio.png")
plt.close()

print("lista original", lista) #lista antes de organizar

a = 0

iter = 0
for i in range (0,n-1,1): #primeira linha da função. Para i com valores entre "(inicial,final,intervalo)" sendo inicial 0, final n-1 (penúltimo no.), intervalo 1 (de 1 em 1)
    for j in range (i+1,n,1): #mesmos comandos da primeira linha da função. Aqui adicionamos em vez de 0 o próprio "i" + 1, que já foi especificado. Isso define a "área" em que nosso programa irá atuar
        iter = iter+1
        x = range (0, n)
        y = lista
        plt.figure()
        plt.title("Grafico da iteraçao {}".format(iter))
        plt.xlabel("Indices")
        plt.ylabel("Numeros")
        plt.plot(x,y,'ok')
        plt.plot(i, lista[i], 'or')
        plt.plot(j, lista[j], 'ob')
        plt.savefig("fig/bubble-it-{}.png".format(iter))
        plt.close()
        if lista[i] > lista[j]: #aqui inicia-se a análise de valores para organizá-los. se o valor que estamos analisando dentro da lista i for maior que o da lista j, o programa executará o que está dentro daqui. Nosso intuito é deixar os números em ordem crescente
            tmp = lista[i] #criado slot temporário com mesmo valor "lista[i]" para não haver perda dos dados 
            lista[i] = lista[j] #substituido valor de lista[i] com lista[j] para que o valor que vem primeiro seja menor
            lista[j] = tmp #substituido valor de lista[j] com tmp (antigo lista[i] para realizar a mudança dos valores. tmp será excluída depois disso.
            a = a+1
            x = range (0, n)
            y = lista
            plt.figure()
            plt.title("Grafico da troca {}".format(a))
            plt.xlabel("Indices")
            plt.ylabel("Numeros")
            plt.plot(x,y,'ok')
            plt.savefig("fig/bubble-troca-{}.png".format(a))
            plt.close()

print("lista em ordem crescente", lista) #lista já está organizada

print("5 menores numeros", lista[0:5])

print("5 maiores numeros", lista[n-5:n])

x = range (0, n)
y = lista
plt.figure()
plt.title("Lista final")
plt.xlabel("Indices")
plt.ylabel("Numeros")
plt.plot(x,y,'ok')
plt.savefig("fig/bubble-final.png")
plt.close()