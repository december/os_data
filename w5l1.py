T = 2
dic = {}
use = set()
int tlast, tcur

def findPage(int request):
    tcur += 1
    if dic.get(request) == None:
        dic[request] = tcur
    else:
        if tcur - tlast > T:
            for k in dic.keys():
                if (tlast < dic[k]) and (dic[k] < tcur):
                    dic.pop(k)
        else:
            dic[request] = tcur
        tlast = tcur