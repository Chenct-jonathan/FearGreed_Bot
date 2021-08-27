#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 2.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
try:
    from intent import Loki_Neutral
    from intent import Loki_ExtremeGreed
    from intent import Loki_Greed
    from intent import Loki_ExtremeFear
    from intent import Loki_Fear
except:
    from .intent import Loki_Neutral
    from .intent import Loki_ExtremeGreed
    from .intent import Loki_Greed
    from .intent import Loki_ExtremeFear
    from .intent import Loki_Fear


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = ""
LOKI_KEY = ""
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "Connect failed."
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    resultDICT = {}
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # Neutral
                if lokiRst.getIntent(index, resultIndex) == "Neutral":
                    resultDICT = Loki_Neutral.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # ExtremeGreed
                if lokiRst.getIntent(index, resultIndex) == "ExtremeGreed":
                    resultDICT = Loki_ExtremeGreed.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Greed
                if lokiRst.getIntent(index, resultIndex) == "Greed":
                    resultDICT = Loki_Greed.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # ExtremeFear
                if lokiRst.getIntent(index, resultIndex) == "ExtremeFear":
                    resultDICT = Loki_ExtremeFear.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # Fear
                if lokiRst.getIntent(index, resultIndex) == "Fear":
                    resultDICT = Loki_Fear.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)


if __name__ == "__main__":
    # Neutral
    print("[TEST] Neutral")
    inputLIST = ['默默等股價表態中','很多股票幾十年來價格始終如一','所以在LCD價格沒有止穩前,對所有面板股都應該觀望']
    testLoki(inputLIST, ['Neutral'])
    print("")

    # ExtremeGreed
    print("[TEST] ExtremeGreed")
    inputLIST = ['一路發','基本面佳','台指狂拉200點','今天大盤漲那麼多','昨天航運類股大漲','今天恭喜各位都大漲','國內的成績相當不容易']
    testLoki(inputLIST, ['ExtremeGreed'])
    print("")

    # Greed
    print("[TEST] Greed")
    inputLIST = ['好兆頭','美股20日上漲','科技股領軍回升','這個盤後不錯吧','難得站上五日線了','台股在本波回升行情','該股目前已站上季線','這樣保持下去就對了','三百以下算是很便宜了','伴隨鋼鐵市況需求強勁','激勵鋼鐵類股多數收漲','自營上週五就開始做多','這樣多頭格局會更確立','有站穩頸線跟上升趨勢線','敦泰出貨動能可望更加強勁','這頂多損失一點點報酬而已','今日早盤洗盤完有機會拉尾盤','官股銀行也在上週五大力護盤','感謝官股銀行和自營商的護盤','台積電則跳空上漲收復所有均線','推動毛利及獲利維持在高檔水準','外資也有可能開始增加期貨的多單','且在2022年出貨量能有機會開始明顯成長','因市場對聯準會政策收緊的擔憂有所緩解','並可望在未來幾年內達到一定規模的市占率','對美聯儲將很快開始收緊貨幣政策的預期提振了美元']
    testLoki(inputLIST, ['Greed'])
    print("")

    # ExtremeFear
    print("[TEST] ExtremeFear")
    inputLIST = ['爛股一支','瞻仰火箭昇空','這回元氣大傷','拖累美股全數走跌','過陣子離開股市好了','早上根本就是歹戲拖棚','玉米期貨觸及三周半最低','他們最後會把股票賣倒台股崩盤為止','等於是在不知不覺中把自己推入中國的火葬場','芝加哥期貨交易所(CBOT)大豆期貨週五跌至七周半最低']
    testLoki(inputLIST, ['ExtremeFear'])
    print("")

    # Fear
    print("[TEST] Fear")
    inputLIST = ['提高警覺','進而拖累需求','今天航運股轉弱','台積尾盤會殺尾','台股超詭異虛漲','台股沒量硬拉雞盤','地緣政治局勢緊張','負面因素並未消失','所有面板股都不要碰','亞股表現幾乎都不理想','共同成為外資的提款機','目前盤勢屬於短期震盪','看來台股壓力尚未解除','結果現在持續被嗄空中','中國經濟增長一直在放緩','大盤受限於量價架構欠佳','這回台灣和南韓同病相憐','這次外資因為太看好中國','銅價已下跌百分之五以上','人們擔心最大消費國中國的需求','因擔憂生物燃料行業的豆油需求','無量的上漲經不起一點點的跌勢','目前正在除權息旺季，根本停券','只能不停地變賣有獲利的標記套現','有多少人追高航運之後跌了40%忍痛停損','以美元計價的金屬對其他貨幣持有者來說更加昂貴','指數若要持續向上攻堅並站穩月線反壓區的難度不小']
    testLoki(inputLIST, ['Fear'])
    print("")

    # 輸入其它句子試看看
    #inputLIST = ["輸入你的內容1", "輸入你的內容2"]
    #filterLIST = []
    #resultDICT = runLoki(inputLIST, filterLIST)
    #print("Result => {}".format(resultDICT))