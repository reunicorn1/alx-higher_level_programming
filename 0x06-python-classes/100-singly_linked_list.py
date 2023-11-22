#!/usr/bin/python3
"""This is class Node definition"""


class Node:
    """This is a single node object which can be a part of a singly linked
    list.

    There is no Public Attributes for this class.
    The __init__method is initilizing private instance attributes which are
    data and next_node.

    Args:
       data (int): the data stored inside each node.
       next_node (:obj: Node): this can be wither None or a Node referring to
       the next node this current node is pointing to to create the linkage.

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The data attribute has a getter and a setter function.
        as the value of data has to be checked and should always be an integer.
        otherwise, an excpetion is raised.

        Args:
           data (int)

        """
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = data

    @property
    def next_node(self):
        """The next_node attribute has a getter and a setter methods.
        the value of next_node has to be checked to be a Node. otherwise a
        TypeError expcetion is raised.

        Args:
           next_node (:obj: Node)

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if next_node and not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = next_node


"""This is a Singly Linked List class definition"""


class SinglyLinkedList:
    """This class creates objects of Single linked list which contains node
    that are linked together.

    No public attributes are defined currently.

    The __init__ method is initlizing the singly linked list with a private
    instance attribute with is the head of the list.

    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        """The __str__ method here instructs Python to print the singly linked
        list by displaying their data values one node on each line, sorted in
        ascending order.

        """
        strlist = []
        current = self.__head
        while current:
            strlist.append(str(current.data))
            current = current.next_node
        return '\n'.join(strlist)

    def sorted_insert(self, value):
        """This method adds a new Node and insert it into the correct sorted
        position in the list (ascending order).

        Args:
           value (int): the value to be stored inside the ndew node created.

        Returns:
           Nothing.
        """
        new = Node(value)
        if not self.__head or self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current.next_node:
            prev = current
            current = current.next_node
            if current.data > new.data:
                prev.next_node = new
                new.next_node = current
                return
        current.next_node = new
