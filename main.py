from matplotlib import  pyplot as plt
import numpy as np

t = 0.5#initial value of function, should not have an effect on the mapping, as long as its not 0

def logisticMap(x,r):
    x = r * x * (1-x)
    return x

def newMap(x,r):
    x =  r/4 * np.sin(np.sin(x) * np.pi/np.sin(1))
    return x

def findConvergence(outputs):#returns the values cyclical values of a function after recursion has been applied
    convergedValues = []
    initVal = 19 #arbitrary value, by 19 iterations the function should have been able to begin falling into a period 
    value = outputs[initVal]
    diff = outputs[initVal + 1]-value
    period = 0
    for i in range(len(outputs)):
        if (i > initVal+1) and np.abs(outputs[i] - outputs[i-1] - diff) < 0.001 :
            period = i - (initVal + 1)
            break
    for i in range(period):
        # print(outputs[initVal + i])
        convergedValues.append(outputs[initVal + i])
    # convergedValues.sort()
    return convergedValues

runLogisticMap = False


def recurValues(iterationLimit,inputs,outputs,r):#recursively use function of choice for a given number of times
    for i in range(iterationLimit):
        inputs.append(outputs[i])
        if (runLogisticMap):
            outputs.append(logisticMap(inputs[i+1],r))
        else:
            outputs.append(newMap(inputs[i+1],r))

def getCyclicValues(iterationLimit,inputs,outputs,r):#recursively use function of choice and return the values that become cyclical
    for i in range(iterationLimit):
        inputs.append(outputs[i])
        if (runLogisticMap):
            outputs.append(logisticMap(inputs[i+1],r))
        else:
            outputs.append(newMap(inputs[i+1],r))
    return findConvergence(outputs)
        
def graphConverged(increment, x, y):#return coordinate pairs of converged/cyclic points of the function
    # global x
    # global y
    # global r            
    r = 0.0

    # for j in range(int(4/increment)):
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
coords = graphConverged(0.01,x,y)
x = coords[0]
y = coords[1]
# print(len(x))
# print(len(y))


plt.scatter(x,y)
plt.title("Logistic Map")
plt.autoscale(False)
plt.xlim(0,4)
plt.ylim(0,1)
plt.show()
