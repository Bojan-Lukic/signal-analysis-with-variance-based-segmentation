import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def single_plot(A, label_x, label_y, ax=False, color='#1f77b4'):
    calibri = {'fontname':'Calibri'}
    if ax == True:
        ax = plt.figure(figsize = (12, 8)).gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    else:
        plt.figure(figsize = (12, 8))
    plt.grid()
    plt.plot(A, color)
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)


def line_plot(A, label_x, label_y, lines, labels):
    calibri = {'fontname':'Calibri'}
    plt.figure(figsize = (12, 8))
    plt.grid()
    plt.plot(A, label = labels[0])    
    plt.axvline(x = lines[0], color = "red", linestyle = 'dashed', label = labels[1], ymin = 0.02, ymax = 0.98)
    for i in range(1, len(lines)):
        plt.axvline(x = lines[i], color = "red", linestyle = 'dashed', ymin = 0.02, ymax = 0.98)
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)
    plt.legend(fontsize = 12)


def multiplot(results, label_x, label_y, color):
    calibri = {'fontname':'Calibri'}
    plt.figure(figsize = (12, 8))
    plt.grid()
    if len(color) != len(results):
        for i in range (0, len(results)):
            plt.plot(results[i])
    else:
        for i in range (0, len(results)):
            plt.plot(results[i], color[i])
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)
    

def multiplot_lines(results, label_x, label_y, color, lines, label):
    calibri = {'fontname':'Calibri'}
    plt.figure(figsize = (12, 8))
    plt.grid()
    if len(color) == len(results):
        for i in range (0, len(results)):
            plt.plot(results[i], color=color[i])
    else:
        for i in range (0, len(results)):
            plt.plot(results[i])    
    plt.axvline(x = lines[0], color = "red", linestyle = 'dashed', label = label, ymin = 0.02, ymax = 0.98)
    for i in range(1, len(lines)):
        plt.axvline(x = lines[i], color = "red", linestyle = 'dashed', ymin = 0.02, ymax = 0.98)
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)
    plt.legend(fontsize = 12)


def bar_plot(y_pos, ratiolistcount, label_x, label_y):
    calibri = {'fontname':'Calibri'}
    plt.figure(figsize = (16, 8))
    plt.bar(y_pos, ratiolistcount, align='center', alpha=0.5)
    for i in range(len(ratiolistcount)):
        plt.text(i, int(ratiolistcount[i]) + 2, int(ratiolistcount[i]), ha = 'center', fontsize = 14)
    plt.xlabel(label_x, **calibri, fontsize = 18)
    plt.ylabel(label_y, **calibri, fontsize = 18)
    plt.yticks(fontsize = 14)
    plt.xticks(fontsize = 14)