#!/usr/bin/python
#coding=utf-8

from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '10.109.111.204', 'port': 9200}])

class Log_analysis(object):
    def __init__(self, index):
         self.index = index

    #获取全部数据
    def get_country_access_num(self):
        scid = es.search(index=self.index,scroll='1m',search_type='scan',size=1000,body={"_source": ["geoip.country_name"]})['_scroll_id']
        while True:
            try:
                data_list = es.scroll(scroll_id=scid,scroll='1m')['hits']['hits']
            except Exception as e:
                print (Exception,":",e)

    #获取排名前10的国家以及访问量
    def get_country_top_10(self):
        response = es.search(
    	index=self.index,
        request_timeout=60,
    	body={
                "size": 0,
    	    "aggs": {
            	"top_states": {
                	"terms": {
                    	"field": "geoip.country_name.raw",
                    	"size": 10
                		}
            	}
        	}
    	}
        )
        country_top_List = response['aggregations']['top_states']['buckets']
        return country_top_List

    #获取前5的http_code以及访问量
    def get_nginx_statu(self):
        response = es.search(
            index=self.index,
            request_timeout=60,
            body={
                "size": 0,
                "aggs": {
                    "top_states": {
                    "terms": {
                            "field": "@fields.status",
                            "size": 5
                            }
                    }
            }
            }
        )
        http_code_List = response['aggregations']['top_states']['buckets']
        return http_code_List

    #获取url以及超时次数
    #调用该函数传递三个参数,超时时间,域名,取前几的url
    def get_nginx_slow_url(self,timeout_sec,domain_name,num):
        body = {
                "size": 0,
                "query": {"filtered" : {"filter" : {"range": {"@fields.upstream_response_time": {"gt": timeout_sec}}}}},
                "query": {"match":{"@fields.host": domain_name}},
                "aggs": {"top_states": {"terms": {"field": "@fields.request.raw","size": num}}}
               }
        response = es.search(
            index=self.index,request_timeout=60,body=body)
        slow_url_List = response['aggregations']['top_states']['buckets']
        return slow_url_List

index_log = Log_analysis('logstash-somangx-2017-09-08')
print (index_log.get_nginx_slow_url(1,"158.85.21.229",5))