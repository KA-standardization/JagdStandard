from pymongo import MongoClient
# 创建一个 MongoClient 连接到服务器
client = MongoClient(host='localhost',port=27017)

# client.dbname 获取到一个数据库对象
db =client.python201

# db.collection_name 获取到一个表，可以进行增删改查的操作
cursor = db.student.find()  # find的结果是一个cursor对象，是一个可迭代对象
for s in cursor:
    print(s)

# 插入一条数据
db.student.insert({'name':'tony','age':19})

