import unittest
import random

import sys
sys.path.append("C:\\Archivos Versionados\\github\\python-ed-fcad-uner")

from data_structures import LinkedList



class LinkedListTest(unittest.TestCase):

    ################
    ################
    ## __len__()  ##
    ################
    ################
    def test_len_should_return_zero(self):
        self.assertEqual(
            len(LinkedList()), 0, "Si la lista está vacía la __len__() debería retornar 0.")

    def test_len_should_return_gt_zero(self):
        linked_list = LinkedList()
        cantidad_esperada = 3

        for _ in range(0, cantidad_esperada, 1):
            linked_list.append(random.randint(1, 100))

        self.assertEqual(len(linked_list),
                          cantidad_esperada,
                          f"Si la lista tiene {cantidad_esperada} elementos len() debería responder {cantidad_esperada}.")

    def test_len_should_return_random_len(self):
        linked_list = LinkedList()
        cantidad_esperada = random.randint(1, 100)

        for _ in range(0, cantidad_esperada, 1):
            linked_list.append(random.randint(1, 100))

        self.assertEqual(len(linked_list),
                          cantidad_esperada,
                          f"Si la lista tiene {cantidad_esperada} elementos len() debería responder {cantidad_esperada}.")

    ################
    ################
    ## __str__()  ##
    ################
    ################
    def test_str_should_return_empty(self):
        self.assertEqual(str(LinkedList()),
                          "LinkedList()",
                          "Si la lista está vacía __str__() debería devolver 'LinkedList()'.")

    def test_str_should_return_not_empty(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(str(linked_list),
                          "LinkedList(1, 2, 3)",
                          "Si la lista tiene como elementos 1, 2, 3 __str__() debería devolver 'LinkedList(1, 2, 3).'")

    ####################
    ####################
    ## __contains__() ##
    ####################
    ####################
    def test_contains_should_return_true(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        self.assertTrue(3 in linked_list,
                        "Si la lista tiene como elementos 1, 2, 3; 3 in linked_list debería devolver True.")

    def test_contains_should_return_false(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)

        self.assertFalse(4 in linked_list,
                         "Si la lista tiene como elementos 1, 2, 3; 4 in linked_list debería devolver False.")
        
    ###################
    ###################
    ## __getitem__() ##
    ###################
    ###################
    def test_getitem_should_raise_exception(self):
        linked_list = LinkedList()
        self.assertRaises(type(Exception()), 
                          linked_list.__getitem__, 
                          1, 
                          "__getitem__() tiene que arrojar una excepción cuando se intenta acceder a una posición que no existe.")
        
    def test_getitem_should_return_first(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list[0],
                          1, 
                          "Método __getitem__() debe retornar el elemento en la primera posición cuando el índice es 0.")
        
    def test_getitem_should_return_last(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list[-1],
                          3, 
                          "Método __getitem__() debe retornar el elemento en la última posición cuando el índice es -1.")
    

    ################
    ################
    ## is_empty() ##
    ################
    ################
    def test_is_empty_should_return_true(self):
        self.assertTrue(LinkedList().is_empty(),
                        "Si la lista no tiene elementos entonces lista.is_empty() debería retornar True.")

    def test_is_empty_should_return_false(self):
        linked_list = LinkedList()
        linked_list.append(100)
        self.assertFalse(linked_list.is_empty(),
                         "Si la lista tiene elementos entonces lista.is_empty() debería retornar False.")
        

    ################
    ################
    ##  append()  ##
    ################
    ################
    def test_append_should_add_element_at_last(self):
        linked_list = LinkedList()
        linked_list.append(100)
        self.assertEqual(linked_list[len(linked_list) - 1], 100, "El elemento se debería insertar al final de la estructura.")
