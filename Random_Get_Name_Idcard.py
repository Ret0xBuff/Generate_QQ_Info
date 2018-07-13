# -*- coding:utf-8 -*-


import sys,os
import random
import string

reload(sys)
sys.setdefaultencoding("utf-8")

code = {}
file = './source/chinacode.txt'
x_str = u"张-陈-李-王-杨-刘-赵-徐-邓-何-孙-周"
man_m_str = u"嘉文-一凡-昊楠-鑫龙-海宇-子君-露桐-柏辉-其贤"
woman_m_str = u"雅菲-叶妃-娅雨-霞月-晟曦-静菡-梓妤-文嫣-春艳"

def read_code(file):
    global code
    f = open(file,'r')
    for n in f.readlines():
        line = n.split('----')
        code[line[0]] = line[1].replace('\n','')
    f.close()

def calculation(idcard):
    sum = int(idcard[0])*7 + int(idcard[1])*9 + int(idcard[2])*10 + int(idcard[3])*5 + int(idcard[4])*8 + \
        int(idcard[5])*4 + int(idcard[6])*2 + int(idcard[7])*1 + int(idcard[8])*6 + int(idcard[9])*3 + \
        int(idcard[10])*7 + int(idcard[11])*9 + int(idcard[12])*10 + int(idcard[13])*5 + int(idcard[14])*8 + \
        int(idcard[15])*4 + int(idcard[16])*2
    remainder = sum%11
    return remainder

def check_code(remainder):
    remainder = str(remainder)
    code = {'0':'1','1':'0','2':'X','3':'9','4':'8',
    '5':'7','6':'6','7':'5','8':'4','9':'3','10':'2'}
    check_code = code[remainder]
    return check_code

def Random_Get_Name_Idcard(file,x_str,man_m_str,woman_m_str):
    global code
    read_code(file)
    code_keys = random.choice(code.keys())
    year = random.randint(1970,1997)
    month = random.choice(['01','03','08','10','12'])
    day = random.choice(['01','03','08','10','12','15','18','25','27'])
    num = random.randint(100,800)
    idcard = code_keys + str(year) + month + day + str(num)
    sex = idcard[-1:]
    if int(sex)%2 ==0:
        name = random.choice(x_str.split('-')) + random.choice(woman_m_str.split('-'))
    else:
        name = random.choice(x_str.split('-')) + random.choice(man_m_str.split('-'))
    remainder = calculation(idcard)
    check_code_0 = check_code(remainder)
    idcard = idcard + check_code_0
    #print name 
    #print idcard
    return name + "----" + idcard

#Random_Get_Name_Idcard(file,x_str,man_m_str,woman_m_str)

#生成随机密码
def random_password():
    key_length = 9
    all_num = []
    all_lowercase = []
    all_uppercase = []
    all_symbol = ['!','@','#','$','%','&','*','_','-']

    #去除容易写错的字符
    for i in range(len(string.digits)):
        if string.digits[i] not in ['0','1']:
            all_num.append(string.digits[i])

    for i in range(len(string.lowercase)):
        if string.lowercase[i] not in ['o','l','i','j']:
            all_lowercase.append(string.lowercase[i])

    for i in range(len(string.uppercase)):
        if string.uppercase[i] not in ['O','L','I','J']:
            all_uppercase.append(string.uppercase[i])

    #for i in range(len(string.punctuation)):
        #if string.punctuation[i] not in ['!','"','%',"'",'<','>']:
            #all_symbol.append(string.punctuation[i])

    #print all_num
    #print all_lowercase
    #print all_uppercase
    #print all_symbol

    one_num = random.choice(all_num)
    one_lowercase = random.choice(all_lowercase)
    one_uppercase = random.choice(all_uppercase)
    one_symbol = random.choice(all_symbol)

    password = [one_num,one_lowercase,one_uppercase,one_symbol]

    for n in range(key_length-4):
        password.append(random.choice(random.choice([all_num,all_lowercase,all_uppercase,all_symbol])))

    format_password = string.join(random.sample(password,key_length)).replace(" ","")

    #print format_password
    return format_password
	
#random_password()

#随机出QQ密保问题，答案固定
def random_question():
    all_question = [u"您母亲的姓名是？----大乔",u"您配偶的生日是？----19960518",
    u"您的学号(或工号)是？----99",
	u"您高中班主任的名字是？----狄仁杰",
    u"您父亲的姓名是？----姜子牙",
	u"您小学班主任的名字是？----后羿",
    u"您父亲的生日是？----19951212",
	u"您配偶的姓名是？----孙尚香",
    u"您初中班主任的名字是？----赵云",
	u"您最熟悉的童年好友名字是？----亚瑟",
    u"您最熟悉的学校宿舍室友名字是？----张飞"]

    get_question = random.sample(all_question,3)
    #print get_question
    return get_question

#random_question()

qq_number = "8888888888"
mobile_number = "15555555555"
line_number = 10     #一次性生成多少条记录

for n in range(line_number):
    get_question = ""
    for m in random_question():
        get_question = get_question + m + "----"
    #print get_question
    recode = qq_number + '----' + random_password() + "----" + get_question + mobile_number + "----" + Random_Get_Name_Idcard(file,x_str,man_m_str,woman_m_str) + '\n\n'
    #print recode
    with open(".//temp.txt",'a+') as f:
        f.write(recode)

os.system('%s\\QQ_INFO.txt'%(os.getcwd()))







