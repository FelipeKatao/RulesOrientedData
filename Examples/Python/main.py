import json
import OrientionData


class Loja():
    def __init__(self) -> None:
        self.Od = OrientionData.OrientionData()
        self.ProdutosAdicionados = []
        pass
   
    def AdicionarProdutosValorAcima(self,IdProduto):
        Produtos = self.Od.GetData()
        Regras = self.Od.ProcessRulesOd(self.Od.ReadRule("Regra-teste","Regras"),Produtos["Produtos"][IdProduto]["Valor"],100,[("{$Quantidade}",Produtos["Produtos"][IdProduto]["Quantidade"])])
        if len(Regras) >=2:
            self.ProdutosAdicionados.append(Produtos["Produtos"][IdProduto]["Produto"])
        print(self.Od.ReturnWorkRules())
        

l =  Loja()
LerProdutos = ["0","1","2","3"]
for i in LerProdutos:
    l.AdicionarProdutosValorAcima(i)
print(l.ProdutosAdicionados)
        