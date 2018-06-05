import soundfile as sf
import numpy as np
import os
import matplotlib.pyplot as plt


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures'
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
    # plt.close()


def div2ar(ar):
    ar1 = []
    ar2 = []
    for i in ar:
        f = True
        for j in i:
            if f:
                f = False
                ar1.append(j)
            else:
                ar2.append(j)
    return ar1, ar2
def delzero(ar):
    i = 0
    while ar[i] == 0:
        i += 1
    first = i
    i = 0
    end = len(ar)
    while ar[len(ar) - 1 - i] == 0:
        end -= 1
        i += 1
    return ar[first:end]
filename = 'samples/ot x5.wav'
data, samplerate = sf.read(filename, dtype='int16')
sf.info(filename)
print(len(data))
ar1 = delzero(data)
print(samplerate)
x = np.arange(0.0, len(ar1), 1)
y = np.array(ar1)
y = y.transpose()

plt.plot(x, y)
plt.grid(True)
save(filename.split('/')[1].replace('.wav', ''))
plt.show()