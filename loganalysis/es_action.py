from elasticsearch import Elasticsearch


def get(index, **body):
    es = Elasticsearch([{'host': '172.30.193.220', 'port': 9200}])
    print index, body
    body1 = []
    for key in body.keys():
        body1.append({'match': {key: body[key]}})

    body_end = {'bool': {'must': body1}}
    # print body_end
    # res = es.search(index=index, body={'query': {"match": body}, "size": 10,
    #                                    "_source": ["endtime", "serverip", "loginip", "dir", "command", "user"]})
    # res = es.search(index='logstash-history-2017.07.14', body={'query': body_end,"size": 10,"_source": [
    #     "endtime", "serverip", "loginip", "dir", "command", "user"]})
    res = es.search(index=index, body={'query': body_end, "size":1000,"_source": [
        "endtime", "serverip", "loginip", "dir", "command", "user"]})
    # print res
    result = res['hits']['hits']
    # print result,type(result)
    # new_res = []
    # for item in result:
    #     new_item = {}
    #     for key, value in item.items():
    #         new_item[key.replace('_', '')] = value
    #     new_res.append(new_item)
    # print new_res
    # return new_res
    return result