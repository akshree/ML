import numpy as np

input_features = np.array([[1,0,0,1],[1,0,0,0],[0,0,1,1],
 [0,1,0,0],[1,1,0,0],[0,0,1,1],
 [0,0,0,1],[0,0,1,0]])
print(input_features.shape)
print(input_features)

target_output = np.array([[1,1,0,0,1,1,0,0]])

target_output = target_output.reshape(8,1)
print(target_output.shape)
print(target_output)

#weights :
weights = np.array([[0.1],[0.2],[0.3],[0.4]])
print(weights.shape)
print(weights)
bias = 0.3
lr = 0.05# Learning Rate

# Sigmoid function :
def sigmoid(x):
 return 1/(1+np.exp(-x))

# Derivative of sigmoid function :
def sigmoid_der(x):
 return sigmoid(x)*(1-sigmoid(x))

# Running our code 10000 times :
for epoch in range(5000):
 inputs = input_features
 pred_in = np.dot(inputs, weights) + bias

 pred_out = sigmoid(pred_in)

 error = pred_out - target_output

 x = error.sum()
 print(x)

 #Calculating derivative :
 dcost_dpred = error
 dpred_dz = sigmoid_der(pred_out)

 z_delta = dcost_dpred * dpred_dz

 inputs = input_features.T
 weights -= lr * np.dot(inputs, z_delta)
 for i in z_delta:
  bias -= lr * i

#Printing final weights:
print("\n\n")
print(weights)
print("\n\n")
print(bias)
print("\n\n")
#Testing 1 :
single_point = np.array([1,0,0,1])
result1 = np.dot(single_point, weights) + bias
result2 = sigmoid(result1)
print(result2)
#Testing 2:
single_point = np.array([0,0,1,0])
result1 = np.dot(single_point, weights) + bias
result2 = sigmoid(result1)
print(result2)
#Testing 3 :
single_point = np.array([1,0,1,0])
result1 = np.dot(single_point, weights) + bias
result2 = sigmoid(result1)
print(result2)
