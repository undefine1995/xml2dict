#-*coding:utf-8*-
from collections import defaultdict

def etree_to_dict(t):       # t为xml格式字符
    d = {t.tag: {} if t.attrib else None}       # d为构建的目标字典
                                                # t.tag若有则为字典第一层
    children = list(t)      # 以下开始递归迭代处理树，直至叶子节点
    if children:        # 判断节点是否为空，递归边界条件
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):     # 递归遍历该树
            for k, v in dc.iteritems():
                dd[k].append(v)     # 在字典中加入自下而上的结果
        d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.iteritems()}}      # 对叶子节点的处理情况
    if t.attrib:        # 处理属性,这里对于存于属性中的 全部加前缀@
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.iteritems())
    if t.text:      # 处理text值
        text = t.text.strip()       # 删除空格
        if children or t.attrib:        #
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text     # txet值直接封装为t.tag
    return d        # return
