### DEMO

![image](https://github.com/XingyuXiong/newsbot/blob/master/demo.gif)

---

### 运行
cd /newsbot/server
python manage.py runserver
于127.0.0.1：8000端口进行访问

---

### 说明

本程序一个基于newsapi的新闻获取机器人newsbot

html+css+js构建前端，django数据库对话信息

用rasa-nlu抽取用户搜索关键词实体

之前版本已部署在服务器上，请访问[newsbot](http://106.54.107.156:8000)

---

### API

#### 检索：

关键词或短语

发布日期

新闻来源

新闻来源域名

#### 分类：

发布日期

相关性

受欢迎度

---

### 更新

google翻译：已经测试完毕可以使用，用以处理多语言任务

支持向量机进行意图识别：需要构建训练数据集

否定意图侦测：需要使用Chatito工具构建模型数据集

更人性化的功能提示和输入检测

---

### 补充说明

新闻机器人的功能受限于免费api newsapi的全部功能，因此无法在对话中完整显示新闻而只能显示其来源。且该bot全部功能都来源于newsapi的不同参数的函数调用

