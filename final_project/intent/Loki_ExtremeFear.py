#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ExtremeFear

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_ExtremeFear = True
userDefinedDICT = {"Verbs": ["套現", "追高", "嗄空", "上升", "升空", "昇空"], "股票": ["股"], "航運": ["航運股", "航運類股"], "Subjects": ["台股", "官股", "銅價", "美聯儲", "芝加哥期貨交易所(CBOT)", "玉米期貨", "期貨", "除權息", "盤後", "面板股", "LCD", "五日線", "聯準會", "美股", "科技股", "毛利", "亞股", "早盤", "季線", "台指", "頸線", ""], "台積電": ["台積"], "市占率": ["市佔率"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ExtremeFear:
        print("[ExtremeFear] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[他們][最後][會]把[股票]賣倒[台股]崩盤為止":
        # write your code here
        pass

    if utterance == "[早上][根本]就是歹戲拖棚":
        # write your code here
        pass

    if utterance == "[爛][股][一支]":
        # write your code here
        pass

    if utterance == "[玉米期貨][觸]及[三周][半]最低":
        # write your code here
        pass

    if utterance == "[芝加哥期貨交易所(CBOT)][大豆][期貨][週][五]跌至[七周][半]最低":
        # write your code here
        pass

    if utterance == "拖累[美股][全][數]走跌":
        # write your code here
        pass

    if utterance == "瞻仰[火箭][昇空]":
        # write your code here
        pass

    if utterance == "等於是在不知不覺[中]把[自己]推入[中國]的火葬場":
        # write your code here
        pass

    if utterance == "這回[元][氣]大傷":
        # write your code here
        pass

    if utterance == "過[陣子]離開[股][市]好了":
        # write your code here
        pass

    return resultDICT