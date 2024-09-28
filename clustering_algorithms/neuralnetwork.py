from typing import List
import numpy as np
import torch

def classification_using_nn(data, num_classes, labels) -> tuple[np.array, np.array]:
    """
    Perform classification using a neural network
    :param data: The input data of shape (num_samples, num_features)
    :param num_classes: The number of labels
    :param labels: The ground truth labels of shape (num_samples,) 
    :return: A tuple containing the predicted labels and the centroids
    """
    
    # Convert the data to a tensor
    data = torch.tensor(data, dtype=torch.float32)
    
    # print the shape of the data
    print(data.shape)
    
    # Get the number of features in the data
    num_features = data.shape[1]
    
    # Create a neural network with 3 hidden layers
    class classifier(torch.nn.Module):
        
        def __init__(self):
            super(classifier, self).__init__()
            self.fc1 = torch.nn.Linear(num_features, 64)
            self.fc2 = torch.nn.Linear(64, 32)
            self.fc3 = torch.nn.Linear(32, num_classes)
            
        def forward(self, x):
            x = torch.relu(self.fc1(x))
            x = torch.relu(self.fc2(x))
            x = self.fc3(x)
            return x
    
    # Create the model
    model = classifier()
        
    # Set the optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    
    # Use cross entropy loss
    criterion = torch.nn.CrossEntropyLoss()
    
    # Train the model
    for _ in range(100):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()
    
    # Get the clusters
    clusters = torch.argmax(model(data), dim=1).numpy()
    
    # Get the centroids
    
    