import requests
import datetime

curr_time = datetime.datetime.now()
re = requests.request('post',f'https://api.day.app/qjUhpKS9bJxkCyrsSxUzU5/签到成功!/UPC-疫情防控通已上报({curr_time.month}月{curr_time.day}日)')
print(re)
requests.request('post', 'https://api.day.app/qjUhpKS9bJxkCyrsSxUzU5/签到成功!/UPC-疫情防控通已上报')
