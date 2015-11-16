5W - PaaS 101 日记本

- 任务目标：在Web版基础上完成极简交互笔记的PaaS版本
- 需求如下：
    - 将上周应用网站发布为公网稳定服务
    - 可以通过固定域名访问系统：
        - 每次运行时合理打印出过往的所有笔记
        - 一次接受输入一行笔记
        - 在服务器端保存为文件
        - 同时兼容3W的Net版本的命令行界面进行交互
    - 可以通过本地命令行工具监察/管理网站:
        - 获得当前笔记数量/访问数量等等基础数据
        - 可以获得所有笔记备份的归档下载
- 发布到各自仓库`_src/0m2py5w/5wex0/`目录中
- 关键技术
    - 固定的免费环境用于运行/调试 - SAE(新浪云)
    - Bottle 网页框架
    - kvdb 新浪云
    - pprint - Pretty-print data structures
    - google Good-API-Design Armin Ronacher
    - Simple API's with bottle.py