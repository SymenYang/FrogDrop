import json



class FrogProtocol() :
    def loadFromString(inputString) :
        dicData = json.loads(inputString)

        if not ('Method' in dicData and \
                'Sender' in dicData and \
                'SenderPort' in dicData and \
                'Reciver' in dicData and \
                'ReciverPort' in dicData and \
                'URI' in dicData) :
            return {"error" : "don't have basic component"}
        
        if dicData['Method'] == 'PUT' :
            if not ('UserName' in dicData and \
                    'Size' in dicData) :
                return {"error" : "don't have PUT component"}
            else:
                return dicData

        if dicData['Method'] == 'REC' :
            if not ('UserName' in dicData) :
                return {"error" : "don't have REC component"}
            else:
                return dicData

        if dicData['Method'] == 'GET' :
            if not ('StartPos' in dicData and \
                    'Size' in dicData) :
                return {"error" : "don't have GET component"}
            else:
                return dicData

        if dicData['Method'] == 'TRS' :
            if not ('File' in dicData and \
                    'Size' in dicData) :
                return {"error" : "don't have TRS component"}
            else:
                return dicData
        
        return {"error" : "Methods dosen't accepted"}

    def getTrsString(inputDic) :
        ret = {}
        acceptList = ['Method','Sender','SenderPort','Reciver','ReciverPort','URI','UserName','Size','StartPos','File']
        for item in acceptList:
            if item in inputDic:
                ret[item] = inputDic[item]
        return json.dumps(ret)