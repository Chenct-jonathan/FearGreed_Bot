#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Neutral

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Neutral = True
userDefinedDICT = {"Verbs": ["套現", "追高", "嗄空", "上升", "升空", "昇空"], "股票": ["股"], "航運": ["航運股", "航運類股"], "Subjects": ["台股", "官股", "銅價", "美聯儲", "芝加哥期貨交易所(CBOT)", "玉米期貨", "期貨", "除權息", "盤後", "面板股", "LCD", "五日線", "聯準會", "美股", "科技股", "毛利", "亞股", "早盤", "季線", "台指", "頸線", ""], "台積電": ["台積"], "市占率": ["市佔率"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Neutral:
        print("[Neutral] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[默默]等股價表態[中]":
        # write your code here
        pass

    if utterance == "很多股票幾[十年]來價格始終如一":
        # write your code here
        pass

    if utterance == "所以在[LCD][價格]沒有止穩[前],對[所有][面板股][都][應該]觀望":
        # write your code here
        pass

    return resultDICT