import requests
import time
import os


class ImageCrawlerTool(object):
    def __init__(self):
        self.host_url = 'https://image.baidu.com/search/acjson?'

        self.headers = {
            'Cookie' :'BDqhfp=%E5%90%91%E6%97%A5%E8%91%B5%26%26-10-1undefined%26%269072%26%269; PSTM=1611916498; BIDUPSID=98B368A119F8B9806DF2A21077684622; __yjs_duid=1_ace0ec46407c1d2776d16f75ad1cd6f91619918680426; BAIDUID=200C8C7670025CB12EF7379591C9EC25:FG=1; BDUSS=VpWks3WFExZEsya3phSjFZMjVZYUJ5NjRwTXZTfmtUaDFvfk5XSVdrOXplZlZnRUFBQUFBJCQAAAAAAAAAAAEAAACXRsIrZ29kenp1MTk5MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHPszWBz7M1gZX; BDUSS_BFESS=VpWks3WFExZEsya3phSjFZMjVZYUJ5NjRwTXZTfmtUaDFvfk5XSVdrOXplZlZnRUFBQUFBJCQAAAAAAAAAAAEAAACXRsIrZ29kenp1MTk5MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHPszWBz7M1gZX; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=34130_34099_34225_31253_34004_34112_33607_34106_34135; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=1; BA_HECTOR=0l04ag8h8001848leq1ge02cp0q; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; indexPageSugList=%5B%22%E5%90%91%E6%97%A5%E8%91%B5%22%2C%22%E6%B4%8B%E8%91%B1%22%5D; cleanHistoryStatus=0; ab_sr=1.0.1_OWY0YzRiN2JiN2YxNDcwODg1ZDliZWYxYWNlZDBiZmQyMjE4ZGNhMjM4NTYwNThhYjIzNjEzOWY4ZmY2NDU1ZTM1ZDJiZmY2YjY1MjM4MDNlMmJlOWU5YTQ2ZDhhMjRkODAzMTcwZTBmMTIzYzE4NjRhNjc3ZTNlNjc4ZDBmMTBmYzgwYjkwNzM0OGZiYjZiNmQwMWM3OWJiZTIwMGVkMmFhMmJmZWFhYzgwOTFhYWM2NjA5NjAwN2E3YWU4Zjdi',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
        }

        self.params = {
            'tn': 'resultjson_com',
            'logid': '11932378203341346473',
            'ipn': 'rj',
            'ct': '201326592',
            'is': '',
            'fp': 'result',
            'queryWord': '',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf - 8',
            'oe': 'utf - 8',
            'adpicid': '',
            'st': '-1',
            'z': '',
            'ic': '2',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': '',
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': '0',
            'istype': '2',
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'nojc': '',
            'acjsonfr': 'click',
            'pn': '',
            'rn': '30',
            'gsm': '3c',
            'time': ''
        }
        self.image_url_list = []

    def get_image_url_list(self, keyword, pages):
        for i in range(0, pages):
            self.params['time'] = int(time.time() * 1000)
            self.params['pn'] = (i+50)*30
            self.params['keyword'] = keyword
            self.params['word'] = keyword
            response = requests.get(url=self.host_url, headers=self.headers, params=self.params)
            for j in range(0, len(response.json()['data']) - 1):
                self.image_url_list.append(response.json()['data'][j]['thumbURL'])

        print(len(self.image_url_list))

    def download_image(self, root_path):

        if not os.path.exists(root_path):
            os.makedirs(root_path)

        con_path = '{}/{}/'.format
        target_path = con_path(root_path,self.params['keyword'])
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        initial_image_num = 1
        for url in self.image_url_list:
            image = requests.get(url=url)
            with open('{}{}.jpg'.format(target_path, initial_image_num), 'wb') as file:
                file.write(image.content)
            initial_image_num += 1


if __name__ == '__main__':
    crawler = ImageCrawlerTool()
    crawler.get_image_url_list(keyword='向日葵', pages=10)
    crawler.download_image(root_path='./data_set')
