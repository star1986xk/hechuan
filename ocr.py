# -*- coding: utf-8 -*-
import requests
import base64
import os


class ocrclass(object):

    def get_token(self):
        get_token_data = {
            'grant_type': 'client_credentials',
            'client_id': 'ax2GW9oyT1TpEbkEt6wltBRM',
            'client_secret': 'CjBL22E4tpwuTPYyiXcWyFAs9CWAaUv5',
        }
        get_token_url = 'https://aip.baidubce.com/oauth/2.0/token'
        response = requests.post(get_token_url, data=get_token_data,verify=False)
        return response.json()['access_token']

    def get_img_base64(self, img_path):
        with open(img_path, 'rb') as f:
            return base64.b64encode(f.read())

    def ocr(self, type, img):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        if type == 'url':
            ocr_data = {
                'access_token': '24.e8503f58b7a05ed1a6f1e7f4e6687572.2592000.1576723889.282335-17802472',
                'url': img
            }
        elif type == 'image':
            ocr_data = {
                'access_token': '24.e8503f58b7a05ed1a6f1e7f4e6687572.2592000.1576723889.282335-17802472',
                'image': img
            }
        ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
        response = requests.post(ocr_url, headers=headers, data=ocr_data,verify=False)
        return response.json()['words_result']

    # 执行主函数
    def ocr_run(self):
        try:
            word = self.ocr('image', self.get_img_base64('1.jpg'))
            return word[0]['words']
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':

    ocr_obj = ocrclass()
    mail = ocr_obj.ocr_run()
    print(mail)

