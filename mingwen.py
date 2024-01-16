#一个只供科学家打铭文的pow链将会崩塌

#在写tx的时候，每一轮交易，改变nonce会让交易顺畅，不会一下子发几十个交易，浪费gas，还会卡

import json

# 函数的三个动作：
# 1、组装参数为 JSON 字符串
# 2、转换为 16 进制
# 3、发起交易
#---------------
# 4、流程控制代码
#-------------- 
def inscribie(self, from_address, private_key, p, op, tick, amt, to, value=0):
    # 1、组装参数为 JSON 字符串
    json_data = json.dumps({"p": p, "op": op, "tick": tick, "amt": amt}, separators=(',', ':'))
    print(f'命数数据：{json_data}')
    
    string_data = 'data:,' + json_data
    print(f'命数数据：{string_data}')
    
    # 2、转换为 16 进制
    hex_data = 'Ox' + string_data.encode().hex()
    
    # 3、发起交易
    return self.helper.send_raw_transaction(from_address, private_key, to, value =value, data = hex_data)



# 4、流程控制代码,无






def task(self, from_address, private_key):

    p = 's'
    op = 'mint'
    tick = 'sync'
    amt = '4'
    to = from_address
    value = 0
    
    success = self.inscribe(from_address, private_key, p, op, tick, amt, to, value)
    
    if success:
        print('打铭文成功')
    else:
        print('打铭文失败失败')
        
    print('打铭文结束')
    
    
    
if __name__ == '__main__':
    task()