class Node:

    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__previous = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, data):
        self.__value = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, data):
        self.__next = data

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, data):
        self.__previous = data


class DoublyLL:

    def __init__(self):

        self.head = None

    def __empty_insert(self, data):

        new_node = Node(data)
        new_node.next = new_node
        new_node.previous = new_node
        self.head = new_node

    def begin_insert(self, data):

        if self.head is None:
            self.__empty_insert(data)
            return

        new_node = Node(data)

        new_node.next = self.head
        new_node.previous = self.head.previous
        self.head.previous.next = new_node
        self.head.previous = new_node
        self.head = new_node

    def end_insert(self, data):

        if self.head is None:
            self.__empty_insert(data)

        else:
            new_node = Node(data)
            current_node = self.head

            while current_node.next != self.head:
                current_node = current_node.next

            new_node.previous = current_node
            new_node.next = self.head
            current_node.next = new_node
            self.head.previous = new_node
            # print(f'valor: {new_node.value}, next= {new_node.next.value}, prev: {new_node.previous.value}')

            if current_node == self.head:
                current_node.previous = new_node

    def before_insert(self, value, node):

        new_node = Node(value)

        if self.head is None:
            print('The list is empty')
            return

        current_node = self.head

        while current_node.next != self.head:
            if current_node.value == node:
                break
            current_node = current_node.next

        if current_node.value != node :
            print('Given Node is not present in the list')
            return

        new_node.next = current_node
        new_node.previous = current_node.previous
        current_node.previous.next = new_node
        current_node.previous = new_node
        if current_node == self.head:
            self.head = new_node

    def after_insert(self, value, node):

        new_node = Node(value)

        if self.head is None:
            print('The list is empty')
        else:
            current_node = self.head

            while current_node.next != self.head:
                if current_node.value == node:
                    break

                current_node = current_node.next

            if current_node.value != node:
                print('Given Node is not present in the list')
                return

            new_node.next = current_node.next
            new_node.previous = current_node
            current_node.next.previous = new_node
            current_node.next = new_node

    def removing_head(self):

        if self.head is None:
            print('The list is empty')
            return

        if self.head.next == self.head:
            self.head = None
            print('List is empty after deleting the node!')

        else:
            self.head.next.previous = self.head.previous
            self.head.previous.next = self.head.next
            self.head = self.head.next

    def removing_tail(self):

        if self.head is None:
            print('The list is empty')
            return
        if self.head.next == self.head:
            self.head = None
            print('List is empty after deleting the node!')
            return
        else:
            self.head.previous = self.head.previous.previous
            self.head.previous.next = self.head

    def removing_middle(self, node):

        if self.head is None:
            print('The list is empty')
            return

        current_node = self.head

        while current_node.next != self.head:
            if current_node.value == node:
                break
            current_node = current_node.next

        if current_node == self.head:
            self.removing_head()

        elif current_node.next == self.head:
            self.removing_tail()
        else:
            current_node.next.previous = current_node.previous
            current_node.previous.next = current_node.next

    def print_ll(self):

        if self.head is None:
            return 'Lista Vazia'
        else:
            current_node = self.head

            while current_node.next != self.head:
                print(current_node.value, '-->', end=' ')
                current_node = current_node.next

            print(current_node.value, '-->')

    def print_ll_reverser(self):
        if self.head is None:
            print('List empty')
        else:
            current_node = self.head
            print(current_node.previous.value)
            while current_node.previous != self.head:
                print(current_node.value, '-->', end=' ')
                current_node = current_node.previous
                if current_node.previous == self.head:
                    break
            print(current_node.value, '-->', end=' ')

    def find(self, node):

        if self.head is None:
            print('List empty')
            return
        current_node = self.head

        while current_node.next != self.head:

            if current_node.value == node:
                break
            current_node = current_node.next

        if current_node.value != node:
            print("Node not found")
            return

        self.__print_node_status(current_node)

        return current_node

    def __print_node_status(self, node):

        next = node.next.value
        previous = node.previous.value

        print(f'next:{next}, prev:{previous}')


linked = DoublyLL()
linked.begin_insert(10)
linked.end_insert(20)
linked.end_insert(30)
linked.end_insert(40)
# linked.end_insert(50)
# linked.end_insert(6000)
#

linked.before_insert(60,10)

linked.after_insert(365,40)



linked.removing_head()
linked.removing_tail()
linked.print_ll()

linked.removing_middle(40)

linked.print_ll()
linked.find(20)



# linked.print_ll_reverser()

# print('')
# linked.removing_middle(60)
# linked.print_ll()
# print('')
# linked.removing_tail()
# linked.print_ll()
# print('')
# linked.removing_head()
# linked.print_ll()
# print('')