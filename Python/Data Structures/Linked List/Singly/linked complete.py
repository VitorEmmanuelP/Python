# A linked list in programming terms is an Abstract Data Type that acts as a linear collection of data elements
# organised as a collection of nodes that contains information about what that node contains and then a link to
# another node. This can take two main forms of a singly linked list, which has only one direction of
# links between nodes, or a doubly-linked list, which can be linked to both the next and last item in the list.
# The benefit of this over a regular array or list is that elements can be easily inserted and removed without the
# need of changing the index of all other items and the memory used to store the linked list does not need to be
# because the data does not have to be stored contiguously. However, we can’t access items in constant time (O(1))
# we could in an array as looking up an item in the list has a linear time complexity (O(n)).

# This data structure can be useful when:

# You want to insert items easily in between other items
# The size of the total collection is unknown
# You don’t need random access when searching for items
# There is no concern about memory usage for storing the data
