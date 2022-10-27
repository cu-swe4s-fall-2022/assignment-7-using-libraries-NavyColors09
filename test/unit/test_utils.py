import sys
import os
import unittest
import shutil
import random
import pandas as pd 
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(src_path)
from data_processor import *  # nopep8
from os.path import exists


class TestUtils(unittest.TestCase):
    def test_get_random_matrix(self):
        first_num = random.randrange(1,10) 
        second_num = random.randrange(1,10) 
        #Create a tuple of two integers 
        pair = (first_num, second_num) 
        
        neg_num=-1
        not_an_integer=3.3 
        
        #Returns true if get_random_matrix raises a type error 
        with self.assertRaises(Exception):
            function.get_random_matrix(neg_num,not_an_integer)
        
        #Testing to see if we get the same MxN matrix 
        df = pd.DataFrame(function.get_random_matrix(first_num,second_num)) 
        dimensions = df.shape
        self.assertEqual(pair,dimensions) 
    
    def test_get_file_dimensions(self):
        rows = 150 
        cols = 5 
        pair = (rows,cols)
        
        #Checking dimensions
        dimensions = function.get_file_dimensions(file_name) 
        self.assertEqual(pair,dimensions) 
        
        #Checking to see if the file path exists. This evaluates as true 
        file_exists = os.path.exists('../iris.data')
        self.assertEqual(file_exists,True) 
        
        #Checking to see if the function throws an error. 
        with self.assertRaises(Exception):
            function.get_file_dimensions('does_not_exist.data') 
        
    def test_write_matrix_to_file(self):
        file_path = '../iris.data'
        #Checking for edge cases
        first_num = -1
        second_num = 3.3
        
        #Checking to see if there is an exception raised to two bad inputs 
        with self.assertRaises(Exception):
            function.write_matrix_to_file(first_num,second_num,file_path) 
            
        first_rand= random.randrange(1,10) 
        second_rand = random.randrange(1,10)
        
        #Checking to see if the file name matches
        
        file_name = "out.csv" 
        file_user_input = "out"
        found_file_name = function.write_matrix_to_file(first_rand, second_rand,file_user_input) 
        self.assertEqual(file_name, found_file_name) 
        
        
        
            
            
        
            
        
        
        
        
        
        
        