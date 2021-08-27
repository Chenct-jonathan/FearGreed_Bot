#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for ExtremeGreed

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_ExtremeGreed = True
userDefinedDICT = {"Verbs": ["套現", "追高", "嗄空", "上升", "升空", "昇空"], "股票": ["股"], "航運": ["航運股", "航運類股"], "Subjects": ["台股", "官股", "銅價", "美聯儲", "芝加哥期貨交易所(CBOT)", "玉米期貨", "期貨", "除權息", "盤後", "面板股", "LCD", "五日線", "聯準會", "美股", "科技股", "毛利", "亞股", "早盤", "季線", "台指", "頸線", ""], "台積電": ["台積"], "市占率": ["市佔率"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_ExtremeGreed:
        print("[ExtremeGreed] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[一][路]發":
        # write your code here
        pass

    if utterance == "[今天][大盤]漲那麼多":
        # write your code here
        pass

    if utterance == "[今天]恭喜各位[都]大漲":
        # write your code here
        pass

    if utterance == "[台指]狂拉[200][點]":
        # write your code here
        pass

    if utterance == "[國內]的[成績][相當]不[容易]":
        # write your code here
        pass

    if utterance == "[基本面]佳":
        # write your code here
        pass

    if utterance == "[昨天][航運類股]大漲":
        # write your code here
        pass

    return resultDICT