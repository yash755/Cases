# html = BeautifulSoup(response.content, 'html.parser')
#
#
# payload_element2 = html.find("input",{'id':'__EVENTVALIDATION'})
# payload_element3 = html.find("input",{'id':'__VIEWSTATE'})
# payload_element4 = html.find("input",{'id':'__VIEWSTATEGENERATOR'})
# payload_element5 = html.find("input",{'id':'SheetContentPlaceHolder_btnYes'})
#
#
# payload["__EVENTARGUMENT"] = ''
# payload["__EVENTTARGET"] = ''
# payload["__EVENTVALIDATION"] = str(payload_element2.get('value'))
# payload["__VIEWSTATE"] = str(payload_element3.get('value'))
# payload["__VIEWSTATEGENERATOR"] = str(payload_element4.get('value'))
# payload["ctl00$SheetContentPlaceHolder$btnYes"] = str(payload_element5.get('value'))
#
#
# url = 'https://cpdocket.cp.cuyahogacounty.us/'
# response1 = s.post(url, data=payload, cookies=cookies)
#
# cookies1 = response1.cookies