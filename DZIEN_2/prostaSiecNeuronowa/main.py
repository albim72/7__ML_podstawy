import numpy as np
from simplenn import SimpleNeuralNetwork

network = SimpleNeuralNetwork()
print(network)

train_inputs = np.array([[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0],])
train_outputs = np.array([[0,1,0,0,1,0]]).T
train_iters = 50_000

network.train(train_inputs,train_outputs,train_iters)
print(network.weights)

print("ewaluacja sieci")
test_data = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0],])

for data in test_data:
    print(f"wynik dla {data} wynosi: {network.propagation(data)}")
