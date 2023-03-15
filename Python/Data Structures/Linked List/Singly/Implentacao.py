class Node:

    def __init__(self, valor):
        self.__value = valor
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, valor):
        self.__value = valor

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node


class LinkedList:

    def __init__(self):
        self.head = None

    def add_begining(self, data):
        """  Adiciona no comeco da lista  """

        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        currentnode = self.head

        while currentnode.next is not None:
            currentnode = currentnode.next

        currentnode.next = new_node

    def add_after_node(self, data, node_value):

        current_node = self.head
        while current_node is not None:
            if current_node.value == node_value:
                break
            current_node = current_node.next

        if current_node is None:
            print('Node is not present in the Linled List')
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def add_before_node(self,data,node_before):
        if self.head is None:
            print('Liked list is empty')
            return

        if self.head.value == data:
            node = Node(data)
            node.next = self.head
            self.head = node
            return

        current_node = self.head

        while current_node.next is not None:
            if current_node.next.value == node_before:
                break

            current_node = current_node.next

        if current_node is None:
            print('Node is not present in the Linled List')

        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def removing_head(self):

        if self.head is None:
            print('Liked list is empty')

        else:
            self.head = self.head.next

    def removing_tail(self):
        if self.head is None:
            print('Liked list is empty')
            return
        elif self.head.next is None:
            self.head= None

        current_node = self.head

        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def removing_middle(self,node):

        if self.head is None:
            print('Liked list is empty')
            return
        if node == self.head.value:
            self.removing_beggin()
            return

        current_node = self.head

        while current_node.next is not None:
            if node == current_node.next.value:
                break
            current_node = current_node.next

        if current_node.next is None:
            print('Node not found')
        else:
            current_node.next = current_node.next.next

    def find(self, valor):

        currentnode = self.head

        while currentnode is not None:
            if currentnode.value == valor:
                break
            currentnode = currentnode.next

        if currentnode is None:
            return 'Lista Vazia ou valor nao esta na lista'
        else:
            return currentnode

    def printlist(self):

        if self.head is None:
            return 'Lista Vazia'
        else:
            n = self.head
            while n is not None:
                print(n.value, '-->', end=' ')
                n = n.next


linked = LinkedList()

linked.insert(10)
linked.insert(20)

linked.add_begining(50)

linked.add_after_node(60,10)
linked.add_before_node(50,10)

linked.insert('Vitor')
linked.add_before_node('Emmanuel','Vitor')

linked.removing_beggin()

linked.removing_end()
linked.removing_end()
# linked.removing_middle(60)
linked.printlist()
