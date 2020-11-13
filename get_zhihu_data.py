import requests
from lxml import etree 
import time
from datetime import datetime
from pymongo import MongoClient

my_cookie = '_zap=28053435-193c-4dd4-a3f5-8914dc54814c; _xsrf=8960d455-58be-4551-8de8-511333b89c2b; d_c0="AEAsQwFvhw-PTuPVi4tX9-c_j2b54uDNAKI=|1559566833"; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20140903=1^3=entry_date=20140903=1; l_n_c=1; n_c=1; tshl=; _ga=GA1.2.541885426.1559579800; __utma=51854390.541885426.1559579800.1589088624.1589646166.17; __utmz=51854390.1589646166.17.4.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/141461214/edit; z_c0="2|1:0|10:1596202034|4:z_c0|92:Mi4xeklCNEFBQUFBQUFBUUN4REFXLUhEeVlBQUFCZ0FsVk5NbW9SWUFCcFFhRHdwUlJvYTVreFJwcldXMUJvQzNITllR|bae15805516c97b330e3798fa839d7c926cde0b9584eac3ec510a2535d394766"; q_c1=59e2ad7bca3845ffb33a420bdc587550|1604260583000|1559568677000; tst=h; SESSIONID=TLBZ7kX6r1rfhzpXDnFwGrINaJ8hbiCRJKy2OGUGH7V; JOID=VVEWAkxpCfFF9IL4LW9nKDZ_fmc4M0-xGcPnqhkbNokhmviGf3ryVhz6hvApLJ-R2IaVaw9GkF5m27AW63UbxbM=; osd=VVwSBE9pBPVD94L1KWlkKDt7eGQ4Pku3GsPqrh8YNoQlnPuGcn70VRz3gvYqLJKV3oWVZgtAk15r37YV63gfw7A=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1604582338,1604582367,1604582697,1604582701; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1604583110; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1604584347|1604578506'

cur_headers = {
    "cookie":my_cookie,
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"
}

question_headers = {
    "cookie":'SESSIONID=ISx69CtZDS6MILq3ofTsmgnnCBQBVqkf8CR8WuAvbkz; JOID=V1kQA0zPXRAc2k2sVco7zWZXsjtEnxVXQe8i8Ga_aGZ_tTXYCRCnsUbcTa1Xt6gLboJNIE8Q4OkaONyPGa3uhtc=; osd=VVkWAUrNXRYe3E-sU8g9z2ZRsD1GnxNVR-0i9mS5amZ5tzPaCRalt0TcS69RtagNbIRPIEkS5usaPt6JG63ohNE=; _zap=28053435-193c-4dd4-a3f5-8914dc54814c; _xsrf=8960d455-58be-4551-8de8-511333b89c2b; d_c0="AEAsQwFvhw-PTuPVi4tX9-c_j2b54uDNAKI=|1559566833"; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20140903=1^3=entry_date=20140903=1; l_n_c=1; n_c=1; tshl=; _ga=GA1.2.541885426.1559579800; __utma=51854390.541885426.1559579800.1589088624.1589646166.17; __utmz=51854390.1589646166.17.4.utmcsr=zhuanlan.zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/p/141461214/edit; z_c0="2|1:0|10:1596202034|4:z_c0|92:Mi4xeklCNEFBQUFBQUFBUUN4REFXLUhEeVlBQUFCZ0FsVk5NbW9SWUFCcFFhRHdwUlJvYTVreFJwcldXMUJvQzNITllR|bae15805516c97b330e3798fa839d7c926cde0b9584eac3ec510a2535d394766"; q_c1=59e2ad7bca3845ffb33a420bdc587550|1604260583000|1559568677000; tst=h; SESSIONID=TLBZ7kX6r1rfhzpXDnFwGrINaJ8hbiCRJKy2OGUGH7V; JOID=VVEWAkxpCfFF9IL4LW9nKDZ_fmc4M0-xGcPnqhkbNokhmviGf3ryVhz6hvApLJ-R2IaVaw9GkF5m27AW63UbxbM=; osd=VVwSBE9pBPVD94L1KWlkKDt7eGQ4Pku3GsPqrh8YNoQlnPuGcn70VRz3gvYqLJKV3oWVZgtAk15r37YV63gfw7A=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1604582338,1604582367,1604582697,1604582701; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1604584407|1604578506; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1604584408',
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"    
}

## This part deal with zhihu api and get data
## zhihu use dynimactic page, so it's diffcult to capture description of title

# get hot questions for now
def get_hot_questions():
    r=requests.get('https://www.zhihu.com/hot',headers=cur_headers)
    if r.status_code!=200:
        print("error response")
        return []
    html = etree.HTML(r.text)
    link_list = html.xpath('//*[@id="TopstoryContent"]/div/div/div[2]/section/div[2]/a/@href')

    questions = []
    for i in range(len(link_list)):
        link = link_list[i]
        if "question" not in link:
            continue
        items = link.split("/")
        for item in items:
            if item.isdigit():
                questions.append((item,link))
    return questions

# 基于driver获取answer内容
def get_question_page_content_by_driver(driver, question_link):
    driver.get(question_link)
    time.sleep(3)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)
    return driver.page_source

# 基于requests包获取answer内容： 目前只能获取到5个，但是相比而言速度更快 
def get_question_page_content_from_request(question_link):
    r=requests.get(question_link,headers=question_headers)
    if r.status_code!=200:
        print("error response")
        return []
    return r.text

# 从爬取的网页中，获取到回答信息
def get_answers(raw):
    html = etree.HTML(raw)
    # what we want
    question_title = ''
    good_answers = []
    # if zhihu changed it's html format we need to know and also change
    question_title = html.xpath('//*[@class="QuestionHeader-title"]')[0].text
    good_answers_content = html.xpath('//*[@class="RichContent-inner"]/span')
    for good_answer_content in good_answers_content:
        good_answer_ori = [] 
        for child in good_answer_content:
            content = child.text
            if content != None:
                good_answer_ori.append(content)
        good_answers.append("\n".join(good_answer_ori))
    return question_title,good_answers

def get_data_and_insert_data(hot_answer):
    questions = get_hot_questions()
    for question in questions:
        question_no = question[0]
        question_link = question[1]

        # find question_no in database, if question_no exist continue
        if hot_answer.find_one({"question_no":question_no}) != None:
            continue
        
        # get page in answer
        answer_page = get_question_page_content_from_request(question_link)
        question_title,answers = get_answers(answer_page)

        # insert answers in database
        hot_answer.insert_one({
            "question_no":question_no,
            "question_title":question_title,
            "answers":answers,
            "insert_time": str(datetime.now().time())
        })

# main task
# get data per hour

# not in use, driver with a lot problem
# driver = webdriver.Chrome(ChromeDriverManager().install())

# init mongo client to store data
client = MongoClient("localhost",61003)
db = client['zhihu_data']
hot_answer = db.zhihu_hot_answer

while True:
    print("get and insert",datetime.now())
    get_data_and_insert_data(hot_answer)
    time.sleep(3600)