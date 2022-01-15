import matplotlib.pyplot as plt

def multiplot(results):
    calibri = {'fontname':'Calibri'}
    plt.figure(figsize = (12, 8))
    plt.grid()
    for i in range (0, len(results)):
        plt.plot(results[i])
    plt.xlabel('Reading point r', **calibri, fontsize = 18)
    plt.ylabel('Signal range', **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)
    plt.legend(fontsize = 12)