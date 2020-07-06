import pandas as pd



################################################################################################################################'
       ####################################################################################################################
                 ########################-----TEST PYTHON PANDAS EXERCISES ------###############################

# faca uma class com três função uma maior valor e a outra menor valor e ultima função media dos valores da tabela investimentos "coluna Preços unitário "

class Verificar:
       def __init__(self):
              pass

       def maior (self,columns):
              archive = pd.read_excel(r"Investimentos.xlsx")

              print(archive.head(10))
              # media 
              print(archive[columns].max())


       def menor (self,columns):

              archive = pd.read_excel(r"Investimentos.xlsx")

              print(archive.head(10))
              # menor 
              print(archive[columns].min())

       def media(self,columns ):      
              archive = pd.read_excel(r"Investimentos.xlsx")

              print(archive.head(10))

              # maximo
              print(archive[columns].mean())


verificar= Verificar()
verificar.maior("Preço unitário")
verificar.media("Preço unitário")
verificar.menor("Preço unitário")



