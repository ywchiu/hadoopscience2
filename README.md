# Big Data資料處理與分析(Hadoop)進階班
=============

### Slides:
https://www.slideshare.net/secret/wbBSOn8Dp9LOf8

password:iii

### [實際應用] 使用Hadoop 分析 Facebook 打卡資訊
https://www.youtube.com/watch?v=FQr2nVvkLzc

### [操作範例] 如何使用Sqoop彙整結構化資料
https://www.youtube.com/watch?v=ZUdXOwnsPPk

### [操作範例] 如何使用Flume彙整非結構化資料
https://www.youtube.com/watch?v=_XXd35NCS2M

### [操作範例] 如何使用Pig
https://www.youtube.com/watch?v=CRujiTH6w18

https://www.youtube.com/watch?v=EEjJzNwlPpk

### [操作範例] 如何使用Hive
https://www.youtube.com/watch?v=UjxBQSy8IBM

install recommendation system
- 1. Download ec.tar.gz
- 2. tar -zxvf ec.tar.gz
- 3. sudo mkdir /webapps
- 4. sudo mv ec /webapps/
- 5. vi /webapps/ec/ec/urls.py
-         'document_root': '/webapps/ec/static/'
- 6. sudo easy_install pip
- 7. pip install django==1.4.5
- 8. pip install happybase
- 9. python manage.py runserver 127.0.0.1:11111

restart hbase
- 1. hbase master stop
- 2. hbase master start
- 3. hbase regionserver stop
- 4. habse regionserver start
