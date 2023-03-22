from collections.abc import Iterator, Iterable

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)

class Baralho:
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def __len__(self):
        return len(self._cartas)

    # def __getitem__(self, item):
    #     return self._cartas[item]
    
    def __iter__(self):
        return DeckIterator(self._cartas)
 

class DeckIterator(Iterator):
    def __init__(self, cartas):
        self._cartas = cartas
        self.counter = 0

    def get_card(self, index):
        return self._cartas[index]
        
    def __next__(self):
        if self.counter == len(self._cartas):
            raise StopIteration()

        data = self.get_card(self.counter)
        
        self.counter += 1

        return data


deck = Baralho()

for card in deck:
    print(card)

print(len(deck))