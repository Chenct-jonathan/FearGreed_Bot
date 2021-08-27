#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Fear

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Fear = True
userDefinedDICT = {"Verbs": ["套現", "追高", "嗄空", "上升", "升空", "昇空"], "股票": ["股"], "航運": ["航運股", "航運類股"], "Subjects": ["台股", "官股", "銅價", "美聯儲", "芝加哥期貨交易所(CBOT)", "玉米期貨", "期貨", "除權息", "盤後", "面板股", "LCD", "五日線", "聯準會", "美股", "科技股", "毛利", "亞股", "早盤", "季線", "台指", "頸線", ""], "台積電": ["台積"], "市占率": ["市佔率"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Fear:
        print("[Fear] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[中國][經濟]增長[一直]在放緩":
        # write your code here
        pass

    if utterance == "[亞股]表現[幾乎][都]不理想":
        # write your code here
        pass

    if utterance == "[人們]擔心[最大][消費國][中國]的[需求]":
        # write your code here
        pass

    if utterance == "[今天][航運股]轉[弱]":
        # write your code here
        pass

    if utterance == "[共同]成為[外資]的提款機":
        # write your code here
        pass

    if utterance == "[只][能][不停地]變賣有獲利的標記套現":
        # write your code here
        pass

    if utterance == "[台積][尾盤][會]殺尾":
        # write your code here
        pass

    if utterance == "[台股][超詭異]虛漲":
        # write your code here
        pass

    if utterance == "[台股]沒量硬拉雞盤":
        # write your code here
        pass

    if utterance == "[地緣政治][局勢]緊張":
        # write your code here
        pass

    if utterance == "[大盤]受限於量價[架構]欠[佳]":
        # write your code here
        pass

    if utterance == "[所有][面板股][都]不要碰":
        # write your code here
        pass

    if utterance == "[指數]若要持續向[上]攻堅並[站穩月線][反壓區]的[難度][不小]":
        # write your code here
        pass

    if utterance == "[目前][盤勢]屬於[短期]震盪":
        # write your code here
        pass

    if utterance == "[目前]正在[除權息][旺][季]，[根本]停券":
        # write your code here
        pass

    if utterance == "[這回][台灣]和[南韓]同病相憐":
        # write your code here
        pass

    if utterance == "[銅價]已下跌[百分之五]以上":
        # write your code here
        pass

    if utterance == "以[美元]計價的[金屬]對其他[貨幣]持有[者]來說更加昂貴":
        # write your code here
        pass

    if utterance == "因擔憂[生物燃料][行業]的[豆油]需求":
        # write your code here
        pass

    if utterance == "提高警覺":
        # write your code here
        pass

    if utterance == "有多少[人][追高][航運][之後]跌了[40%]忍痛停損":
        # write your code here
        pass

    if utterance == "無量的上漲經不起[一點點]的跌勢":
        # write your code here
        pass

    if utterance == "看來[台股]壓力尚未解除":
        # write your code here
        pass

    if utterance == "結果[現在]持續被嗄空[中]":
        # write your code here
        pass

    if utterance == "負面[因素]並未消失":
        # write your code here
        pass

    if utterance == "這次[外資]因為[太]看好[中國]":
        # write your code here
        pass

    if utterance == "進而拖累需求":
        # write your code here
        pass

    return resultDICT