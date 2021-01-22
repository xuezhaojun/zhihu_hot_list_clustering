# 知乎热门问题分析

本项目中，通过3个步骤，分析2020年度，7月到8月中，知乎最人们的问题，从而了解知乎用户在这个时间段内，最关注的内容是什么。

## 步骤
* Crawl Data = get_zhihu_data.py
* Data Preprocess
    + nlp
    + tf-idf
    + svd
* Clustering
    + k-means
    + dbscan

由于知乎的反爬虫策略，我们只爬取了（问题描述+前两个高赞回答内容）

nlp过程中，使用jieba对爬取的内容进行：

* 分词
* 去掉标点符号
* 去掉stopwords

tf-idf是信息检索用于匹配query和文本内容的技术，我们通过比对两个问题的tf-idf的score来判断内容是否一致

svd用于提取文本的关键特征，减少数据维度

聚类过程中使用了K-means和dbscan两种聚类方式，K-means的聚类方式对于高纬度的数据结果不是很理想，而基于密度的dbscan具有去噪的能力，可以更精确的聚类数据特征。因此最终选择了dbscan的聚类结果。

## 结果

可以看到总体来说，用户最关心的内容为：

* 工作，孩子，学习等，生存相关问题
* 美国疫情和选举等，国际政治问题
* 护肤问题
* 情感问题
* 等等

![结果1](https://github.com/xuezhaojun/zhihu_hot_list_clustering/blob/master/r_01.png?raw=true)

我们还可以具体统计某一个类聚类结果下的高频词，如下为“美国”聚类的高频词展示：

![结果2](https://github.com/xuezhaojun/zhihu_hot_list_clustering/blob/master/r_02.png?raw=true)

具体聚类结果可见目录 k_means_results 和 dbscan_results下的结果文件

## 依赖
* [requests](https://requests.readthedocs.io/en/master/)
* [lxml](https://lxml.de/index.html)
* [jieba](https://github.com/fxsjy/jieba)