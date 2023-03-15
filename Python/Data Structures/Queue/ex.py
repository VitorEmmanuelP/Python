from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    print(simqueue.items)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        print('passou',simqueue.items)

        simqueue.dequeue()
        print('morreu',simqueue.items)
    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],1))


print(']-----------------------------')
def BatataQuente(list,rodadas):
    pessoal = []
    for nomes in list:
        pessoal.append(nomes)
    print(pessoal)
    while len(pessoal) > 1 :
        for i in range(rodadas):
            pessoal.insert(len(pessoal),pessoal[0])
            pessoal.pop(0)
            print('passou', pessoal)
        pessoal.pop(0)

        print('morreu',pessoal)

    return pessoal

print(BatataQuente(["Bill","David","Susan","Jane","Kent","Brad"],1))