这个文档记录了我的python学习过程和练习代码


创建该文档时，我已经基本学习完了《python从入门到实践》，学习了部分python-100天从新手到大师，《流畅的python》一书比较难懂，所以下一步的学习方向有一些不明确。感觉就是基础的已经看过了，进阶的又还看不懂。
因此，我觉得按照python-100天从新手到大师中的编排顺序，从头开始，对基础知识进行查漏补缺，并练习，直到完成100天的学习内容（当然实际用时可能远远超过100天）。
在学习过程中，我会尽可能把每个部分的知识点都写出例程连练习，其中遇到的各种问题的解决方法也会一并记录


1、fork
2、git clone https://github.com/Jason-Zhang9309/golangsdk.git ~/go/src/github.com/huaweicloud/golangsdk
3、git remote add upstream https://github.com/huaweicloud/golangsdk.git
4、git remote -v
5、git fetch upstream
6、git checkout master
7、git merge upstream/master
8、git push origin master
9、git checkout -b  dev
10、写代码
11、git add .
12、git commit -m “注释”
13、git push orgin dev
14、pull request
15、等待代码合并，或修改重新提交（git commit --amend） 
16、git branch -D dev
17、git push origin --delete dev

###每次开发需重复5-17
go get github.com/huaweicloud/golangsdk
go mod vendor
