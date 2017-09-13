import redis
import datetime

r = redis.Redis(host='127.0.0.1')

def search_key(search_date):
    return r.keys(pattern="%s*"%(search_date))

def get_redis(key):
    return r.get(key)

def mget_redis(key_list):
    return r.mget(key_list)

def yester_contrast(date1,num):
    import datetime
    """
    获取昨天的时间
    """
    date_time = datetime.datetime.strptime(date1, '%Y-%m-%d')
    yes_time = date_time - datetime.timedelta(days=int(num))
    yes_date = yes_time.strftime('%Y-%m-%d')

    key_list = search_key(date1)
    country_list = map(lambda x: bytes.decode(x).split('_')[1], key_list)
    value_list = mget_redis(key_list)
    country_dict = dict(map(lambda x, y: [x, bytes.decode(y).split('_')[0]], country_list, value_list))

    key_list1 = search_key(yes_date)
    country_list1 = map(lambda x: bytes.decode(x).split('_')[1], key_list1)
    value_list1 = mget_redis(key_list1)
    country_dict1 = dict(map(lambda x, y: [x, bytes.decode(y).split('_')[0]], country_list1, value_list1))

    print (country_dict,country_dict1)

print (yester_contrast('2017-09-12',1))

