import numpy as np 
import pandas as pd 

#This file contains a class that has functions used in the main driver 
class function: 
    def get_random_matrix(num_rows, num_columns):
        while True:
            try:
                num_rows = int(num_rows)
                num_columns = int(num_columns)
                
                if num_rows > 0 and num_columns > 0: 
                    matrix = np.random.rand(num_rows,num_columns) 
                    return matrix 
            except ValueError as e:
                print (e)

        return matrix 

    def get_file_dimensions(file_name):
        data_frame = pd.read_csv(file_name,header=None) 
        return data_frame.shape 

    def write_matrix_to_file(num_rows, num_columns, file_name):
        matrix = get_random_matrix(num_rows,num_columns) 
        pd.DataFrame(matrix).to_csv(file_name+".csv")
        #data_frame.to_csv(file_name+'.csv', sep=',')
        return None 
