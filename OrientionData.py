import json

class OrientionData:
    def __init__(self) -> None:
        self.AlterValues = []
        self.alter = False
        self.Execute_sub_rule = False
        self.ListRetuns = []
        self.OberverData = []
        pass

    def GetData(self):
        with open('./Dados.json','r') as Data:
            dados = json.load(Data)
        return dados
    
    def ReadRule(self,Regra,caminho):
        with open(f'./{caminho}.Od.json','r') as Data:
            dados = json.load(Data)
        return dados["Regras"][Regra]
    
    def ProcessRulesOd(self,Regras,valor,valor2=None,customValues=[]):
        self.__attachData("#"+str(Regras['nome'])+">"+str(valor)+","+str(valor2)+","+str(customValues))
        varA =Regras["condicao"]
        if(self.Execute_sub_rule == False):
            self.ListRetuns = []
        self.Execute_sub_rule = False

        for i in varA:

            if len(customValues) >=1:
                for z in customValues:
                    self.AlterValues.append(z[0])
                    self.AlterValues.append(z[1])
            Regra_application = str(i['condicao']).replace("{$}",str(valor))

            if(len(self.AlterValues) >=1):
                Regra_application = str(i['condicao']).replace(self.AlterValues[0],str(self.AlterValues[1]))
                self.AlterValues =[]
                self.alter = True

            if valor2!=None and self.alter == False:
                Regra_application = str(i["condicao"]).replace("{$$}",str(valor2)).replace("{$}",str(valor))
            else:
                Regra_application = str(Regra_application).replace("{$$}",str(valor2)).replace("{$}",str(valor))
                self.alter = False
            if '@int' in i["condicao"] :
                Regra_application = Regra_application.replace('@int', '').strip()
                Regra_application = Regra_application.replace(" ",'')
                if ">=" in Regra_application:
                    Regra_application = Regra_application.split(">=")
            
                    if int(Regra_application[0]) >= int(Regra_application[1]):
                
                       if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                       else:
                            self.ListRetuns.append(i["acao"])

                if ">" in Regra_application:
                    Regra_application = Regra_application.split(">")
                    if int(Regra_application[0]) > int(Regra_application[1]):
                       if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                       else:
                            self.ListRetuns.append(i["acao"])
                if "<=" in Regra_application:
                    Regra_application = Regra_application.split("<=")
                    if int(Regra_application[0]) <= int(Regra_application[1]):
                       if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                       else:
                            self.ListRetuns.append(i["acao"])
                if "<" in Regra_application:
                    Regra_application = Regra_application.split("<")
                    if int(Regra_application[0]) < int(Regra_application[1]):
                       if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                       else:
                            self.ListRetuns.append(i["acao"])
                if "==" in Regra_application:
                    Regra_application = Regra_application.split("==")
                    if int(Regra_application[0]) == int(Regra_application[1]):
                       if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                       else:
                            self.ListRetuns.append(i["acao"])
                if "!=" in Regra_application:
                    Regra_application = Regra_application.split("!=")
                    if int(Regra_application[0]) != int(Regra_application[1]):
                       if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                       else:
                            self.ListRetuns.append(i["acao"])
                
            elif '@string' in i:
                Regra_application = Regra_application.replace('@string', '').strip()
                if "==" in Regra_application and Regra_application.split("==")[0].strip() == Regra_application.split("==")[1].strip():
                   if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                   else:
                           self.ListRetuns.append(i["acao"])
                if "!=" in Regra_application and Regra_application.split("!=")[0].strip() != Regra_application.split("!=")[1].strip():
                   if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                   else:
                           self.ListRetuns.append(i["acao"])
                if ">" in Regra_application and Regra_application.split(">")[0].strip() > Regra_application.split(">")[1].strip():
                   if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                   else:
                           self.ListRetuns.append(i["acao"])
                if "<" in Regra_application and Regra_application.split("<")[0].strip() < Regra_application.split("<")[1].strip():
                   if "#" in i["acao"]:
                           self.__CallOtherRules(i["acao"],valor,valor2,customValues)
                   else:
                           self.ListRetuns.append(i["acao"])
        self.__NotifyData(self.ListRetuns)
        return self.ListRetuns 
    
    def __CallOtherRules(self,Regras,valor,valor2=None,customValues=[]):
        RuleDinamic = str(Regras).replace("#",'').split(":")
        self.Execute_sub_rule = True
        self.ProcessRulesOd(self.ReadRule(RuleDinamic[1],RuleDinamic[0]),valor,valor2,customValues)

    def __attachData(self,Values):
         self.OberverData.append([Values])
        
    def __NotifyData(self,Values):
         self.OberverData[len(self.OberverData)-1].append(Values)
        
    def ReturnWorkRules(self):
         return self.OberverData