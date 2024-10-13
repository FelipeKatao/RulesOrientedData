import json
import OrientionData


class Store():
    def __init__(self) -> None:
        self.Od = OrientionData.OrientionData()
        self.AddProducts = []
        pass
   
    def AboveProductValue(self,IdProduto):
        Products = self.Od.GetData()
        Regras = self.Od.ProcessRulesOd(self.Od.ReadRule("Regra-teste","Regras"),Products["Produtos"][IdProduto]["Valor"],100,[("{$Quantidade}",Products["Produtos"][IdProduto]["Quantidade"])])
        if len(Regras) >=2:
            self.AddProducts.append(Products["Produtos"][IdProduto]["Produto"])
        print(self.Od.ReturnWorkRules())
        

l =  Store()
LerProdutos = ["0","1","2","3"]
for i in LerProdutos:
    l.AboveProductValue(i)
print(l.AddProducts)
        