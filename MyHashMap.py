class MyHashMap:
    
    size=100000
    tmpList=[None]*size
    def __init__(self):
        return

    def put(self, key: int, value: int) -> None:
        self.tmpList[key]=value

    def get(self, key: int) -> int:
        if (self.tmpList[key] is None):
            return -1
        return self.tmpList[key]

    def remove(self, key: int) -> None:
        self.tmpList[key]=None


input1=["MyHashMap","remove","put","remove","remove","get","remove","put","get","remove","put","put","put","put","put","put","put","put","put","put","put","remove","put","put","get","put","get","put","put","get","put","remove","remove","put","put","get","remove","put","put","put","get","put","put","remove","put","remove","remove","remove","put","remove","get","put","put","put","put","remove","put","get","put","put","get","put","remove","get","get","remove","put","put","put","put","put","put","get","get","remove","put","put","put","put","get","remove","put","put","put","put","put","put","put","put","put","put","remove","remove","get","remove","put","put","remove","get","put","put"]
input2=[[],[27],[65,65],[19],[0],[18],[3],[42,0],[19],[42],[17,90],[31,76],[48,71],[5,50],[7,68],[73,74],[85,18],[74,95],[84,82],[59,29],[71,71],[42],[51,40],[33,76],[17],[89,95],[95],[30,31],[37,99],[51],[95,35],[65],[81],[61,46],[50,33],[59],[5],[75,89],[80,17],[35,94],[80],[19,68],[13,17],[70],[28,35],[99],[37],[13],[90,83],[41],[50],[29,98],[54,72],[6,8],[51,88],[13],[8,22],[85],[31,22],[60,9],[96],[6,35],[54],[15],[28],[51],[80,69],[58,92],[13,12],[91,56],[83,52],[8,48],[62],[54],[25],[36,4],[67,68],[83,36],[47,58],[82],[36],[30,85],[33,87],[42,18],[68,83],[50,53],[32,78],[48,90],[97,95],[13,8],[15,7],[5],[42],[20],[65],[57,9],[2,41],[6],[33],[16,44],[95,30]]
expected=[None,None,None,None,None,-1,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,90,None,-1,None,None,40,None,None,None,None,None,29,None,None,None,None,17,None,None,None,None,None,None,None,None,None,33,None,None,None,None,None,None,18,None,None,-1,None,None,-1,35,None,None,None,None,None,None,None,-1,-1,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,87,None,None]

obj = MyHashMap()
for i in range(1, len(input1)):
    op = input1[i]
    para=input2[i]
    expect=expected[i]

    result = None
    if (op=="remove"):
        obj.remove(para[0])
        result=None
    elif (op=="put"):
        obj.put(para[0],para[1])
        result =None
    elif (op == "get"):
        result = obj.get(para[0])
        if (result == -1):
            result==None
    print("op={} para={} result={} expect={} result=expect={} ?".format(op,para, "null" if result is None else result, "null" if expect is None else expect, result==expect))
