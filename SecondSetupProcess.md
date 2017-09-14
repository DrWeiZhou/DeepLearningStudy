## 安装vim
docker run -it --name ndl1 ubuntu /bin/bash
apt-get update
apt install -y vim
docker commit ndl1 weizhou/deepl
docker run -it --name ndl2 -v d:/anacondaInstallationFiles:/root/softwares weizhou/deepl /bin/bash
## 安装anaconda2,3（事先下好anaconda2，anaconda3安装文件）
cd /root/sofwares
apt-get install bzip2
bash Anaconda2-4.4.0-Linux-x86_64.sh
source ~/.bashrc
bash Anaconda3-4.4.0-Linux-x86_64.sh -b -p $HOME/anaconda2/envs/py3
##配置conda国内源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --set show_channel_urls yes
##python2安装tensorflow，pytorch
conda install -c conda-forge tensorflow
conda install pytorch torchvision -c soumith
## 初始化配置jupyter,测试python2 jupyter
jupyter notebook --generate-config --allow-root
jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root
## python3安装tensorflow，pytorch
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
conda install pytorch torchvision -c soumith
##测试python3 jupyter
jupyter notebook --port=8888 --no-browser --ip=0.0.0.0 --allow-root
source deactivate
##

