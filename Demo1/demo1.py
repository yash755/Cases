import requests
import json
from bs4 import BeautifulSoup
import csv
import time


file = open('name.txt','r')


for f in file:
    name_fin = f
    name_fin = name_fin.replace('\n','')

    url = 'https://cpdocket.cp.cuyahogacounty.us'
    payload = {}
    headers = {}


    proxies = {
        "https": "https://159.65.69.186:9300",
    }


    s = requests.Session()

    response = s.get(url)
    cookies = response.cookies
    html = BeautifulSoup(response.content, 'html.parser')



    payload_element2 = html.find("input", {'id': '__EVENTVALIDATION'})
    payload_element3 = html.find("input", {'id': '__VIEWSTATE'})
    payload_element4 = html.find("input", {'id': '__VIEWSTATEGENERATOR'})
    payload_element5 = html.find("input", {'id': 'SheetContentPlaceHolder_btnYes'})

    payload["__EVENTARGUMENT"] = ''
    payload["__EVENTTARGET"] = ''
    payload["__EVENTVALIDATION"] = str(payload_element2.get('value'))
    payload["__VIEWSTATE"] = str(payload_element3.get('value'))
    payload["__VIEWSTATEGENERATOR"] = str(payload_element4.get('value'))
    payload["ctl00$SheetContentPlaceHolder$btnYes"] = str(payload_element5.get('value'))

    url = 'https://cpdocket.cp.cuyahogacounty.us/'
    response1 = s.post(url, data=payload, cookies=cookies)

    cookies1 = response1.cookies
    html1 = BeautifulSoup(response1.content, 'html.parser')




    payload_element10 = html1.find("input", {'id': '__EVENTVALIDATION'})
    payload_element11 = html1.find("input", {'id': '__VIEWSTATE'})
    payload_element12 = html1.find("input", {'id': '__VIEWSTATEGENERATOR'})

    payload1 = {}
    payload1["__EVENTVALIDATION"] = str(payload_element10.get('value'))
    payload1["__VIEWSTATE"] = str(payload_element11.get('value'))
    payload1["__VIEWSTATEGENERATOR"] = str(payload_element12.get('value'))
    payload1["ctl00$SheetContentPlaceHolder$rbSearches"] = 'crname'

    url1 = 'https://cpdocket.cp.cuyahogacounty.us/Search.aspx'
    response2 = s.post(url1, data=payload1, cookies=cookies)

    cookies2 = response2.cookies

    html1 = BeautifulSoup(response2.content, 'html.parser')

    payload_element11 = html1.find("input", {'id': '__EVENTVALIDATION'})
    payload_element12 = html1.find("input", {'id': '__VIEWSTATE'})
    payload_element13 = html1.find("input", {'id': '__VIEWSTATEGENERATOR'})

    payload2 = {}
    payload2["__EVENTVALIDATION"] = str(payload_element11.get('value'))
    payload2["__VIEWSTATE"] = str(payload_element12.get('value'))
    payload2["__VIEWSTATEGENERATOR"] = str(payload_element13.get('value'))

    payload2["ctl00$SheetContentPlaceHolder$criminalNameSearch$btnSubmitName"] = 'Submit Search'
    payload2["ctl00$SheetContentPlaceHolder$criminalNameSearch$ddlFormatResults"] = '20'
    payload2["ctl00$SheetContentPlaceHolder$criminalNameSearch$grpType"] = 'rbAlpha'
    payload2["ctl00$SheetContentPlaceHolder$criminalNameSearch$txtLastName"] = str(name_fin)
    payload2["ctl00$SheetContentPlaceHolder$rbSearches"] = 'crname'

    url1 = 'https://cpdocket.cp.cuyahogacounty.us/Search.aspx'
    response3 = s.post(url1, data=payload2, cookies=cookies2)

    cookies3 = response3.cookies

    html3 = BeautifulSoup(response3.content, 'html.parser')



    payload_element14 = html3.find("input", {'id': '__EVENTVALIDATION'})
    payload_element15 = html3.find("input", {'id': '__VIEWSTATE'})
    payload_element16 = html3.find("input", {'id': '__VIEWSTATEGENERATOR'})

    payload3 = {}
    payload3["__EVENTVALIDATION"] = str(payload_element14.get('value'))
    payload3["__VIEWSTATE"] = str(payload_element15.get('value'))
    payload3["__VIEWSTATEGENERATOR"] = str(payload_element16.get('value'))
    payload3["__EVENTTARGET"] = 'ctl00$SheetContentPlaceHolder$ctl00$gvNameResults'
    payload3["__EVENTARGUMENT"] = 'Page$2'

    i = 2
    while i < 22:
        try:

            name = html3.find('a', {'id': 'SheetContentPlaceHolder_ctl00_gvNameResults_lbName_' + str(i-2)})
            name = name.text.strip()

            print (name)

            if i < 10:
                name_data = 'ctl00$SheetContentPlaceHolder$ctl00$gvNameResults$ctl0' + str(i) + '$lbName'
            else:
                name_data = 'ctl00$SheetContentPlaceHolder$ctl00$gvNameResults$ctl' + str(i) + '$lbName'


            payload5 = {}
            payload5["__EVENTTARGET"] = name_data
            payload5["__EVENTVALIDATION"] = str(payload_element14.get('value'))
            payload5["__VIEWSTATE"] = str(payload_element15.get('value'))
            payload5["__VIEWSTATEGENERATOR"] = str(payload_element16.get('value'))

            response5 = s.post('https://cpdocket.cp.cuyahogacounty.us/NameSearchResults.aspx', data=payload5, cookies=cookies3)
            html5 = BeautifulSoup(response5.content, 'html.parser')

            trs = html5.find_all('tr')

            if trs and len(trs) >= 2:

                payload_element18 = html5.find("input", {'id': '__EVENTVALIDATION'})
                payload_element19 = html5.find("input", {'id': '__VIEWSTATE'})
                payload_element20 = html5.find("input", {'id': '__VIEWSTATEGENERATOR'})

                payload6 = {}
                payload6["__EVENTTARGET"] = 'ctl00$SheetContentPlaceHolder$info$gvCaseResults$ctl02$lbCaseNum'
                payload6["__EVENTVALIDATION"] = str(payload_element18.get('value'))
                payload6["__VIEWSTATE"] = str(payload_element19.get('value'))
                payload6["__VIEWSTATEGENERATOR"] = str(payload_element20.get('value'))

                response8 = s.post('https://cpdocket.cp.cuyahogacounty.us/CaseInfoByName.aspx', data=payload6,
                                   cookies=cookies3)

                html6 = BeautifulSoup(response8.content, 'html.parser')

                link = html6.find('form').get('action')
                link = link.split('?')

                if len(link) >= 2:

                    response_final = s.get(
                        'https://cpdocket.cp.cuyahogacounty.us/CR_CaseInformation_Defendant.aspx?' + str(link[1]),
                        cookies=cookies3)
                    html_final = BeautifulSoup(response_final.content, 'html.parser')

                    trs_final = html_final.find_all('tr')

                    add1 = ''
                    add2 = ''
                    add3 = ''
                    dob = ''

                    for tr in trs_final:
                        tr_text = tr.text.strip()

                        if 'Address:' in tr_text:
                            tr_text = tr_text.replace('\n', '')
                            tr_text = tr_text.replace('\r', '')
                            tr_text = tr_text.replace('Address:', '')
                            tr_text = tr_text.lstrip()
                            if add1 == '':
                                add1 = tr_text

                        if 'Line 2:' in tr_text:
                            tr_text = tr_text.replace('\n', '')
                            tr_text = tr_text.replace('\r', '')
                            tr_text = tr_text.replace('Line 2:', '')
                            tr_text = tr_text.lstrip()
                            if add2 == '':
                                add2 = tr_text

                        if 'City, State, Zip:' in tr_text:
                            tr_text = tr_text.replace('\n', '')
                            tr_text = tr_text.replace('\r', '')
                            tr_text = tr_text.replace('City, State, Zip:', '')
                            tr_text = tr_text.lstrip()
                            if add3 == '':
                                add3 = tr_text

                        if 'DOB:' in tr_text:
                            tr_text = tr_text.replace('\n', '')
                            tr_text = tr_text.replace('\r', '')
                            tr_text = tr_text.replace('DOB:', '')
                            tr_text = tr_text.lstrip()
                            if dob == '':
                                dob = tr_text

                    for tr in trs:
                        try:
                            a_tag = tr.find('a')
                            if a_tag:

                                temp = []
                                temp.append(name)
                                temp.append(dob)
                                temp.append(add1)
                                temp.append(add2)
                                temp.append(add3)


                                temp.append(a_tag.text.strip())

                                tds = tr.find_all('td')

                                if len(tds) >= 3:

                                    temp.append(tds[2].text.strip())


                                arr = []
                                arr.append(temp)

                                with open('data1.csv', 'a+') as csvfile:
                                    csvwriter = csv.writer(csvfile)
                                    csvwriter.writerows(arr)

                                time.sleep(1)




                        except:
                            print ("A Error")




        except:
            print ("Error")

        i = i+1


    page = 3

    while True:
        print (page)
        response4 = s.post('https://cpdocket.cp.cuyahogacounty.us/NameSearchResults.aspx', data=payload3, cookies=cookies3)

        cookies3 = response4.cookies

        html3 = BeautifulSoup(response4.content, 'html.parser')

        # file = open('data.html','a+')
        # file.write(str(html3))
        # file.close()


        payload_element14 = html3.find("input", {'id': '__EVENTVALIDATION'})
        payload_element15 = html3.find("input", {'id': '__VIEWSTATE'})
        payload_element16 = html3.find("input", {'id': '__VIEWSTATEGENERATOR'})

        payload3 = {}
        payload3["__EVENTVALIDATION"] = str(payload_element14.get('value'))
        payload3["__VIEWSTATE"] = str(payload_element15.get('value'))
        payload3["__VIEWSTATEGENERATOR"] = str(payload_element16.get('value'))
        payload3["__EVENTTARGET"] = 'ctl00$SheetContentPlaceHolder$ctl00$gvNameResults'
        payload3["__EVENTARGUMENT"] = 'Page$' + str(page)

        page = page + 1


        if page >=8:

            j = 2
            while j < 22:
                try:

                    name = html3.find('a', {'id': 'SheetContentPlaceHolder_ctl00_gvNameResults_lbName_' + str(j - 2)})
                    name = name.text.strip()

                    print (name)



                    if j < 10:
                        name_data = 'ctl00$SheetContentPlaceHolder$ctl00$gvNameResults$ctl0' + str(j) + '$lbName'
                    else:
                        name_data = 'ctl00$SheetContentPlaceHolder$ctl00$gvNameResults$ctl' + str(j) + '$lbName'



                    payload5 = {}
                    payload5["__EVENTTARGET"] = name_data
                    payload5["__EVENTVALIDATION"] = str(payload_element14.get('value'))
                    payload5["__VIEWSTATE"] = str(payload_element15.get('value'))
                    payload5["__VIEWSTATEGENERATOR"] = str(payload_element16.get('value'))

                    response5 = s.post('https://cpdocket.cp.cuyahogacounty.us/NameSearchResults.aspx', data=payload5,
                                       cookies=cookies3)
                    html5 = BeautifulSoup(response5.content, 'html.parser')


                    trs = html5.find_all('tr')



                    if trs and len(trs) >=2:


                        payload_element18 = html5.find("input", {'id': '__EVENTVALIDATION'})
                        payload_element19 = html5.find("input", {'id': '__VIEWSTATE'})
                        payload_element20 = html5.find("input", {'id': '__VIEWSTATEGENERATOR'})

                        payload6 = {}
                        payload6["__EVENTTARGET"] = 'ctl00$SheetContentPlaceHolder$info$gvCaseResults$ctl02$lbCaseNum'
                        payload6["__EVENTVALIDATION"] = str(payload_element18.get('value'))
                        payload6["__VIEWSTATE"] = str(payload_element19.get('value'))
                        payload6["__VIEWSTATEGENERATOR"] = str(payload_element20.get('value'))



                        response8 = s.post('https://cpdocket.cp.cuyahogacounty.us/CaseInfoByName.aspx', data=payload6,
                                           cookies=cookies3,proxies=proxies)

                        html6 = BeautifulSoup(response8.content, 'html.parser')

                        link = html6.find('form').get('action')
                        # print (link)
                        link = link.split('?')

                        if len(link)>=2:

                            # print ('https://cpdocket.cp.cuyahogacounty.us/CR_CaseInformation_Defendant.aspx?' + str(link[1]))

                            response_final = s.get('https://cpdocket.cp.cuyahogacounty.us/CR_CaseInformation_Defendant.aspx?' + str(link[1]),cookies=cookies3)
                            html_final = BeautifulSoup(response_final.content, 'html.parser')

                            trs_final = html_final.find_all('tr')

                            add1 = ''
                            add2 = ''
                            add3 = ''
                            dob = ''

                            # print (add1)

                            for tr in trs_final:
                                tr_text = tr.text.strip()

                                if 'Address:' in tr_text:
                                    tr_text = tr_text.replace('\n','')
                                    tr_text = tr_text.replace('\r', '')
                                    tr_text = tr_text.replace('Address:', '')
                                    tr_text = tr_text.lstrip()
                                    if add1 == '':
                                        add1 = tr_text

                                if 'Line 2:' in tr_text:
                                    tr_text = tr_text.replace('\n','')
                                    tr_text = tr_text.replace('\r', '')
                                    tr_text = tr_text.replace('Line 2:', '')
                                    tr_text = tr_text.lstrip()
                                    if add2 == '':
                                        add2 = tr_text


                                if 'City, State, Zip:' in tr_text:
                                    tr_text = tr_text.replace('\n','')
                                    tr_text = tr_text.replace('\r', '')
                                    tr_text = tr_text.replace('City, State, Zip:', '')
                                    tr_text = tr_text.lstrip()
                                    if add3 == '':
                                        add3 = tr_text

                                if 'DOB:' in tr_text:
                                    tr_text = tr_text.replace('\n','')
                                    tr_text = tr_text.replace('\r', '')
                                    tr_text = tr_text.replace('DOB:', '')
                                    tr_text = tr_text.lstrip()
                                    if dob == '':
                                        dob = tr_text


                            for tr in trs:
                                try:
                                    a_tag = tr.find('a')
                                    if a_tag:

                                        temp = []
                                        temp.append(name)
                                        temp.append(dob)
                                        temp.append(add1)
                                        temp.append(add2)
                                        temp.append(add3)



                                        temp.append(a_tag.text.strip())

                                        tds = tr.find_all('td')

                                        if len(tds) >= 3:

                                            temp.append(tds[2].text.strip())



                                        arr = []
                                        arr.append(temp)

                                        with open('data1.csv', 'a+') as csvfile:
                                            csvwriter = csv.writer(csvfile)
                                            csvwriter.writerows(arr)




                                except:
                                    print ("A Error")










                except:
                    print ("Error")

                j = j + 1

