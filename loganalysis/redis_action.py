import redis
import datetime

r = redis.Redis(host='127.0.0.1')

def search_key(search_date):
    return r.keys(pattern="%s*"%(search_date))

def del_key(key):
    return r.delete(key)

def exists_key(key):
    return r.exists(key)

def get_redis(key):
    return r.get(key)

def mget_redis(key_list):
    return r.mget(key_list)

def lrange_http_redis(key):
    List = r.lrange(key,0,4)
    return List[::-1]

def hgetall_redis(key):
    Dict = r.hgetall(key)
    return Dict

def hset_redis(key,**kwargs):
    Dict = kwargs
    for k in Dict.keys():
        value = Dict.get(k)
        r.hset(key,k,value)


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

    date_key = str(date1)+"_country_"

    key_list = search_key(date_key)
    for key in key_list:
        Dict = {}
        country = bytes.decode(key).split('_')[2]
        value = bytes.decode(get_redis(key)).split('_')[0]
        yes_key = str(yes_date)+'_country_'+str(country)
        if exists_key(yes_key):
            yes_value = bytes.decode(get_redis(yes_key)).split('_')[0]
        else:
            yes_value = 0
        week_ago_key = str(week_ago_date)+'_country_'+str(country)
        if exists_key(week_ago_key):
            week_ago_value = bytes.decode(get_redis(week_ago_key)).split('_')[0]
        else:
            week_ago_value = 0
        Dict['country']=country
        Dict['value']=value
        Dict['yes_value']=yes_value
        Dict['week_ago_value']=week_ago_value
        result.append(Dict)
    return result

def yester_http_code(date1):
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

    date_key = str(date1)+"_http_code_"

    key_list = search_key(date_key)
    for key in key_list:
        Dict = {}
        http_code = bytes.decode(key).split('_')[3]
        value = bytes.decode(get_redis(key)).split('_')[0]
        yes_key = str(yes_date)+'_http_code_'+str(http_code)
        if exists_key(yes_key):
            yes_value = bytes.decode(get_redis(yes_key)).split('_')[0]
        else:
            yes_value = 0
        week_ago_key = str(week_ago_date)+'_http_code_'+str(http_code)
        if exists_key(week_ago_key):
            week_ago_value = bytes.decode(get_redis(week_ago_key)).split('_')[0]
        else:
            week_ago_value = 0
        Dict['http_code']=http_code
        Dict['value']=value
        Dict['yes_value']=yes_value
        Dict['week_ago_value']=week_ago_value
        url = get_url(date1,http_code)
        Dict['url_list']=url
        result.append(Dict)
    return result



def get_url(date_time,code):
    key = str(date_time)+"_http_url_"+str(code)
    print (key)
    List = lrange_http_redis(key)
    List_str = [ bytes.decode(x) for x in List ]
    result = '\n'.join(List_str)
    print (result)
    return result

def get_domain(date1):
    key = str(date1)+"_http_domain_total"
    List = r.lrange(key,0,9)
    List_str = [bytes.decode(x) for x in List]
    List1 = List_str[::-1]
    return List1

def get_domain_slow_url(key):
    List =  lrange_http_redis(key)
    List_str = [bytes.decode(x) for x in List]
    print (List)
    List1 = []
    for item in List_str:
        Dict = {}
        slow_url = item.split(':')[0]
        slow_num = item.split(':')[1]
        Dict['slow_url'] = slow_url
        Dict['slow_num'] = slow_num
        List1.append(Dict)
    return List1

def get_alert_user():
    key_List = search_key("alert_user")
    List = []

    for key in key_List:
        decode_key = bytes.decode(key)
        Dict = hgetall_redis(decode_key)
        Dict1 = {bytes.decode(k): bytes.decode(Dict.get(k)) for k in Dict.keys()}
        List.append(Dict1)

    return List

def get_alert_rule():
    key_List =  search_key("alert_rule")
    List = []

    for key in key_List:
        decode_key = bytes.decode(key)
        Dict = hgetall_redis(decode_key)
        Dict1 = {bytes.decode(k): bytes.decode(Dict.get(k)) for k in Dict.keys()}
        Dict1['key'] = key
        List.append(Dict1)

    return List


