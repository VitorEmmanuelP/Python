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

    def add_beggin(self, data):
        """  Adiciona no comeco da lista  """

        new_node = Node(data)
        if self.head is None:

            new_node.next = new_node
            self.head = new_node
        else:
            current_node = self.head
            new_node.next = current_node
            current_node.next = new_node
            self.head = new_node

    def add_end(self, data):

        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        current_node = self.head

        while current_node.next != self.head:
            current_node = current_node.next

        current_node.next = new_node
        new_node.next = self.head

    def add_after_node(self, data, node_value):
        new_node = Node(data)

        if self.head is None:
            print('Liked list is empty')
            return

        current_node = self.head

        while current_node.next != self.head:
            if current_node.value == node_value:
                break
            current_node = current_node.next

        if current_node.value != node_value:
            print('Node is not present in the Linled List')
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def add_before_node(self, data, node_before):
        new_node = Node(data)

        if self.head is None:
            print('Liked list is empty')
            return

        if self.head.value == node_before:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            tail.next = new_node
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head

        while current_node.next != self.head:
            if current_node.next.value == node_before:
                break

            current_node = current_node.next

        if current_node.value != node_before:
            print('Node is not present in the Linled List')

        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def removing_head(self):

        if self.head is None:
            print('Liked list is empty')

        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            self.head = self.head.next
            tail.next = self.head
            return

    def removing_tail(self):
        if self.head is None:
            print('Liked list is empty')
            return

        current_node = self.head

        while current_node.next.next != self.head:
            current_node = current_node.next

        current_node.next = self.head

    def removing_middle(self, node):

        if self.head is None:
            print('Liked list is empty')
            return

        if node == self.head.value:
            self.removing_head()
            return

        current_node = self.head

        while current_node.next != self.head:
            if node == current_node.next.value:
                break
            current_node = current_node.next

        if current_node.next.value != node:
            print('Node not found')
        else:
            current_node.next = current_node.next.next

    def find(self, valor):

        current_node = self.head

        while current_node is not None:

            if current_node.value == valor:
                break
            current_node = current_node.next

        if current_node is None:
            return 'Lista Vazia ou valor nao esta na lista'
        else:
            return current_node

    def printlist(self):

        if self.head is None:
            return 'Lista Vazia'
        else:
            current_node = self.head

            while current_node.next != self.head:
                print(current_node.value, '-->', end=' ')
                current_node = current_node.next

            print(current_node.value, '-->')


linked = LinkedList()

linked.add_beggin(40)
linked.add_end(50)
linked.add_end(60)
linked.add_end(70)
linked.printlist()

linked.add_before_node(30, 40)
linked.add_after_node(80, 70)
linked.printlist()

linked.removing_head()
linked.printlist()

linked.removing_tail()
linked.printlist()

linked.removing_middle(50)
linked.printlist()

linked.removing_middle(60)
linked.printlist()
