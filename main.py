from matplotlib import  pyplot as plt
import numpy as np

t = 0.9 #initial value of function, should not have an effect on the mapping, as long as its not 0 and less than 1
runLogisticMap = True #choose to run the logistic map or a new function

def logisticMap(x,r):
    x = r * x * (1-x)
    return x

def newMap(x,r):
    x =  (r/4) * np.sin(np.sin(x) * np.pi/np.sin(1))
    # x = (27 * r /4) * x * x * (1-x)
    # x = (r/4) * np.cos(np.pi * x)
    # x = (r/4) * np.sin(np.pi * x)
    return x

def findConvergence(outputs,r):#returns the values cyclical values of a function after recursion has been applied
    convergedValues = []
    initVal = 127 #arbitrary value, by this number of iterations the function should have been able to begin falling into a period 
    if (r > 3.):
        initVal = 201
    value = outputs[initVal]
    diff = outputs[initVal + 1]-value
    period = 0
    for i in range(len(outputs)):
        if (i > initVal+1) and np.abs(outputs[i] - outputs[i-1] - diff) < 0.001 :
            period = i - (initVal + 1)
            break
    for i in range(period):
        convergedValues.append(outputs[initVal + i])
    if (len(convergedValues)) < 1:
        print("r: " + str(r))
        print("Number converged: "+ str(len(convergedValues)))
    return convergedValues

def recurValues(iterationLimit,inputs,outputs,r):#recursively use function of choice for a given number of times
    for i in range(iterationLimit):
        inputs.append(outputs[i])
        if (runLogisticMap):
            outputs.append(logisticMap(inputs[i+1],r))
        else:
            outputs.append(newMap(inputs[i+1],r))

def getCyclicValues(iterationLimit,inputs,outputs,r):#recursively use function of choice and return the values that become cyclical
    recurValues(iterationLimit,inputs,outputs,r)
    return findConvergence(outputs,r)
        
def Bifurcation(increment, x, y, negatives):#return coordinate pairs of the bifurcation diagram of the function   
    r = 0
    if (negatives):   
        r = -4
    while r <= 4:
        inputs = [t]
        outputs = []
        if (runLogisticMap):
            outputs.append(logisticMap(t,r))
        else:
            outputs.append(newMap(t,r))

        values = getCyclicValues(512,inputs,outputs,r)
        for i in values: 
            x.append(r)
            y.append(i)
        r+=increment
    return [x,y]

def graphBifurcation(negatives):
    x = []
    y = []
    coords = Bifurcation(0.0100,x,y,negatives)
    x = coords[0]
    y = coords[1]
    if (runLogisticMap):
        plt.suptitle("rx(1-x)")
    plt.scatter(x,y,s=0.5)
    plt.title("Bifurcation Diagram")
    plt.autoscale(False)
    plt.xlim(0,4)
    if (negatives):
        plt.xlim(-4,4)
    plt.xlabel("r")
    plt.ylim(0,1)
    plt.ylabel("converged value")
    plt.show()

def graphFunctionRecursion(r):
    if (runLogisticMap):
        plt.suptitle("rx(1-x)")

    inputs = [t]
    outputs = []
    if (runLogisticMap):
        outputs.append(logisticMap(t,r))
    else:
        outputs.append(newMap(t,r))

    recurValues(256,inputs,outputs,r)

    iterations = []
    for i in range(len(outputs)):
        iterations.append(i)
    plt.clf()
    plt.scatter(iterations,outputs,s=0.5)
    plt.plot(iterations,outputs)
    plt.title("recursion Diagram")
    plt.suptitle("r = " + str(r))
    plt.autoscale(False)
    plt.xlim(0,len(iterations))
    plt.xlabel("iterations")
    plt.ylim(0,1)
    plt.ylabel("outputs")
    # plt.show()

# r  = 0
# while r <= 4:
#     r += 0.01 
#     graphFunctionRecursion(r)
#     plt.pause(0.001)
# plt.show()

# graphFunctionRecursion(3.58)
# plt.show()
graphBifurcation(False)
# print(getCyclicValues())

# r: 3.6399999999999664
# Number converged: 0
# r: 3.659999999999966
# Number converged: 0
# r: 3.6799999999999655
# Number converged: 0
# r: 3.699999999999965
# Number converged: 0
# r: 3.749999999999964
# Number converged: 0
# r: 3.759999999999964
# Number converged: 0
# r: 3.789999999999963
# Number converged: 0
# r: 3.799999999999963
# Number converged: 0
# r: 3.8199999999999625
# Number converged: 0
# r: 3.8799999999999613
# Number converged: 0
# r: 3.889999999999961
# Number converged: 0
# r: 3.899999999999961
# Number converged: 0
# r: 3.9199999999999604
# Number converged: 0
# r: 3.92999999999996
# Number converged: 0
# r: 3.9499999999999598
# Number converged: 0
# r: 3.989999999999959
# Number converged: 0
