from matplotlib import  pyplot as plt
import numpy as np

r = 3.3
t = 0.2
inputs = [t]
outputs = []

def logisticMap(x):
    x = r * x * (1-x)
    return x
def newMap(x):
    x =  r/4 * np.sin(np.sin(x) * np.pi/np.sin(1))
    return x

def findConvergence(outputs):
    convergedValues = []
    initVal = 19
    value = outputs[initVal]
    diff = outputs[initVal + 1]-value
    period = 0
    for i in range(len(outputs)):
        if (i > initVal+1) and np.abs(outputs[i] - outputs[i-1] - diff) < 0.001 :
            period = i - (initVal + 1)
            print(period)
            break
    for i in range(period):
        convergedValues.append(initVal + i)
    return convergedValues

runLogisticMap = False
iterations = [0]

if (runLogisticMap):
    outputs.append(logisticMap(t))
else:
    outputs.append(newMap(t))

iterationLimit = 256
for i in range(iterationLimit):
    iterations.append(i)
    inputs.append(outputs[i])
    if (runLogisticMap):
        outputs.append(logisticMap(inputs[i+1]))
    else:
        outputs.append(newMap(inputs[i+1]))

# r=0
# for i in range(100):
#     r+=1

plt.scatter(inputs,outputs)
plt.scatter(iterations,outputs)
plt.title("Logistic Map")
plt.autoscale(False)
plt.xlim(0,len(iterations))
plt.ylim(0,1)
plt.show()

print(findConvergence(outputs))