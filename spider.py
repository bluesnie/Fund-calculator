# _*_ encoding: utf-8 _*_
__author__ = 'nzb'
__date__ = '2019/5/18 14:41'

import json
import re

import requests

from dao import Dao

# fund_map = {
#     '易方达沪深300ETF联接A': '110020',
#     '天弘中证500指数A': '000962',
# }
# fund_map1 = [
#     {'name': '易方达沪深300ETF联接A', 'num': '110020'},
#     {'name': '天弘中证500指数A', 'num': '000962'},
#
# ]


def get_page(url, headers, query_params, jj_info):
    """
    爬取最新基金净值
    url: url
    headers:请求头
    query_params:请求参数
    id：基金ID
    """

    res = requests.get(url, headers=headers, params=query_params).text
    # print(res)
    pattern = re.compile(r'\((.*?)\)', re.S)
    res = re.findall(pattern, res)
    res = json.loads(res[0])
    if res.get('ErrCode') == 0 and res.get('Data'):
        for item in res.get('Data').get('LSJZList'):
            dic = {}
            dic['fund'] = jj_info[0]
            dic['jzdate'] = item.get('FSRQ')
            dic['dwjz'] = item.get('DWJZ')
            dic['ljjz'] = item.get('LJJZ')
            dic['jzzzl'] = item.get('JZZZL')
            sql = "select id from fund_jz where fund={0} and jzdate='{1}';".format(jj_info[0], item.get('FSRQ'))
            # print(sql)
            res = dao.fetchone(sql)
            if res and res[0] != False:
                result = dao.update('fund_info', dic)
                if result:
                    print('{0}基金{1}更新成功'.format(jj_info[1], item.get('FSRQ')))
                else:
                    print(result[1])
            elif res == False:
                result = dao.insert('fund_jz', dic)
                if result:
                    print('{0}基金{1}插入成功'.format(jj_info[1], item.get('FSRQ')))
                else:
                    print(result[1])
            else:
                print(res[1])


def get_jj_info():
    """获取基金信息"""
    sql = "select * from fund_info;"
    result = dao.fetchall(sql)
    return result


def main():
    for item in get_jj_info():  # 获取基金信息
        headers = {
            'Referer': 'http://fundf10.eastmoney.com/jjjz_' + item[2] + '.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  \
                            Chrome/72.0.3626.121 Safari/537.36',
        }
        print('正在获取{0}基金'.format(item[1]))
        for i in range(1, 2):
            query_params = {
                'callback': 'jQuery18308233452494049915_1558162230907',
                'fundCode': '110020',
                'pageIndex': i,
                'pageSize': '20',
            }

            url = 'http://api.fund.eastmoney.com/f10/lsjz'
            get_page(url, headers, query_params, item)


if __name__ == '__main__':

    dao = Dao('root', '123456', 'fund')

    main()
