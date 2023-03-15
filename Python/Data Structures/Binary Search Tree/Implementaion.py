class BinarySearchTree:

    def __init__(self, value):

        self.value = value
        self.left_child = None
        self.right_child = None


    def insert(self, data):
        if self.value is None:

            self.value = data
            return

        if self.value == data:
            return

        if self.value > data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = BinarySearchTree(data)

        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = BinarySearchTree(data)

    def pre_order_search(self):

        print(self.value, end=' ')

        if self.left_child:
            self.left_child.pre_order_search()

        if self.right_child:
            self.right_child.pre_order_search()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value, end=' ')

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value, end=' ')

    def delete(self,data, current):

        if self.value is None:
            print('Tree is empty')
            return

        if data < self.value:
            if self.left_child:
                self.left_child = self.left_child.delete(data, current)
            else:
                print('Given node is not present in the tree')
        elif data > self.value:
            if self.right_child:
                self.right_child = self.right_child.delete(data, current)
            else:
                print('Given node is not present in the tree')

        else:
            if self.left_child is None:
                temp = self.right_child
                if data == current:
                    self.value = temp.value
                    self.right_child = temp.right_child
                    self.left_child = temp.left_child
                    temp = None
                    return

                valor = None
                return temp

            if self.right_child is None:
                temp = self.left_child
                if data == current:
                    self.value = temp.value
                    self.right_child = temp.right_child
                    self.left_child = temp.left_child
                    temp = None
                    return
                valor = None
                return temp

            node = self.right_child
            while node.left_child:
                node = node.left_child

            self.value = node.value
            self.right_child = self.right_child.delete(node.value, current)

        return self

    def min_value(self):
        current = self
        while current.left_child:
            current = current.left_child

        print(f'Min value: {current.value}')

    def max_value(self):
        current = self
        while current.right_child:
            current = current.right_child

        print(f'Max value: {current.value}')


    def find(self,data):

        root = self.value

        if root == data:
            return print('Node is found')

        if data < root:
            if self.left_child:
                self.left_child.find(data)
            else:
                print('Node not Found')
        else:
            if self.right_child:
                self.right_child.find(data)
            else:
                print('Node not Found')

        return self







def count(node):
    if node is None:
        return 0

    return 1 + count(node.left_child) + count(node.right_child)


root = BinarySearchTree(10)
lista = [20,4,30,4,1,5,6]

for i in lista:
    root.insert(i)

if count(root) > 1:
    root.delete(20, root.value)

else:
    print('Cant delete')



