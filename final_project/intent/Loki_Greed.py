#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for Greed

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

DEBUG_Greed = True
userDefinedDICT = {"Verbs": ["套現", "追高", "嗄空", "上升", "升空", "昇空"], "股票": ["股"], "航運": ["航運股", "航運類股"], "Subjects": ["台股", "官股", "銅價", "美聯儲", "芝加哥期貨交易所(CBOT)", "玉米期貨", "期貨", "除權息", "盤後", "面板股", "LCD", "五日線", "聯準會", "美股", "科技股", "毛利", "亞股", "早盤", "季線", "台指", "頸線", ""], "台積電": ["台積"], "市占率": ["市佔率"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_Greed:
        print("[Greed] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[三百][以下]算是[很便宜]了":
        # write your code here
        pass

    if utterance == "[今日][早盤]洗盤完有[機會]拉[尾盤]":
        # write your code here
        pass

    if utterance == "[台積電]則跳空上漲收復[所有][均線]":
        # write your code here
        pass

    if utterance == "[台股]在本波回升[行情]":
        # write your code here
        pass

    if utterance == "[外資][也]有[可能]開始增加[期貨]的[多單]":
        # write your code here
        pass

    if utterance == "[官股][銀行][也]在[上週五][大力]護盤":
        # write your code here
        pass

    if utterance == "[敦泰]出貨動[能][可]望[更加強勁]":
        # write your code here
        pass

    if utterance == "[科技股]領軍回升":
        # write your code here
        pass

    if utterance == "[美股][20日]上漲":
        # write your code here
        pass

    if utterance == "[該][股][目前]已[站][上][季線]":
        # write your code here
        pass

    if utterance == "[難]得站[上][五日線]了":
        # write your code here
        pass

    if utterance == "且在[2022年][出貨量][能]有[機會]開始[明顯]成長":
        # write your code here
        pass

    if utterance == "並[可]望在[未來]幾[年內]達到[一定][規模]的[市占率]":
        # write your code here
        pass

    if utterance == "伴隨[鋼鐵][市]況需求[強勁]":
        # write your code here
        pass

    if utterance == "因[市場]對[聯準會][政策]收緊的擔憂有所緩解":
        # write your code here
        pass

    if utterance == "好[兆頭]":
        # write your code here
        pass

    if utterance == "對[美聯儲][將][很快]開始[收緊貨幣][政策]的預期提振了[美元]":
        # write your code here
        pass

    if utterance == "感謝[官股][銀行]和[自營商]的護盤":
        # write your code here
        pass

    if utterance == "推動[毛利]及獲利維持在[高檔][水準]":
        # write your code here
        pass

    if utterance == "有站穩[頸線]跟[上升][趨勢線]":
        # write your code here
        pass

    if utterance == "激勵[鋼鐵][類][股][多數]收漲":
        # write your code here
        pass

    if utterance == "自營[上週五]就開始做多":
        # write your code here
        pass

    if utterance == "這個[盤後][不錯]吧":
        # write your code here
        pass

    if utterance == "這樣保持下去就對了":
        # write your code here
        pass

    if utterance == "這樣多[頭][格局][會][更]確立":
        # write your code here
        pass

    if utterance == "這頂多損失[一點點][報酬]而已":
        # write your code here
        pass

    return resultDICT