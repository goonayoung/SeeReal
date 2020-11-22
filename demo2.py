import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

class similarity:
    def list_to_vector(self, reqList):
        tfidf_vect_simple = TfidfVectorizer()
        reqVector = tfidf_vect_simple.fit_transform(reqList)
        return reqVector
    
    def vector_to_dense(self, reqVector):
        denseMatrix = reqVector.todense()
        return denseMatrix
    
    def checkSim(self, denseMatrix):
        vect1 = np.array(denseMatrix[0]).reshape(-1,)
        vect2 = np.array(denseMatrix[1]).reshape(-1,)
        dot_product = np.dot(vect1, vect2)
        #print("dot = ", dot_product)
        l2_norm = (np.sqrt(sum(np.square(vect1))) * np.sqrt(sum(np.square(vect2))))
        #print("norm = ", l2_norm)
        similarity = dot_product / l2_norm  
        return similarity
    def result(self, reqArr):
        print("lll")

class internal_similarity(similarity):
    def result(self, reqArr):
        super().result(reqArr)
        df = pd.read_excel('C:/Users/nayoung/kai_python/requirement.xlsx')
        df = df.fillna('000')
        sim=[]
        x=0
        excel_allArr=df.values
        print(excel_allArr)
        while(x < len(excel_allArr)-1):
            print('x =        ', x)
            
            arr=excel_allArr[x][:]
            excelArr = np.ravel(arr, order='C')           
            print('excelArr = ',excelArr)
            doc = [0, 0]
            simArr = []
            length = len(reqArr)
            print('reqArr =   ',reqArr)
            for i in range(0, length-1, 1):
                doc[0] = excelArr[i+3]
                doc[1] = reqArr[i]
                reqVector = self.list_to_vector(doc)
                denseMatrix = self.vector_to_dense(reqVector)
                simNum = self.checkSim(denseMatrix)
                simArr.append(simNum)
            if(excelArr[6] == reqArr[length-1]):
                simArr.append(1)
            else:
                simArr.append(0)
                #simArr = [0]*len(simArr)
                
            print('simArr   = ',simArr)
            weightSum = 0.4*simArr[0] + simArr[1] + 0.1*simArr[2] + 0.3*simArr[3]
            
            sim.append([])
            sim[x].append(arr[0])
            sim[x].append(arr[1])
            sim[x].append(weightSum)
            
            x = x + 1
            print("")
        simil=np.array(sim)
        df2 = pd.DataFrame(simil,
            columns= ["Unit","Index","Similarity"])
        df2 = df2.sort_values("Similarity",ascending=False)
        df2.to_excel('C:/Users/nayoung/kai_python/test.xlsx', sheet_name = 'Sheet1', 
            header = True,
            index = False, 
            startrow = 0, 
            startcol = 0, 
            ) 
        return df2

    
class external_similarity(similarity):
    def result(self, reqArr):
        df = pd.read_excel('C:/Users/nayoung/kai_python/requirement.xlsx')
        dff=df.loc[[27],:]
        arr=dff.values
        sim = similarity()
        excelArr = np.ravel(arr, order='C')
        doc = [0, 0]
        simArr = []
        length = len(reqArr)
        print("req = ", reqArr)
        for x in range(0, length, 1):
            doc[0] = excelArr[x+3]
            doc[1] = reqArr[x]
            reqVector = sim.list_to_vector(doc)
            denseMatrix = sim.vector_to_dense(reqVector)
            simNum = sim.checkSim(denseMatrix)
            simArr.append(simNum)
        print(simArr)
        weightSum = 0.7*simArr[0] + simArr[1] + 0.5*simArr[2]
        print("sum = ", weightSum)

b=['FC','Scales Control Simulation', 'INT', 1001]
a=internal_similarity()
simil=a.result(b)
print('')
print('<<similarity>>')
print(pd.DataFrame(simil))