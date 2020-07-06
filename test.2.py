
################################################################################################################################'
       ####################################################################################################################
                 ########################-----TEST PYTHON PANDAS EXERCISES ------###############################

# faça função que selecione o produto pelo seu valor, utilizando tabela Investimentos
import pandas as pd 

class Localizar:
       def __init__(self):
              pass

       def localizar_preço (self,columns4,valor):
              archive = pd.read_excel(r"Investimentos.xlsx")
              valor_produto = archive[archive[columns4]== valor]
              print(archive.head())
              print(valor_produto)
              print(valor_produto.shape)
              return valor_produto


localizar = Localizar()
localizar.localizar_preço("Preço unitário",200)
