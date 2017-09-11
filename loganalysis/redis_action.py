import redis

r = redis.Redis(host='127.0.0.1')

def search_country(search_date):
    return r.keys(pattern=search_date)

def get_redis(key):
    return r.get(key)

def mget_redis(key_list):
    return r.mget(key_list)