import redis
import datetime

r = redis.Redis(host='127.0.0.1')

def search_key(search_date):
    return r.keys(pattern="%s*"%(search_date))

def get_redis(key):
    return r.get(key)

def mget_redis(key_list):
    return r.mget(key_list)

def yester_contrast(date1):
    import datetime
    """
    获取昨天的时间
    """
    date_time = datetime.datetime.strptime(date1, '%Y-%m-%d')
    yes_time = date_time - datetime.timedelta(days=1)
    yes_date = yes_time.strftime('%Y-%m-%d')

    week_ago_time = date_time - datetime.timedelta(days=7)
    week_ago_date = week_ago_time.strftime('%Y-%m-%d')

    result = []

    key_list = search_key(date1)
    for key in key_list:
        Dict = {}
        country = bytes.decode(key).split('_')[1]
        value = bytes.decode(get_redis(key)).split('_')[0]
        yes_key = str(yes_date)+'_'+str(country)
        yes_value = bytes.decode(get_redis(yes_key)).split('_')[0]
#        week_ago_key = str(week_ago_date)+'_'+str(country)
#        week_ago_value = bytes.decode(get_redis(week_ago_key)).split('_')[0]
        Dict['country']=country
        Dict['value']=value
        Dict['yes_value']=yes_value
#        Dict['week_ago_value']=week_ago_value
        result.append(Dict)
    return result

