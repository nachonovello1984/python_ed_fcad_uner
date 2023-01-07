import unittest
import random

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
    def test_getitem_should_raise_exception1(self):
        try:
            linked_list = LinkedList()
            print(linked_list[4])

            self.fail("__getitem__() tiene que arrojar una excepción cuando se intenta acceder a una posición que no existe.")
            
        except Exception as exc:
            self.assertTrue(True, "Siempre debería llegar aquí")
            
    def test_getitem_should_raise_exception2(self):
        try:
            linked_list = LinkedList()
            linked_list.append(1)    
            print(linked_list[4])

            self.fail("__getitem__() tiene que arrojar una excepción cuando se intenta acceder a una posición que no existe.")
            
        except Exception as exc:
            self.assertTrue(True, "Siempre debería llegar aquí")
        
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
    
    ###################
    ###################
    ## __setitem__() ##
    ###################
    ###################
    def test_setitem_should_raise_exception1(self):
        try:
            linked_list = LinkedList()
            linked_list[4] = 0
            self.fail("__setitem__() tiene que arrojar una excepción cuando se intenta insertar un elemento en una posición que no existe.")
        except Exception as exc:
            self.assertTrue(True, "Siempre debería llegar aquí")
            
    def test_setitem_should_raise_exception2(self):
        try:
            linked_list = LinkedList()
            linked_list.append(1)
            linked_list[4] = 0
            self.fail("__setitem__() tiene que arrojar una excepción cuando se intenta insertar un elemento en una posición que no existe.")
        except Exception as exc:
            self.assertTrue(True, "Siempre debería llegar aquí")
    
    def test_setitem_should_change_value(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        
        linked_list[0] = 0
        
        self.assertEqual(linked_list[0],
                          0, 
                          "__setitem__() tiene que establecer el valor en la posición indicada.")
        
    def test_setitem_should_change_value_with_negative_index(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        
        linked_list[-1] = 0
        
        self.assertEqual(linked_list[len(linked_list) - 1],
                          0, 
                          "__setitem__() tiene que establecer el valor en la posición indicada.")
        
    ###################
    ###################
    ## __delitem__() ##
    ###################
    ###################
    def test_delitem_should_raise_exception1(self):
        try:
            linked_list = LinkedList()

            del linked_list[4]
            
            self.fail("__delitem__() tiene que arrojar una excepción cuando se intenta eliminar un elemento en una posición que no existe.")
            
        except Exception as exc:
            self.assertTrue(True, "Siempre debería llegar aquí.")
            
    def test_delitem_should_raise_exception2(self):
        try:
            linked_list = LinkedList()
            linked_list.append(1)
            
            del linked_list[4]
            
            self.fail("__delitem__() tiene que arrojar una excepción cuando se intenta eliminar un elemento en una posición que no existe.")
            
        except Exception as exc:
            self.assertTrue(True, "Siempre debería llegar aquí.")
    
    def test_delitem_should_remove_first_element(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        
        del linked_list[0]
        
        self.assertEqual(linked_list[0],
                          2, 
                          "__delitem__() tiene que elimiinar el elemento en la posición indicada.")
        
    def test_delitem_should_remove_middle_element(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        
        index = len(linked_list) //2
        
        expected = linked_list[index + 1]
        
        del linked_list[index]
        
        self.assertEqual(linked_list[index],
                          expected, 
                          "__delitem__() tiene que elimiinar el elemento en la posición indicada.")
        
    def test_delitem_should_remove_last_element(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        
        del linked_list[len(linked_list) - 1]
        
        self.assertEqual(linked_list[len(linked_list) - 1],
                          2, 
                          "__delitem__() tiene que elimiinar el elemento en la posición indicada.")
        
    def test_delitem_should_remove_with_negative_index(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        
        del linked_list[-1]
        
        self.assertEqual(linked_list[len(linked_list) - 1],
                          2, 
                          "__delitem__() tiene que elimiinar el elemento en la posición indicada.")

    ################
    ################
    ## __iter__() ##
    ################
    ################
    
    def test_iter(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        
        iter = linked_list.__iter__()
        self.assertEquals(iter.__next__(), 1, "__iter__() no funciona como se esperaba (1).")
        self.assertEquals(iter.__next__(), 2, "__iter__() no funciona como se esperaba (2).")
        self.assertEquals(iter.__next__(), 3, "__iter__() no funciona como se esperaba (3).")

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
