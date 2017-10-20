import numpy as np
import rawpy
import imageio
import random
import os

a = []
b = len(a)
print b

'''
a = np.zeros(shape=(3,4))
a[0] = [1.1,2,3,4]
a[1] = [1.2,2,3,4]
a[2] = [1.1,2,3,4]

print a.shape
b = np.zeros(shape=(3,4))
b[0] = [1,2,3,4]
b[1] = [3,6,9,12]
b[2] = [9,18,27,36]

c = a.astype('uint8')
print c

temp_str = ['44C','48C','56C','68C','80C','92C']
print len(temp_str)

git_task_accuracy = 'C:/Users/Sai/Desktop/thermal/task_accuracy'
input_raw_images  = git_task_accuracy+'/raw_images/'

all_files = [x for x in os.listdir(input_raw_images)]
print all_files


d = a[1,:]
print d
print d.shape
print d[0]
print d[1]
print d[2]
print d[3]

def single_num(n,mat,slope,intercept,stddev):
    # Repeats until a number within the scale is found.
    while 1:
        mat_trans = (mat*slope) + intercept
        h,w = mat.shape
        for x in xrange(h):
            row = mat_trans[x,:]
            num = []
            for y in xrange(w):
                num.append( random.randint(row[y]-(n*stddev), row[y]+(n*stddev)) )
            mat_trans[x,:] = num
        return mat_trans

c = single_num(1,a,1,1,0 )

print c
'''







'''
c = np.zeros(shape=(3,4))
print a[:,1]
for i in xrange(3):
    print i
    t1 = np.column_stack((a[:,i],b[:,i]))
    if ( i == 0):
        c = t1
    else:
        c = np.column_stack((c,t1))

print c

c = np.reshape(c,(2,9))

print c

with rawpy.imread(filename) as raw:
    #raw = rawpy.imread(filename)
    b = raw.raw_image
    rgb = raw.postprocess(output_bps=8)
    imageio.imsave('C:\Users\Sai\Downloads\IMG_20171004_164502.png', rgb)

# add a row/column to numpy array
fixed_width = 3
fixed_heigth = 2
bayer_img = np.zeros(shape=(fixed_heigth,fixed_width))

tl = [1,2,3]
bayer_img = np.insert(bayer_img,[1],tl, axis=0)

print bayer_img

# read bytes from a file
filename = 'C:\Users\Sai\Downloads\Task_acc_test.raw'

with open(filename, "rb") as f:
    integers = np.fromstring(f.read(), dtype='uint8')
    print integers[np.where(integers > 80)]

'''