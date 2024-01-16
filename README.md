# Universal-inscription-method 铭文
通用打铭文的方式，参考大佬 https://x.com/gm365/status/1736286875839873218?s=20

1、通用铭文格式

一般而言，铭文大体有如下两种格式：

data:,{"p":"zrc-20","op":"mint","tick":"sync","amt":"4"}

{"p":"zrc-20","op":"mint","tick":"sync","amt":"4"}

2、打铭文的实质

从交易的角度而言，一个所谓的“打铭文”操作等同于如下动作：

to: from_address    #自己的钱包地址

value: 0            #金额

input data: text_to_hex(input_data)  #铭文的字符串转换为16进制代码，并添加 0x 作为开头

把文字转换成 16 进制

def text_to_hex(text):

    return ''.join(format(ord(char), '02x') for char in text)
    
了解了这笔交易的核心，那么一个通用的打铭文的代码也就呼之欲出了

函数的三个动作：

1、组装参数为 JSON 字符串

2、转换为 16 进制

3、发起交易

代码接收6个铭文相关的参数：

p : 类型定义，根据铭文规定填写，比如 zrc-20

op : 动作，打铭文的操作一般是 mint

tick :  名称，这里是 sync

amt : 数量，根据规定填写，一般不可乱改动，这里是 4

to : 交易地址，根据规定来，有些是向自己钱包地址发起交易，有些则有特定地址，比如 Facet 铭文

value : 附带的 ETH 价值，正常来说都是0，收钱的铭文除外
