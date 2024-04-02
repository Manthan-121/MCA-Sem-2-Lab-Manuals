import matplotlib.pyplot as plt

def histogram(numbers):
    plt.barh(range(len(numbers)), numbers)
    plt.xlabel('Value')
    plt.ylabel('Index')
    plt.title('Vertical Histogram')
    plt.show()

histogram([4, 9, 7])
