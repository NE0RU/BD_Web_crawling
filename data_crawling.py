from selenium import webdriver as wb
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from pymongo import MongoClient

my_client = MongoClient("mongodb://localhost:27017/")
mydb = my_client['Anawa']

cpu = mydb['cpu']
cpu_Cooler = mydb['cpu_Cooler']
board = mydb['board']
ram = mydb['ram']
gpu = mydb['gpu']
ssd = mydb['ssd']
hdd = mydb['hdd']
case = mydb['case']
power = mydb['power']

# cpu(1,25), cpu_Cooler(1,146), board(1,48), ram(1,43), gpu(1,40), ssd(1,80), hdd(1,37), cas(1,64), power(1,48) 2020.11.25
cpu_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=873&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=CPU&productRegisterAreaSeq=1&categorySeq1=861&categorySeq2=873&categorySeq3=0&categorySeq4=0&selectOptionList[]=40&selectOptionList[]=312287&selectOptionList[]=41&selectOptionList[]=51&selectOptionList[]=45&selectOptionList[]=15444&selectOptionList[]=46&selectOptionList[]=44&selectOptionList[]=47&selectOptionList[]=15570&selectOptionList[]=32302&selectOptionList[]=53&selectOptionList[]=319006&goodsCount=696&page='
cpu_Cooler_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=887&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=%EC%BF%A8%EB%9F%AC%2F%ED%8A%9C%EB%8B%9D&productRegisterAreaSeq=14&categorySeq1=862&categorySeq2=887&categorySeq3=0&categorySeq4=0&selectOptionList[]=687&selectOptionList[]=315758&selectOptionList[]=688&selectOptionList[]=691&selectOptionList[]=693&selectOptionList[]=21022&selectOptionList[]=11014&selectOptionList[]=11012&selectOptionList[]=15081&selectOptionList[]=18727&selectOptionList[]=31279&selectOptionList[]=6805&selectOptionList[]=6806&selectOptionList[]=32780&selectOptionList[]=20520&goodsCount=4335&page='
board_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=875&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=%EB%A9%94%EC%9D%B8%EB%B3%B4%EB%93%9C&productRegisterAreaSeq=2&categorySeq1=861&categorySeq2=875&categorySeq3=0&categorySeq4=0&selectOptionList[]=499&selectOptionList[]=500&selectOptionList[]=504&selectOptionList[]=506&selectOptionList[]=13029&selectOptionList[]=509&selectOptionList[]=508&selectOptionList[]=510&selectOptionList[]=8856&selectOptionList[]=512&selectOptionList[]=6204&selectOptionList[]=24942&selectOptionList[]=8931&selectOptionList[]=516&selectOptionList[]=519&selectOptionList[]=6092&selectOptionList[]=6205&selectOptionList[]=30357&selectOptionList[]=37977&selectOptionList[]=21207&goodsCount=1395&page='
ram_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=874&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=%EB%A9%94%EB%AA%A8%EB%A6%AC&productRegisterAreaSeq=3&categorySeq1=861&categorySeq2=874&categorySeq3=0&categorySeq4=0&selectOptionList[]=278&selectOptionList[]=277&selectOptionList[]=282&selectOptionList[]=279&selectOptionList[]=283&selectOptionList[]=15079&selectOptionList[]=15080&selectOptionList[]=6200&selectOptionList[]=312860&selectOptionList[]=38276&selectOptionList[]=38560&goodsCount=1246&page='
gpu_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=876&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=%EA%B7%B8%EB%9E%98%ED%94%BD%EC%B9%B4%EB%93%9C&productRegisterAreaSeq=4&categorySeq1=861&categorySeq2=876&categorySeq3=0&categorySeq4=0&selectOptionList[]=654&selectOptionList[]=655&selectOptionList[]=6857&selectOptionList[]=658&selectOptionList[]=657&selectOptionList[]=659&selectOptionList[]=6858&selectOptionList[]=665&selectOptionList[]=661&selectOptionList[]=663&selectOptionList[]=664&selectOptionList[]=6201&selectOptionList[]=6574&selectOptionList[]=680&selectOptionList[]=16333&selectOptionList[]=20550&selectOptionList[]=31689&selectOptionList[]=7599&selectOptionList[]=321985&selectOptionList[]=684&selectOptionList[]=666&selectOptionList[]=682&selectOptionList[]=32778&selectOptionList[]=37388&selectOptionList[]=32182&selectOptionList[]=321958&goodsCount=1141&page='
ssd_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=32617&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=SSD&productRegisterAreaSeq=16&categorySeq1=861&categorySeq2=32617&categorySeq3=0&categorySeq4=0&selectOptionList[]=14689&selectOptionList[]=14695&selectOptionList[]=14690&selectOptionList[]=14691&selectOptionList[]=14694&selectOptionList[]=33312&selectOptionList[]=14696&selectOptionList[]=14811&selectOptionList[]=33313&selectOptionList[]=14692&selectOptionList[]=14693&selectOptionList[]=30722&selectOptionList[]=30833&selectOptionList[]=14810&selectOptionList[]=313592&selectOptionList[]=14697&goodsCount=2354&page='
hdd_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=877&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=%ED%95%98%EB%93%9C%EB%94%94%EC%8A%A4%ED%81%AC&productRegisterAreaSeq=5&categorySeq1=861&categorySeq2=877&categorySeq3=0&categorySeq4=0&selectOptionList[]=788&selectOptionList[]=793&selectOptionList[]=790&selectOptionList[]=789&selectOptionList[]=791&selectOptionList[]=792&selectOptionList[]=310922&goodsCount=1069&page='
case_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=879&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=%EC%BC%80%EC%9D%B4%EC%8A%A4&productRegisterAreaSeq=7&categorySeq1=861&categorySeq2=879&categorySeq3=0&categorySeq4=0&selectOptionList[]=973&selectOptionList[]=974&selectOptionList[]=977&selectOptionList[]=6196&selectOptionList[]=991&selectOptionList[]=24679&selectOptionList[]=32072&selectOptionList[]=38704&selectOptionList[]=995&selectOptionList[]=996&selectOptionList[]=997&selectOptionList[]=998&selectOptionList[]=999&selectOptionList[]=7437&selectOptionList[]=1009&selectOptionList[]=21573&selectOptionList[]=29061&selectOptionList[]=35342&selectOptionList[]=35343&selectOptionList[]=66325&selectOptionList[]=39662&selectOptionList[]=39876&selectOptionList[]=38702&selectOptionList[]=7254&goodsCount=1890&page='
power_url = 'http://shop.danawa.com/virtualestimate/?&controller=estimateMain&methods=product&categorySeq=880&categoryDepth=2&marketPlaceSeq=16&sellerSeq=0&pseq=2&name=&listPerPage=30&attribute=&makerCode=&brandCode=&serviceSectionSeq=0&productRegisterAreaGroupSeq=0&ignoreKeywordYN=N&preparationSale=&tabOrderbyYn=N&suggestName=&displayOptionCount=3&categoryName=%ED%8C%8C%EC%9B%8C&productRegisterAreaSeq=8&categorySeq1=861&categorySeq2=880&categorySeq3=0&categorySeq4=0&selectOptionList[]=1086&selectOptionList[]=1088&selectOptionList[]=1090&selectOptionList[]=1091&selectOptionList[]=1093&selectOptionList[]=28622&selectOptionList[]=6198&selectOptionList[]=40062&selectOptionList[]=13033&selectOptionList[]=20905&selectOptionList[]=15039&selectOptionList[]=315140&goodsCount=1405&page='

driver = wb.Chrome()

def crawling(x, y, get_url, get_db) :
    for i in range(x, y):
        url = get_url + str(i)

        driver.get(url)
    
        soup = bs(driver.page_source,'html.parser')

        name_list = []
        spec_list = []
        price_list = []
    
        name_tag_list = soup.select('p.subject > a')
        for name_tag in name_tag_list:
            name_list.append(name_tag.text)

        spec_tag_list = soup.select('div.spec_bg > a')
        for spec_tag in spec_tag_list:
            spec_list.append(spec_tag.text)

        price_tag_list = soup.select('td.rig_line > p')
        for price_tag in price_tag_list:
            price_list.append(price_tag.text)

        spec_list = spec_list[2:]
        name_list = name_list[2:]
        price_list = price_list[2:]

        for index in range(0, len(name_list)):
            get_db.insert_one({"name":name_list[index], "spec":spec_list[index], "price":price_list[index]})

crawling(1,11,cpu_url,cpu)
crawling(1,11,cpu_Cooler_url,cpu_Cooler)
crawling(1,11,board_url,board)
crawling(1,11,ram_url,ram)
crawling(1,11,gpu_url,gpu)
crawling(1,11,ssd_url,ssd)
crawling(1,11,hdd_url,hdd)
crawling(1,11,case_url,case)
crawling(1,11,power_url,power)