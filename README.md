深度学习课程代码练习[源代码](https://github.com/jastarex/DeepLearningCourseCodes)
# 安装tf-gpu
* python3.5 WIN10安装成功tensorflow 1.3
* 需要装CUDA，装CUDA需要装visual studio(装了2015community)
* 装完CUDA需要装cudnn，然后拷贝dll文件到cuda的bin目录中.[参考](http://blog.csdn.net/bianjun1075/article/details/60478487)
* 老师github的程序是python2的，要使用以下命令转换下
> D:\PythonWork\Anaconda2_431\envs\tensorflow\Tools\scripts>python 2to3.py -w D:\WEIZHOU_QTECH\WEIZHOU_Workspace\PythonProjects\TensorflowTest\01_TF_basics_and_linear_regression

# 运行经验
## unit1
* 网上说`get_ipython().magic('matplotlib inline')`应该这样运行`$ ipython python/my_test_imagenet.py`,我直接注释掉了，然后在pycharm里面也能运行起来


# 坑
* AttributeError: module 'tensorflow' has no attribute 'mul'
```
解决方案：[参考](http://blog.csdn.net/caicai_zju/article/details/70477929)
用tf.multiply替代tf.mul
```