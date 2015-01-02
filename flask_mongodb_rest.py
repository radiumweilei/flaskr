#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import json
from bson import json_util
from bson.objectid import ObjectId
from pymongo import Connection

app = Flask(__name__)
connection = Connection('localhost', 27017)
db = connection.case


def to_json(data):
    return json.dumps(data, default=json_util.default)  # 将 Mongodb 对象转换成JSON


@app.route('/case/', methods=['GET'])
def get_case_list():
    if request.method == 'GET':
        lim = int(request.args.get('limit', 10))
        off = int(request.args.get('offset', 0))
        results = db['CaseObject'].find().skip(off).limit(lim)
        json_results = []
        for result in results:
            json_results.append(result)
        return to_json(json_results)


@app.route('/case/count', methods=['GET'])
def get_case_count():
    if request.method == 'GET':
        count = db['CaseObject'].count()
        return to_json(count)


@app.route('/case/<_id>', methods=['GET'])
def get_case(_id):
    if request.method == 'GET':
        result = db['CaseObject'].find_one({'_id': _id})
        return to_json(result)


if __name__ == '__main__':
    app.run(debug=True)


# 参考 https://hidekiitakura.wordpress.com/author/hitakura/