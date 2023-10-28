L = [3, 5, 4] ; L = L.sort()
# sort nie zwraca listy, wiec L, po drugim przypisaniu staje sie None

x, y = 1, 2, 3
# jest za malo zmiennych dostarczonych, powinno byc tyle zmiennych po lewej ile wartosci jest podanych po prawej

X = 1, 2, 3 ; X[1] = 4
# tuple jest niezmienna, wiec nie mozna do niej nic przypisac po utworzeniu

X = [1, 2, 3] ; X[3] = 4
# przypisanie X[3] wychodzi indeksem poza zasieg

X = "abc" ; X.append("d")
# string nie ma metody append

L = list(map(pow, range(8)))
# pow wymaga dwoch argumentow