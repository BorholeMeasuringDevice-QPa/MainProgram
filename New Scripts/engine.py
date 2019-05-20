import math

def deviceOrientation(magx, magy, declinationDegre, declinationMinutes):

    return 0
    

def magneticTranslation (magX, magY, magZ, xMin, xMax, yMin, yMax, zMin, zMax ):

    leftX = abs(xMin - xMax)
    rightX = abs(-360 - 360)

    valueXscaled = float(magX-xMin)/float(leftX)
    magDegreeX = -360 + (valueXscaled * rightX)

    leftY = abs(yMin - yMax)
    rightY = abs(-360 - 360)
    valueYscaled = float(magY-yMin)/float(leftY)
    magDegreeY = -360 + (valueYscaled * rightY)

    eftZ = abs(zMin - zMax)
    rightZ = abs(-360 - 360)
    valueZscaled = float(magZ-zMin)/float(leftZ)
    magDegreeZ = -360 + (valueZscaled * rightZ)


    return magDegreeX, magDegreeY, magDegreeZ

def magnetometerDegre(declinationDegre, declinationMinutes):

    

    inclination = math.atan2(x,y)

    if inclination <0:
        inclination = inclination + 2*3.1416

    if inclination>2*3.1416:
        inclination = inclination -2*3.1416

    magneticDegree = (inclination * 180/3.1416)+ (declinationDegre + (declinationMinutes / 60))/(180/3.1416)

    return magneticDegree


def accelerometerDegree(accX, accY, accZ):

    aX=accX*0.00061*9.174
    aY=accY*0.00061*9.174
    aZ=accZ*0.00061*9.174

    rX=aX*3.1416/180
    rY=aY*3.1416/180
    rZ=aZ*3.1416/180

    #mapowanie map ()



    return accDegreX, accDegreY, accDegerZ


