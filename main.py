import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.nasdaq.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gid=GA1.2.520139622.1651247728; _gcl_au=1.1.963449012.1651247728; ak_bmsc=F515B39B69CF4DFF5025F6DFD872D028~000000000000000000000000000000~YAAQT582Fy4Sn2eAAQAAMcMIdg9pNw+lRiF2oLRIK4hFoLVyOFjts9px5fOFqpPU3gEqEPZZlbSjIl3gcScCmO8DF2dXFaiMdyOvM5tLg/KkZCRDagUTBSB8DpXZY0s/bq92d2Y+T9aBnOA+0OwMiMUAW/HCUNFM1EtBwX5D3fSA+NE7zYRryRe7YoFa2wikW6j0ByCiy0Udo9nLICsQvSrgH9THQbLtsigdwt60f/eEiXyMeCLLoVUN0Kh0bFg9klMadx85p0J215go03QZqjYiXLotgnGYOulIgkcmmjepXl75i+cVuRl+YWsslYJkM+Ib1ihhHmyCj66t9JdPieO2RUNCIPFVORk15otAzUZZQj3zkwjqtofYDX7ZQYMH0PLo9Xerb0mCBM77o9OmpMLqlaeInxxrYJQKt7fyd1ASZiJbtau5Gh0qMrZAf/NbsO12qG4J1bRDZXskQC0Poc9zcnAUatKfXMi2SeXDMudPr/71dvdDb6YyKX4=; _lr_geo_location=ZA; _rdt_uuid=1651247728785.cd4d217f-a002-490e-a454-1428d13ef333; leadChannelMostRecent=Search; __aaxsc=1; _clck=1nac0ql|1|f11|0; trc_cookie_storage=taboola%2520global%253Auser-id%3Deda0ed6f-e657-44ff-a83a-c18b30536476-tuct9658ff4; _biz_uid=1f7722be41d74ff9eb70bdbc0fff05fe; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; AKA_A2=A; entryUrl=https://www.nasdaq.com/market-activity/stocks; _biz_sid=69271f; _hjSessionUser_1904744=eyJpZCI6ImNiZjgyZWZkLTRhNzMtNWM4OC1hMjRhLWE1MTJmOWUzODMwMiIsImNyZWF0ZWQiOjE2NTEyNDc3MjkwNDMsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample=0; _hjSession_1904744=eyJpZCI6Ijk1MDU3M2Y5LTIwMmYtNDk5OC05Mjc0LTk1Njc5NTJjNTZiMCIsImNyZWF0ZWQiOjE2NTEyNTM4NzU1NzEsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _cc_id=9b01f889ee698e11aa88b71bfb26c8fb; panoramaId_expiry=1651858684493; panoramaId=a60ce0582ed5926f48197d1e75c216d5393856f16fb10a44043596f36391d5a8; entryReferringURL=https://www.nasdaq.com/market-activity/stocks; recentlyViewedList=RDBX|Stocks; todaysViewedSymbol=RDBX|Stocks; secondUrl=https://www.nasdaq.com/market-activity/stocks; _biz_nA=5; _biz_pendingA=%5B%5D; _ga_4VZJSZ76VC=GS1.1.1651253872.2.1.1651254520.58; _uetsid=ca8a6760c7d411ecb1cee55da516d26c; _uetvid=ca8a8bb0c7d411ec90887d1ac9b77ada; bm_sv=4060A73F6821C3F467E7A82BEF4ACBFC~dtU+a7H3zch0QneIP98qe43ugejDGFRwaDNnLz5mou6zGQMN9IGEcMMPdCtgwEWPZHZxBzJIZ8axotUWF/m1CqtQSKprE3p8Be1/9QuUOHMQqlHmf5R8icrfJDvVEgA+JJRXCE8JyZQO6oXe7ipfW1DUOYKoRRyLuvY26hH9fWU=; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Apr+29+2022+19%3A48%3A41+GMT%2B0200+(South+Africa+Standard+Time)&version=6.20.0&isIABGlobal=false&hosts=&landingPath=https%3A%2F%2Fwww.nasdaq.com%2Fmarket-activity%2Fstocks&groups=C0004%3A0%2CC0001%3A1%2CC0003%3A0%2CC0002%3A0; aasd=4%7C1651253877108; _ga=GA1.2.1493132402.1651247728; cto_bundle=jh_BzF9MZjBOb1BYRW0lMkZicHRydzVSTDk2NndrQ282Q2JKZE1rQ0hSZ0ZVMTBva3kwVkwzZW5vbE1mWE9GJTJCNENycmlScFAyUWhJSVMzZEJ2TkJxMjZ2OG5INjZkRnQlMkZNc2s5N2dpS1gxRVNPWXBFUFJ0WDNTYWdiZWdzOTVpJTJGNUtMRG9WazNWcEVUOGt4cUhhN3p6elBtaW0zZyUzRCUzRA; _clsk=1bnzsfy|1651254903029|6|0|j.clarity.ms/collect; RT="z=1&dm=nasdaq.com&si=f77e767d-9339-4ac8-80a3-b61d0ec6a42f&ss=l2kpx5zy&sl=4&tt=jrw&bcn=%2F%2F02179918.akstat.io%2F&obo=1&ul=mavu"',
    'pragma': 'no-cache',
    'referer': 'https://www.nasdaq.com/market-activity/stocks',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
}
site = requests.get(url="https://www.nasdaq.com/market-activity/stocks", timeout=10, headers=headers)

soup = BeautifulSoup(site.text, "html.parser")
high_stocks = soup.find_all(name="tr", class_="mini-asset-class-tables__row mini-asset-class-tables__row--up")
print(len(high_stocks))
f = open("w.txt", "w", encoding="utf-8")
f.write(site.text)
f.close()
for i in high_stocks:
    print(i)
