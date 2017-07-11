import math


#位置信息    longitude 为经度  latitude为纬度
class location:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

#计算两个位置之间的距离
def calculateLineDistance(llocation, rlocation):
    if(not isinstance(llocation, location) or not isinstance(rlocation,location)):
        raise Exception("bade type!")
    try:
        ratio = 0.01745329251994329
        llongitude = llocation.longitude
        llatitude = llocation.latitude
        rlongitude = rlocation.longitude
        rlatitude = rlocation.latitude
        llongitude = llongitude * ratio
        llatitude = llatitude * ratio
        rlongitude = rlongitude * ratio
        rlatitude = rlatitude * ratio

        llongitude_sin = math.sin(llongitude)
        llongitude_cos = math.cos(llongitude)
        llatitude_sin = math.sin(llatitude)
        llatitude_cos = math.cos(llatitude)
        rlongitude_sin = math.sin(rlongitude)
        rlongitude_cos = math.cos(rlongitude)
        rlatitude_sin = math.sin(rlatitude)
        rlatitude_cos = math.cos(rlatitude)

        arry1 = []
        arry2 = []
        arry1.append(llongitude_cos * llatitude_cos)
        arry1.append(llatitude_cos * llongitude_sin)
        arry1.append(llatitude_sin)
        arry2.append(rlongitude_cos * rlatitude_cos)
        arry2.append(rlatitude_cos * rlongitude_sin)
        arry2.append(rlatitude_sin)

        tmp = math.sqrt(math.pow(arry1[0]-arry2[0],2) + math.pow(arry1[1] - arry2[1],2)
                        + math.pow(arry1[2] - arry2[2],2))
        return (float) (math.asin(tmp/2.00000) * 1.27420015798544E7)
    except Exception:
        print(Exception)
        return 0.0