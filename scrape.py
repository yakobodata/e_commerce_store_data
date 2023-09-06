import requests
import json
import numpy as np
import pandas as pd
from time import sleep
data = []

for page in range(18406):
    cookies = {
        'first_visit': '1688760304',
        'app': '8ae4b4f9e0514c1a8e2b0d2c6cb1d511',
        'uid': '07aa95bd9d675ff474cc1daa94fa3f7fc5aab9fd',
        'lang': 'en',
        'MgidSensorNVis': '70',
        'MgidSensorHref': 'https://jiji.ug/home-garden',
        '_ga': 'GA1.2.419471541.1688760310',
        '_gcl_au': '1.1.1493704520.1688760310',
        '_ga_XSRWECBEVV': 'GS1.1.1690203020.7.1.1690203028.52.0.0',
        '_fbp': 'fb.1.1689880058448.1032111111',
        'g_state': '{i_l:1,i_p:1690186654444}',
        'change-language-popup': '1',
        'intercom-device-id-ugmhsbgy': '81311081-197d-4d3f-a16c-27ddabf6ddb9',
        'MgidSensorUtmSource': 'google_adw',
        'MgidSensorClidV': '0',
        '_gcl_aw': 'GCL.1690193704.Cj0KCQjwwvilBhCFARIsADvYi7IxmsPqovdvFeYwKWqlcJXsyt0HDd5y6p_Ox3HE8dLXHG7Asij_ciMaArp0EALw_wcB',
        '_gac_UA-137059257-3': '1.1690193704.Cj0KCQjwwvilBhCFARIsADvYi7IxmsPqovdvFeYwKWqlcJXsyt0HDd5y6p_Ox3HE8dLXHG7Asij_ciMaArp0EALw_wcB',
        '__gads': 'ID=a0c6915ec333378b-22ab54274be0009a:T=1692131546:RT=1692133878:S=ALNI_MZ3gXdipaUeLooX4pq4tmXcLy5pyw',
        '__gpi': 'UID=00000c88eaebc603:T=1692131546:RT=1692133878:S=ALNI_MZFUsKEJ3frk1--bJAfkQorgoY5KQ',
        'alerts_actualized': '1',
        'intercom-session-ugmhsbgy': 'VkdPdDR2cWI1aTFHTE1LM2Iya3UwNjNoTEhETGEwaStrbVhpSmtyZVhnTzduTmo2ODB4Sk5jOGdtZmxFaUJqcy0tVno2VkVQMWtVNklCcmhjYmFVWlRQUT09--386e570b1d8e8f9f500bbed977660c457bb60dc9',
        'rid': 'jiji.ug',
        '_js2': 'NgYgnxeY8dcAtacAwEQ43qqXxGWg6LFgcUPaBOtfkhU^%^3D',
        'app_sid': '1693130479946',
        '_js2': 'NgYgnxeY8dcAtacAwEQ43qqXxGWg6LFgcUPaBOtfkhU=',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://jiji.ug/home-garden',
        'X-CSRF-Token': 'IjE1MDg0ZGNhYmRiNDViZTMxZTY2ZDEwODRlYjk5ZjYxMjBiMjRkNDIi.ZOsfcw.8TkU8J2-r1KWgZ7dYuLUdEhzItg',
        'Connection': 'keep-alive',
        # 'Cookie': 'first_visit=1688760304; app=8ae4b4f9e0514c1a8e2b0d2c6cb1d511; uid=07aa95bd9d675ff474cc1daa94fa3f7fc5aab9fd; lang=en; MgidSensorNVis=70; MgidSensorHref=https://jiji.ug/home-garden; _ga=GA1.2.419471541.1688760310; _gcl_au=1.1.1493704520.1688760310; _ga_XSRWECBEVV=GS1.1.1690203020.7.1.1690203028.52.0.0; _fbp=fb.1.1689880058448.1032111111; g_state={i_l:1,i_p:1690186654444}; change-language-popup=1; intercom-device-id-ugmhsbgy=81311081-197d-4d3f-a16c-27ddabf6ddb9; MgidSensorUtmSource=google_adw; MgidSensorClidV=0; _gcl_aw=GCL.1690193704.Cj0KCQjwwvilBhCFARIsADvYi7IxmsPqovdvFeYwKWqlcJXsyt0HDd5y6p_Ox3HE8dLXHG7Asij_ciMaArp0EALw_wcB; _gac_UA-137059257-3=1.1690193704.Cj0KCQjwwvilBhCFARIsADvYi7IxmsPqovdvFeYwKWqlcJXsyt0HDd5y6p_Ox3HE8dLXHG7Asij_ciMaArp0EALw_wcB; __gads=ID=a0c6915ec333378b-22ab54274be0009a:T=1692131546:RT=1692133878:S=ALNI_MZ3gXdipaUeLooX4pq4tmXcLy5pyw; __gpi=UID=00000c88eaebc603:T=1692131546:RT=1692133878:S=ALNI_MZFUsKEJ3frk1--bJAfkQorgoY5KQ; alerts_actualized=1; intercom-session-ugmhsbgy=VkdPdDR2cWI1aTFHTE1LM2Iya3UwNjNoTEhETGEwaStrbVhpSmtyZVhnTzduTmo2ODB4Sk5jOGdtZmxFaUJqcy0tVno2VkVQMWtVNklCcmhjYmFVWlRQUT09--386e570b1d8e8f9f500bbed977660c457bb60dc9; rid=jiji.ug; _js2=NgYgnxeY8dcAtacAwEQ43qqXxGWg6LFgcUPaBOtfkhU^%^3D; app_sid=1693130479946; _js2=NgYgnxeY8dcAtacAwEQ43qqXxGWg6LFgcUPaBOtfkhU=',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'slug': 'home-garden',
        'init_page': 'true',
        'page': page,
        'webp': 'true',
    }

    response = requests.get('https://jiji.ug/api_web/v1/listing', params=params, cookies=cookies, headers=headers)


    # Assuming response_text contains the JSON data as a string
    response_json = json.loads(response.text)

    try:

        products = response_json['adverts_list']['adverts']

        # print(keys[0])

        for product in products:
            # sleep(5)
            # category_name
            try:
                category_name = product['fb_view_content_data']['content_category']
                print(category_name)
            except:
                category_name = np.nan
            
            #product_name
            try:
                product_name = product['fb_view_content_data']['content_name']
                print(product_name)
            except:
                product_name = np.nan
                

            #product_image
            try:
                product_image = product['image_obj']['url']
                print(product_image)
            except:
                product_image = np.nan
                

            #package_info
            try:
                package_info = product['paid_info']['package_type']
                print(package_info)
            except:
                package_info = np.nan
                # continue

            #price
            # print(product['price_obj']['view'])
            try:
                price = product['price_obj']['view']
                print(price)
            except:
                price = np.nan

            #phone
            
            try:
                phone = product['user_phone']
                print(phone)
            except:
                phone = np.nan

            # description
            try:
                desc = product['short_description']
                print(desc)
            except:
                desc = np.nan

            data.append({"category_name":category_name,"product_name":product_name,"product_image":product_image
                        ,"package_info":package_info
                        ,"price":price
                        ,"phone":phone
                        ,"desc":desc
                        ,"page_number":page})
    except:
        break

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
# Export the DataFrame to a CSV file
df.to_csv('output_2.csv', index=False)
