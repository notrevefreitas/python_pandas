
################################################################################################################################'
       ####################################################################################################################
                 ########################-----TEST PYTHON PANDAS EXERCISES ------###############################

import pandas as pd 


#Selecione 5 primeiro items FirstName,LastName da tabela do excel Dados 



def selecione_columns( columns1, columns2):
       

       archive = pd.read_excel(r"Dados.xlsx", sheet_name="Plan1")
       coluna_seleciona = archive.loc[1:6,[columns1, columns2]] 
       print(coluna_seleciona)
       return coluna_seleciona
          

             
selecione_columns("FirstName","LastName")

