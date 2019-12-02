import pymysql
from flask import Flask, request
import json
import os


os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
app = Flask(__name__)


@app.route('/index1', methods=['get'])
def indextest():
    # 获取传入的参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    # 对参数进行操作
    print(name)
    data = getcontent(name)
    return data


def getcontent(name):
    conn = pymysql.connect("39.96.199.86", "root", "Root1234", "exp_server")  # 创建连接
    # 使用cursor()方法创建游标，用于执行sql语句并获得结果
    cur = conn.cursor()
    print('---连接数据库成功---')
    sql = "SELECT id AS ID,name AS NAME,uid AS UID,mobile AS MOBILE,app_id AS APP_ID FROM user_info where name='%s'" % name
    cur.execute(sql)
    data = cur.fetchall()
    print(data)
    jsonData = []
    for row in data:
        result = {}
        result['ID'] = row[0]
        result['NAME'] = row[1]
        result['UID'] = row[2]
        result['MOBILE'] = row[3]
        result['APP_ID'] = row[4]
        jsonData.append(result)
    print(jsonData)

    jsondatar = json.dumps(jsonData, ensure_ascii=False)
    return jsondatar[1:len(jsondatar) - 1]


if __name__ == '__main__':
    app.run(host="172.17.11.247",debug=True)
#http://172.17.11.247:5000/index1?name=11223344