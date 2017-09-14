深度学习课程代码(python2,python3)[源代码](https://github.com/jastarex/DeepLearningCourseCodes)

# 使用Docker运行CPU版本的TensorFlow，pytorch(docker文件大小:8.43GB)
* 基于Ubuntu16.04，安装了vim,git,anacoda2(2.7),anaconda3(3.6)
* 2,3下都直接安装了TensorFlow1.3，pytorch
* 使用jupyter notebook在浏览器中作为ide浏览运行代码
* 包含了上课戎老师的代码(python2,python3)，我会持续更新，或者自己外挂卷运行自己的代码也可
* 构建过程参见`SecondSetupProcess.md`,请大神请DockerFile之，减小容量
* 如果缺python包，可以自己`docker run`进映像安装，我也会更新这个docker文件
```
#下载映像
docker pull weizhou/deeplearning
#运行python2(jupyter notebook)
docker run -it --rm -p 8888:8888 weizhou/deeplearning /root/deeplearning2.sh
#运行python2(jupyter notebook)
docker run -it --rm -p 8888:8888 weizhou/deeplearning /root/deeplearning3.sh
#运行python2(jupyter notebook)自己的代码
docker run --it --rm -p 8888:8888 -v c:/p2CodeDir:/root/DeepLearningStudy/python2/p2CodeDir weizhou/deeplearning /root/deeplearning2.sh
#运行python3(jupyter notebook)自己的代码
docker run --it --rm -p 8888:8888 -v c:/p3CodeDir:/root/DeepLearningStudy/python3/p3CodeDir weizhou/deeplearning /root/deeplearning3.sh
#将控制台最后一行输出的地址复制到host machine的浏览器中，将其中的0.0.0.0修改成127.0.0.1即可
```


# Windows 10安装tf-gpu
* python3.5 WIN10安装成功tensorflow 1.3
* 需要装CUDA，装CUDA需要装visual studio(装了2015community)
* 装完CUDA需要装cudnn，然后拷贝dll文件到cuda的bin目录中.[参考](http://blog.csdn.net/bianjun1075/article/details/60478487),[国内下载地址Omigaga回答](https://www.zhihu.com/question/37082272)
* 老师github的程序是python2的，要使用以下命令转换下
> D:\PythonWork\Anaconda2_431\envs\tensorflow\Tools\scripts>python 2to3.py -w D:\WEIZHOU_QTECH\WEIZHOU_Workspace\PythonProjects\TensorflowTest\01_TF_basics_and_linear_regression

## 运行经验
### unit1
* 网上说`get_ipython().magic('matplotlib inline')`应该这样运行`$ ipython python/my_test_imagenet.py`,我直接注释掉了，然后在pycharm里面也能运行起来


# 坑
* AttributeError: module 'tensorflow' has no attribute 'mul'
```
解决方案：[参考](http://blog.csdn.net/caicai_zju/article/details/70477929)
用tf.multiply替代tf.mul
```