from matplotlib import  pyplot as plt
import numpy as np

t = 0.9 #initial value of function, should not have an effect on the mapping, as long as its not 0 and less than 1
runLogisticMap = False #choose to run the logistic map or a new function

def logisticMap(x,r):
    x = r * x * (1-x)
    return x

def newMap(x,r):
    # x =  (r/4) * np.sin(np.sin(x) * np.pi/np.sin(1))
    # x = (27 * r /4) * x * x * (1-x)
    # x = (r/4) * np.cos(np.pi * x)
    x = (r/4) * np.sin(np.pi * x)
    return x

def findConvergence(outputs):#returns the values cyclical values of a function after recursion has been applied
    convergedValues = []
    initVal = 69 #arbitrary value, by this number of iterations the function should have been able to begin falling into a period 
    value = outputs[initVal]
    diff = outputs[initVal + 1]-value
    period = 0
    for i in range(len(outputs)):
        if (i > initVal+1) and np.abs(outputs[i] - outputs[i-1] - diff) < 0.0001 :
            period = i - (initVal + 1)
            break
    for i in range(period):
        convergedValues.append(outputs[initVal + i])
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
    return findConvergence(outputs)
        
negatives = True
def Bifurcation(increment, x, y):#return coordinate pairs of the bifurcation diagram of the function   
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

        values = getCyclicValues(256,inputs,outputs,r)
        for i in values: 
            x.append(r)
            y.append(i)
        r+=increment

    return [x,y]

x = []
y = []
coords = Bifurcation(0.01,x,y)
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

# print(getCyclicValues())
