from os import name
import requests
import json
import ctypes
import time
import random
import requests
import ctypes
from nordvpnzwitch import initialize_VPN,rotate_VPN,terminate_VPN
from datetime import datetime
import sys


parent_dir = "D:\\Users\\yuri2\\Desktop\\tokoped_pdp_py\\"
f = open(parent_dir + "1_nama_toko.txt", 'r+', encoding='utf-8-sig')
importNamaToko = [line for line in f.read().splitlines()]
f.close()

f = open(parent_dir + "2_storeKeyPDP.txt", 'r+', encoding='utf-8-sig')
importstoreKeyPDP = [line for line in f.read().splitlines()]
f.close()

itungan_proses = 1

def ganti_vpn_bos():
    print("ganti server dulu")
    instructions = initialize_VPN(stored_settings=1)
    rotate_VPN(instructions)

if len(importNamaToko) == len(importstoreKeyPDP):
    #kalo jumlah baris text1 sama dengan jumlah baris text2 do:
    
    hitung = range(len(importNamaToko)) #tarik jumlah barisnya

    trigger_vpn = 0
    for i in hitung: #iterate sebanyak list tokonya

        headers = {
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'authority': 'gql.tokopedia.com',
            'x-tkpd-lite-service': 'zeus',
            'x-tkpd-akamai': 'product_info',
            'origin': 'https://www.tokopedia.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'referer': 'https://www.tokopedia.com/',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8',
            'cookie': '_ga=GA1.2.1042084316.1542769760; __auc=9dbf2471167343e577f21aeb4f4; zarget_visitor_info=%7B%7D; DID=cda223321a65667c68eb4752c667d383d4cf316cccd304ee6feef7f6ed7d5af5; _fbp=fb.1.1559025387803.1261762704; lasty=9; fe_discovery_experiments=%7B%220%22%3A%7B%22topads_cpm_exp_abc%22%3A%7B%22name%22%3A%22topads_cpm_exp_abc%22%2C%22selected%22%3A%22old-cpm%22%7D%7D%7D; _jx=c7567f50-e5a5-11e9-a45e-333c5fee818f; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2260c3066d-5bfe-484f-913f-0f4cbf976a7b%22; _BID_TOKOPEDIA_=67bad6daa91fb25583bfbeb7dcd08c27; amp-access=amp-b866GJ3-taJCELumK3-n-A; _gcl_au=1.1.694237445.1587697566; _UUID_NONLOGIN_=09d77a5012089206f9dccc07096fe551; lang=id; _SID_Tokopedia_=WYgZf3w3b97XSNigb1o-kV9RYrh0WIEb5AnPlHJGGiOGBC6rePyvm1zwJY-3HDjaeFu2vofQPWIbQHqITLa2JMnBI6zujweVvrOlCW2DrFEWxG0Wll3dPuLi9tYQuPWu; _gcl_dc=GCL.1601954880.CjwKCAjwiOv7BRBREiwAXHbv3CD0EtTV-RYy6-kBz-eNwU88n-znL-8Tr3yCuhGqzefhskMH2nKFjBoCUNoQAvD_BwE; _hjid=d5b08578-5855-45e2-be67-fc32cd19da99; S_L_e4e10fe4518041c2fc975e43571fb8cb=63efcb28bb4958842be37f661544eaaa~20210104141001; l=1; aus=1; TOPATK=UAm6kfrSSYu8BXhtUPnkqQ; TOPRTK=_Z9wOW2dR1Wg3bs-khvNHg; _gcl_aw=GCL.1602647891.Cj0KCQjwoJX8BRCZARIsAEWBFMI9o8V-rRvGilJ_UVdEz_xeJBaWT_kJngJKxhSfvHFaR_iVLUVVV4AaAvnMEALw_wcB; _gac_UA-9801603-1=1.1602647900.Cj0KCQjwoJX8BRCZARIsAEWBFMI9o8V-rRvGilJ_UVdEz_xeJBaWT_kJngJKxhSfvHFaR_iVLUVVV4AaAvnMEALw_wcB; _gid=GA1.2.175698177.1605521103; tuid=14408709; moe_uuid=a901e0f6-55e5-4a53-b954-3dca23b81208; _jxs=1605580603-c7567f50-e5a5-11e9-a45e-333c5fee818f; bm_sz=97FDA196B62CF15CF704AC26654902DE~YAAQpigoF7W2mKB1AQAAl1Hr1An1BlruuyrTfpJxGZTWJvPd8NdgctzxxID8OHsLXl4NlRPJdQ+Moh8y4Xm9PQTOMRK0CdA4tj0djiwd2+zhiAFrXKqPGg4vZD254rCot5RCrDcvUiTVkRMQlf3F/j79luUVGVCeFOXV/jJgNJkkGHuuscMQ5DyUqkZjhFhwbeX5; bm_sv=9869650B7C4AE6130E5D6A7F4388047E~P9TEn8vthzDK7DkKb33+rXr68D0a11Xv7K+IL9JnNIU76UpNa+OEZd5QrbcZDYsAjwYvzKoSpY1oMa5/5ZrluMBkgJHRJdHggmWW6mI9TIVddFl9ZJ5/WawNDvpiFYdA6qpBdprJWU2xgY1eeaYV06pgBAKGT1YMYVR9QbgrZL4=; __asc=7d57f1aa175d5805d1671ee6db7; _abck=4071AA2CED018616A89714D756D61E04~0~YAAQNEgcuJWNYdV1AQAAKNyA1QSaWyieiDDNuiYh1zAQYNL5aPZViwnFUWu2mEXSmA5WMaVGQofGMXVEx93frJ5HTCi2IDivLecYhZys6AzZqQUYI3dJoDKFqEK1G/dfND4czgc+OLdLOeWB6Q5jFsMmsZp8mHj4oRLa9N1MtiNkFRzj1rv2DcoFqsEvQlYp+VEGnPhSBpsDY2J8mjQrzTjqCLmeTQo7uCryYmrNSDtQmbYJS8oOMOHzNEMMQdXchPuozyTm1rVVNHmOVODdRoo/z7jUyI4+k+EicfDUQTkSVaZfkRClpXFNId33iGGc+XHPkNKazhYksukdcXKTZyiJpyn9khwZ0Q==~-1~-1~-1; _gat_UA-9801603-1=1; _dc_gtm_UA-9801603-1=1',

        }

        data = {
            "operationName":
            "PDPInfoQuery",
            "variables": {
                "shopDomain":
                "inito8",
                "productKey":
                "masker-3ply-3-ply-grade-medical-bedah-medis-surgical-mask-earloop"
            },
            "query":
            "query PDPInfoQuery($shopDomain: String, $productKey: String) {\n  getPDPInfo(productID: 0, shopDomain: $shopDomain, productKey: $productKey) {\n    basic {\n      id\n      shopID\n      name\n      alias\n      price\n      priceCurrency\n      lastUpdatePrice\n      description\n      minOrder\n      maxOrder\n      status\n      weight\n      weightUnit\n      condition\n      url\n      sku\n      gtin\n  __typename\n    }\n    pictures {\n      picID\n      fileName\n      filePath\n      description\n      isFromIG\n      width\n      height\n      urlOriginal\n      urlThumbnail\n      url300\n      status\n      __typename\n    }\n  }\n}\n"
        }

        #swap variabel dengan list yang ada
        data['variables']['shopDomain'] = importNamaToko[i]
        data['variables']['productKey'] = importstoreKeyPDP[i]

        print("Now Process: \n" + importNamaToko[i] + "\n" + importstoreKeyPDP[i] + "\n")
        response = requests.post('https://gql.tokopedia.com/', headers=headers, data=json.dumps(data))


        print(response.status_code, response.reason)
        print(response.text)

        dir_tulis = parent_dir + "_result\\"
        nameJson = importNamaToko[i] + "_" + importstoreKeyPDP[i] + ".json"
        
        nameSimpanJson = dir_tulis + nameJson

        with open(nameSimpanJson, 'w', encoding='utf-8') as f:
            parsed = json.loads(response.text)
            json.dump(parsed, f, ensure_ascii=False, indent=4)
            print("\nFile written!")
        
        print("Crawl ke- " + str(itungan_proses) + " from " + str(len(importNamaToko)) + " produk")
        itungan_proses = itungan_proses + 1

        waktu_delay = random.randrange(5, 10, 2)
        print("Delayed " + str(waktu_delay) + " secs...\n")
        time.sleep(waktu_delay)
        print("")
        trigger_vpn = trigger_vpn + 1

        if trigger_vpn == 15:
            ganti_vpn_bos()
            trigger_vpn = 0
            time.sleep(5)

else:
	textCheck1 = "Nama Toko: " + str(len(importNamaToko))
	textCheck2 = "Store Key: " + str(len(importstoreKeyPDP))
 
	textConcatenate = "Jumlah Text : " + "\n" + textCheck1 + "\n" + textCheck2
	ctypes.windll.user32.MessageBoxW(0, "Jumlah List Text Tidak Sama.\nTolong Check Lagi Ya\n\n" + textConcatenate, "Error", 0)

exportSukses = "Done!!!"
ctypes.windll.user32.MessageBoxW(0, exportSukses, "Exported", 0)