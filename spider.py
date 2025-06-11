import requests
import time
import simplejson
import random
url = "https://api-csob.ok-skins.com/api/v2/goods/search"


headers = {
    "Host": "api-csob.ok-skins.com",
    "Connection": "keep-alive",
    "sec-ch-ua-platform": "\"Linux\"",
    "Timestamp": "1746794748698",  # 注意和 URL 参数不一样，建议保持一致
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "Auth": "9cb3b771a34586035d5751eaca70d40e",
    "sec-ch-ua-mobile": "?0",
    "Accept": "*/*",
    "Origin": "https://cs2ob.cn",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://cs2ob.cn/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
params = {
    "name": "",
    "page": 99,
    "isDetail": "true",
    "category": "weapon_awp",
    "timestamp": "1746794748692"
}
#rifle_weapons_list=['weapon_m4a1_silencer','weapon_galilar','weapon_scar20','weapon_ak47','weapon_famas','weapon_m4a1','weapon_sg556','weapon_ssg08','weapon_aug','weapon_g3sg1']
#SubmachineList=['weapon_p90','weapon_mac10','weapon_ump45','weapon_mp7','weapon_bizon','weapon_mp9','weapon_mp5sd']
#SubmachineList=['weapon_mp9','weapon_mp5sd']
#knife_list=['weapon_knife_survival_bowie','weapon_knife_butterfly','weapon_knife_falchion','weapon_knife_flip','weapon_knife_gut','weapon_knife_tactical','weapon_knife_m9_bayonet','weapon_bayonet','weapon_knife_karambit','weapon_knife_push','weapon_knife_stiletto','weapon_knife_ursus','weapon_knife_gypsy_jackknife','weapon_knife_widowmaker','weapon_knife_css','weapon_knife_cord','weapon_knife_canis','weapon_knife_outdoor','weapon_knife_skeleton','weapon_knife_kukri']
#pistol_list=['weapon_cz75a','weapon_tec9','weapon_revolver','weapon_deagle','weapon_elite']
#pistol_list=['weapon_hkp2000','weapon_usp_silencer','weapon_glock','weapon_p250','weapon_fiveseven',]
#shogun_list=['weapon_mag7']
machine_gun=['weapon_m249','weapon_negev']
MVP=''
for k in machine_gun:
    params['category']=k
    with open(k,"w") as fd:
        for i in range(1, 1000):

            params['page'] = i
            response = requests.get(url, params=params, headers=headers)
            response_json = response.content
            Content_Length = len(response_json)
            if Content_Length == 58:
                print('没了')
                break
            toDict = simplejson.loads(response_json)
            skin_list = toDict['data']['list']
            for j in skin_list:
                print(j['goodsName'])
                fd.write(j['goodsName']+"\n")
            # print(skin_list)
            # print(response.status_code)
            # print(response.json())

            random_time = random.randint(10, 20)
            time.sleep(random_time)


# 输出 JSON 数据
