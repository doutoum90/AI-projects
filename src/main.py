import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


def getdataSet():
    row_per_class = 100
    sick = np.random.randn(row_per_class, 2) +np.array([-2,-2])
    sick_2 = np.random.randn(row_per_class, 2) +np.array([-2,-2])
    healthy = np.random.randn(row_per_class, 2) +np.array([-2,2])
    healthy_2 = np.random.randn(row_per_class, 2) +np.array([2,-2])
    features = np.vstack([sick, sick_2, healthy, healthy_2])
    targets = np.concatenate((np.zeros(row_per_class*2),np.zeros(row_per_class*2)+1))
    targets = targets.reshape(-1, 1)
    return features, targets

def plotData(features, targets):
    plt.scatter(features[:,0], features[:, 1], s=40, c=targets, cmap=plt.cm.Spectral)
    plt.show()


if __name__== '__main__':
    features, targets = getdataSet()
    # plotData(features, targets)
    tf_features = tf.placeholder(dtype=tf.float32, shape=[None, 2])
    tf_targets = tf.placeholder(dtype=tf.float32, shape=[None, 1])

    session = tf.Session()


    print(tf_features)

   
