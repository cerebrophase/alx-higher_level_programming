#!/usr/bin/python3
""" module for a singly linked list """


class Node:
    """ defines a node """
    def __init__(self, data, next_node=None):
        """ Initializes the node with instance variables """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ gets data attribute """

        return (self.__data)

    @data.setter
    def data(self, value):
        """ sets data attribute """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self, value):
        """ get next_node attribute
        Returns: next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ set value of next node """

        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

        class SinglyLinkedList:
            """ defines a singly linked list """

            def __init__(self):
                """ Initializes the singly linked list """

                self.head = None

            def sorted_insert(self, value):
                """ sorted insert of the linked list
                Args:
                    value: value on the node
                """

                new_node = Node(value)

                if self.head is None:
                    self.head = new_node
                elif value < self.head.data:
                    new_node.next_node = self.head
                    self.head = new_node

                else:
                    current_node = self.head
                    while current_node.next_node is not None
                    and value > current_node.next_node.data:
                        current_node = current_node.next_node
                    new_node.next_node = current_node.next_node
                    current_node.next_node = new_node

            def __repr__(self):
                """ makes list printable """

                node_list = []
                current_node = self.head
                while current_node is not None:
                    node_list.append(str(current_node.data))
                    current_node = current_node.next_node
                return '\n'.join(node_list)
