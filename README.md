Hadoop Course - To Build Recommendation System
=============

### Slides:
https://www.slideshare.net/secret/jAXKRnPCrknokG


### Package To Download

Nutch (在shell 下):
- 下載Nutch 1.9: wget http://ftp.tc.edu.tw/pub/Apache/nutch/1.9/apache-nutch-1.9-bin.tar.gz


Python (在shell 下):

- sudo pip install requests
- sudo pip install BeautifulSoup4
- sudo pip install grequests
- sudo pip install xmltodict

R (在R 下; Shell 下打入R):

- install.packages("Amelia")

### 下載Tableau Desktop
http://www.tableausoftware.com/products/trial

### 安裝連接Driver
http://www.tableausoftware.com/support/drivers

Mahout 與機器學習
http://www.slideshare.net/secret/gDvLRYko4Cfcn3

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
