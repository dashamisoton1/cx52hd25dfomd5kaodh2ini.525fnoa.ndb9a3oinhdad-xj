import json


class DB():
    def Destroy(self,__Name):
        __DB = self._FR()
        if __Name in __DB.keys():
            __DB.pop(__Name)
            return self._FW(__DB)
        return False
    def Define(self,__Name,__Value):
        __DB = self._FR()
        __DB[str(__Name)] = __Value
        return self._FW(__DB)
    def Get(self,__Name:str) -> dict:
        __DB = self._FR()
        if __Name in __DB.keys():
            return __DB[__Name]
        return False
    def GetAll(self):
        return self._FR()
    def Reset(self):
        return self._FW({})
    def AddToList(self,__Name,__Value):
        __DB = self._FR()
        if __Name in __DB.keys():
            __DB[__Name].append(__Value)
            return self._FW(__DB)
        return False
    def DelFromList(self,__Name,__Value):
        __DB = self._FR()
        if __Name in __DB.keys():
            if __Value in __DB[__Name]:
                __DB[__Name].remove(__Value)
                return self._FW(__DB)
        return False
    

    def AddToDict(self,__Name,__Key,__Value):
        __DB = self._FR()
        if __Name in __DB.keys():
            __DB[__Name][__Key] = __Value
            return self._FW(__DB)
        return False
    
    def DelFromDict(self,__Name,__Key):
        __DB = self._FR()
        if __Name in __DB.keys():
            __DB[__Name].pop(__Key)
            return self._FW(__DB)
        return False
    
    def Clear(self,__Name):
        __DB = self._FR()
        if __Name in __DB.keys():
            __DB[__Name] = None
            return self._FW(__DB)
        return False

















    def _FR(self) -> dict:
        with open(self.path, 'r', encoding="utf-8") as __f:
                return json.loads(__f.read())

    def _FW(self, __j) -> bool:
        try:
            with open(self.path, 'w', encoding="utf-8") as __f:
                __f.write(json.dumps(__j))
                return 1
        except:return 0


    def __init__(self, __path):
        if not ".DataBase" in __path:
            self.path = __path + ".DataBase"
        else:
            self.path = __path
        try:
            open(self.path, "r").close()
        except:
            open(self.path, "w").write("{}")


        
