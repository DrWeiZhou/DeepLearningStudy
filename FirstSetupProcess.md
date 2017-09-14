docker run -it --name dl1 ubuntu /bin/bash
apt-get update
apt install -y vim
vim /etc/apt/source.list #复制源http://blog.csdn.net/paincupid/article/details/52895676，没效果
apt-get update
exit
docker commit dl1 weizhou/deeplearning
#事先下好anaconda2，anaconda3安装文件
docker run -it --name dl2 -v d:/anacondaInstallationFiles:/root/softwares weizhou/deeplearning /bin/bash
cd /root/sofwares
apt-get install bzip2
bash Anaconda2-4.4.0-Linux-x86_64.sh
source ~/.bashrc
#参照http://www.cnblogs.com/zle1992/p/6720425.html
bash Anaconda3-4.4.0-Linux-x86_64.sh -b -p $HOME/anaconda2/envs/py3
docker commit dl2 weizhou/deeplearning
docker run -it --name dl3 -p 8888:8888 weizhou/deeplearning /bin/bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
conda create -n deeplearning2 
source activate deeplearning2
conda install -c conda-forge tensorflow
conda install pytorch torchvision -c soumith
#参考http://jupyter-notebook.readthedocs.io/en/latest/public_server.html
jupyter notebook --generate-config --allow-root
jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root
#获取git仓库
apt-get install git
git config --global user.name "toweizhou"
git config --global user.email "toweizhou@gmail.com"
git clone https://github.com/DrWeiZhou/DeepLearningStudy.git
#在新env下重新安装jupyter
source activate deeplearning2
conda install jupyter
source activate py3
 rm -f $HOME/anaconda2/envs/py3/bin/conda*
 rm -f $HOME/anaconda2/envs/py3/conda-meta/conda-*
 rm -f $HOME/anaconda2/envs/py3/bin/activate
 rm -f $HOME/anaconda2/envs/py3/bin/deactivate
 cd $HOME/anaconda2/envs/py3/bin
 ln -s ../../../bin/conda .
 ln -s ../../../bin/activate .
 ln -s ../../../bin/deactivate .
conda install -c conda-forge tensorflow



docker run -it --name dl6 -p 8888:8888 -v d:/anacondaInstallationFiles:/root/softwares weizhou/deeplearning /bin/bash


 