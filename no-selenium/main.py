import requests

cookies = {
    '__utmz': '213851395.1671941693.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'G_ENABLED_IDPS': 'google',
    'ASP.NET_SessionId': 's3qd4fjwxb4asjzq4eb1rjyi',
    '__utma': '213851395.448485636.1671941693.1671941693.1672038376.2',
    '__utmc': '213851395',
    '__utmt': '1',
    '__utmb': '213851395.1.10.1672038376',
}

headers = {
    'Host': 'fap.fpt.edu.vn',
    # 'Content-Length': '20238',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://fap.fpt.edu.vn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://fap.fpt.edu.vn/Phuhuynh/StudentTranscriptdn.aspx',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Cookie': '__utmz=213851395.1671941693.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); G_ENABLED_IDPS=google; ASP.NET_SessionId=s3qd4fjwxb4asjzq4eb1rjyi; __utma=213851395.448485636.1671941693.1671941693.1672038376.2; __utmc=213851395; __utmt=1; __utmb=213851395.1.10.1672038376',
}

data = {
    '__VIEWSTATE': '/wEPDwUKMjExODgwMDg5NA9kFgJmD2QWAgIDD2QWBgIBD2QWAgIBDw8WAh4EVGV4dAURdHJ1b25nbnBjZTE1MDg0MitkZAIDDw8WAh8ABUQ8YSBocmVmPScuLi9Eb25vci5hc3B4Jz5Ib21lPC9hPiZuYnNwO3wmbmJzcDs8Yj5HcmFkZSBUcmFuc2NyaXB0PC9iPmRkAgUPZBYCAgEPZBYGAgEPDxYCHwAFZDxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1kZWZhdWx0Jz5DRTE1MDg0Mjwvc3Bhbj4gLSA8c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtaW5mbyc+QklUX0lBXzE1Qzwvc3Bhbj5kZAIDDxYCHglpbm5lcmh0bWwFqGI8VGFibGUgY2xhc3M9J3RhYmxlIHRhYmxlLWhvdmVyJz48dGhlYWQgY2xhc3M9J3RoZWFkLWludmVyc2UnPjx0cj48dGggIHN0eWxlPSd3aWR0aDoxMHB4Jz5ObzwvdGg+PHRoICBzdHlsZT0nd2lkdGg6MTVweCc+VGVybTwvdGg+PHRoIHN0eWxlPSd3aWR0aDo4MHB4Jz5TZW1lc3RlcjwvdGg+PHRoIHN0eWxlPSd3aWR0aDo2MHB4Jz5TdWJqZWN0IENvZGU8L3RoPjx0aCBzdHlsZT0nd2lkdGg6NjBweCc+cHJlcmVxdWlzaXRlPC90aD48dGggc3R5bGU9J3dpZHRoOjgwcHgnPlJlcGxhY2VkIFN1YmplY3Q8L3RoPjx0aD5TdWJqZWN0IE5hbWU8L3RoPjx0aCAgc3R5bGU9J3dpZHRoOjEwcHgnPkNyZWRpdDwvdGg+PHRoIHN0eWxlPSd3aWR0aDoyMHB4Jz5HcmFkZTwvdGg+PHRoIHN0eWxlPSd3aWR0aDo4MHB4Jz5TdGF0dXM8L3RoPjwvdHI+PC90aGVhZD4gIDx0Ym9keT48dHI+PHRkPjE8L3RkPjx0ZD4wPC90ZD48dGQ+RmFsbDIwMTk8L3RkPjx0ZD5WT1YxMTQ8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PC90ZD48dGQ+Vm92aW5hbSAxPC90ZD48dGQ+MjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz42PC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+MjwvdGQ+PHRkPjA8L3RkPjx0ZD5TdW1tZXIyMDIwPC90ZD48dGQ+Vk9WMTI0PC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPlZPVjExNDwvdGQ+PHRkPjwvdGQ+PHRkPlZvdmluYW0gMjwvdGQ+PHRkPjI8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+Ni4zPC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+MzwvdGQ+PHRkPjA8L3RkPjx0ZD5GYWxsMjAyMDwvdGQ+PHRkPlZPVjEzNDwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5WT1YxMjQ8L3RkPjx0ZD48L3RkPjx0ZD5Wb3ZpbmFtIDM8L3RkPjx0ZD4yPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjcuNTwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjQ8L3RkPjx0ZD4wPC90ZD48dGQ+RmFsbDIwMTk8L3RkPjx0ZD5HRFFQPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjwvdGQ+PHRkPk1pbGl0YXJ5IHRyYWluaW5nPC90ZD48dGQ+MDwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz42Ljc8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD41PC90ZD48dGQ+MDwvdGQ+PHRkPlNwcmluZzIwMjI8L3RkPjx0ZD5UTUkxMDE8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+w5BUUjEwMjwvdGQ+PHRkPlRyYWRpdGlvbmFsIG11c2ljYWwgaW5zdHJ1bWVudDwvdGQ+PHRkPjM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+OS42PC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+NjwvdGQ+PHRkPjE8L3RkPjx0ZD5GYWxsMjAyMDwvdGQ+PHRkPkNTSTEwMWI8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PC90ZD48dGQ+SW50cm9kdWN0aW9uIHRvIENvbXB1dGVyIFNjaWVuY2U8L3RkPjx0ZD4zPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjguMTwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjc8L3RkPjx0ZD4xPC90ZD48dGQ+RmFsbDIwMjA8L3RkPjx0ZD5DRUEyMDFiPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjwvdGQ+PHRkPkNvbXB1dGVyIE9yZ2FuaXphdGlvbiBhbmQgQXJjaGl0ZWN0dXJlPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz44LjI8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD44PC90ZD48dGQ+MTwvdGQ+PHRkPkZhbGwyMDIwPC90ZD48dGQ+TUFFMTAxPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjwvdGQ+PHRkPk1hdGhlbWF0aWNzIGZvciBFbmdpbmVlcmluZzwvdGQ+PHRkPjM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+NS44PC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+OTwvdGQ+PHRkPjE8L3RkPjx0ZD5GYWxsMjAyMDwvdGQ+PHRkPlBSRjE5MjwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz48L3RkPjx0ZD48L3RkPjx0ZD5Qcm9ncmFtbWluZyBGdW5kYW1lbnRhbHM8L3RkPjx0ZD4zPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjcuMzwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjEwPC90ZD48dGQ+MTwvdGQ+PHRkPlN1bW1lcjIwMjA8L3RkPjx0ZD5TU0wxMDFjPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPlNTTDEwMTwvdGQ+PHRkPkFjYWRlbWljIHNraWxscyBmb3IgVW5pdmVyc2l0eSBzdWNjZXNzPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz42Ljc8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4xMTwvdGQ+PHRkPjI8L3RkPjx0ZD5TcHJpbmcyMDIxPC90ZD48dGQ+TldDMjAzYzwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz48L3RkPjx0ZD48L3RkPjx0ZD5Db21wdXRlciBOZXR3b3JraW5nPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz41Ljc8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4xMjwvdGQ+PHRkPjI8L3RkPjx0ZD5TcHJpbmcyMDIxPC90ZD48dGQ+U1NHMTAzPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjwvdGQ+PHRkPkNvbW11bmljYXRpb24gYW5kIEluLUdyb3VwIFdvcmtpbmcgU2tpbGxzPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz43LjE8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4xMzwvdGQ+PHRkPjI8L3RkPjx0ZD5TcHJpbmcyMDIxPC90ZD48dGQ+TUFEMTAxPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjwvdGQ+PHRkPkRpc2NyZXRlIG1hdGhlbWF0aWNzPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz42LjY8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4xNDwvdGQ+PHRkPjI8L3RkPjx0ZD5TcHJpbmcyMDIxPC90ZD48dGQ+UFJPMTkyPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPlBSRjE5MjwvdGQ+PHRkPjwvdGQ+PHRkPk9iamVjdC1PcmllbnRlZCBQcm9ncmFtbWluZzwvdGQ+PHRkPjM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+Ny45PC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+MTU8L3RkPjx0ZD4yPC90ZD48dGQ+U3ByaW5nMjAyMTwvdGQ+PHRkPk9TRzIwMjwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz48L3RkPjx0ZD48L3RkPjx0ZD5PcGVyYXRpbmcgU3lzdGVtPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz42PC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+MTY8L3RkPjx0ZD4zPC90ZD48dGQ+U3VtbWVyMjAyMTwvdGQ+PHRkPkNTRDIwMTwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5QUk8xOTI8L3RkPjx0ZD48L3RkPjx0ZD5EYXRhIFN0cnVjdHVyZXMgYW5kIEFsZ29yaXRobTwvdGQ+PHRkPjM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+Nzwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjE3PC90ZD48dGQ+MzwvdGQ+PHRkPlN1bW1lcjIwMjE8L3RkPjx0ZD5MQUIyMTE8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+UFJPMTkyPC90ZD48dGQ+PC90ZD48dGQ+T09QIHdpdGggSmF2YSBMYWI8L3RkPjx0ZD4zPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjE4PC90ZD48dGQ+MzwvdGQ+PHRkPlN1bW1lcjIwMjE8L3RkPjx0ZD5EQkkyMDI8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PC90ZD48dGQ+RGF0YWJhc2UgU3lzdGVtczwvdGQ+PHRkPjM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+Njwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjE5PC90ZD48dGQ+MzwvdGQ+PHRkPlN1bW1lcjIwMjE8L3RkPjx0ZD5KUEQxMTM8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PC90ZD48dGQ+RWxlbWVudGFyeSBKYXBhbmVzZSAxLSBBMS4xPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz42Ljc8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4yMDwvdGQ+PHRkPjM8L3RkPjx0ZD5TdW1tZXIyMDIxPC90ZD48dGQ+SUFPMjAxYzwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz48L3RkPjx0ZD48L3RkPjx0ZD5JbnRyb2R1Y3Rpb24gdG8gSW5mb3JtYXRpb24gQXNzdXJhbmNlPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz44PC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+MjE8L3RkPjx0ZD40PC90ZD48dGQ+RmFsbDIwMjE8L3RkPjx0ZD5JT1QxMDI8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PC90ZD48dGQ+SW50ZXJuZXQgb2YgVGhpbmdzPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz43Ljc8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4yMjwvdGQ+PHRkPjQ8L3RkPjx0ZD5GYWxsMjAyMTwvdGQ+PHRkPklURTMwMmM8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PC90ZD48dGQ+RXRoaWNzIGluIElUPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz45LjU8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4yMzwvdGQ+PHRkPjQ8L3RkPjx0ZD5GYWxsMjAyMTwvdGQ+PHRkPkpQRDEyMzwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5KUEQxMTM8L3RkPjx0ZD48L3RkPjx0ZD5FbGVtZW50YXJ5IEphcGFuZXNlIDEtQTEuMjwvdGQ+PHRkPjM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+NS4yPC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+MjQ8L3RkPjx0ZD40PC90ZD48dGQ+RmFsbDIwMjE8L3RkPjx0ZD5NQVMyOTE8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+TUFFMTAxPC90ZD48dGQ+PC90ZD48dGQ+U3RhdGlzdGljcyAmIFByb2JhYmlsaXR5PC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz41Ljc8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4yNTwvdGQ+PHRkPjQ8L3RkPjx0ZD5GYWxsMjAyMTwvdGQ+PHRkPk9TUDIwMTwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5OV0MyMDNjPC90ZD48dGQ+PC90ZD48dGQ+T3BlbiBTb3VyY2UgUGxhdGZvcm0gYW5kIE5ldHdvcmsgQWRtaW5pc3RyYXRpb248L3RkPjx0ZD4zPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjcuNTwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjI2PC90ZD48dGQ+NTwvdGQ+PHRkPlNwcmluZzIwMjI8L3RkPjx0ZD5JQUEyMDI8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+SUFPMjAxYzwvdGQ+PHRkPjwvdGQ+PHRkPlJpc2sgTWFuYWdlbWVudCBpbiBJbmZvcm1hdGlvbiBTeXN0ZW1zPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1kYW5nZXInPjUuNzwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtZGFuZ2VyJz5Ob3QgcGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjI3PC90ZD48dGQ+NTwvdGQ+PHRkPlNwcmluZzIwMjI8L3RkPjx0ZD5JQU0zMDI8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+UFJPMTkyLElURTMwMmM8L3RkPjx0ZD48L3RkPjx0ZD5NYWx3YXJlIEFuYWx5c2lzIGFuZCBSZXZlcnNlIEVuZ2luZWVyaW5nPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1kYW5nZXInPjMuNzwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtZGFuZ2VyJz5Ob3QgcGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjI4PC90ZD48dGQ+NTwvdGQ+PHRkPlNwcmluZzIwMjI8L3RkPjx0ZD5QUlAyMDFjPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjwvdGQ+PHRkPlB5dGhvbiBQcm9ncmFtbWluZzwvdGQ+PHRkPjM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+OS44PC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+Mjk8L3RkPjx0ZD41PC90ZD48dGQ+U3ByaW5nMjAyMjwvdGQ+PHRkPkZSUzMwMTwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5OV0MyMDNjPC90ZD48dGQ+PC90ZD48dGQ+RGlnaXRhbCBGb3JlbnNpY3M8L3RkPjx0ZD4zPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjguMTwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjMwPC90ZD48dGQ+NTwvdGQ+PHRkPlNwcmluZzIwMjI8L3RkPjx0ZD5DUlkzMDNjPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPk1BRDEwMTwvdGQ+PHRkPjwvdGQ+PHRkPkFwcGxpZWQgQ3J5cHRvZ3JhcGh5PC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz41LjU8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4zMTwvdGQ+PHRkPjY8L3RkPjx0ZD5TdW1tZXIyMDIyPC90ZD48dGQ+U1lCMzAyYzwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz48L3RkPjx0ZD48L3RkPjx0ZD5FbnRyZXByZW5ldXJzaGlwPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz44Ljk8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4zMjwvdGQ+PHRkPjY8L3RkPjx0ZD5TdW1tZXIyMDIyPC90ZD48dGQ+T0pUMjAyPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjwvdGQ+PHRkPk9uLVRoZS1Kb2IgVHJhaW5pbmc8L3RkPjx0ZD4xMDwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz43LjI8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4zMzwvdGQ+PHRkPjc8L3RkPjx0ZD5GYWxsMjAyMjwvdGQ+PHRkPklBUDMwMTwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5JQUEyMDI8L3RkPjx0ZD48L3RkPjx0ZD5Qb2xpY3kgRGV2ZWxvcG1lbnQgaW4gSW5mb3JtYXRpb24gQXNzdXJhbmNlPC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz43LjE8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4zNDwvdGQ+PHRkPjc8L3RkPjx0ZD5GYWxsMjAyMjwvdGQ+PHRkPkhPRDQwMTwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5PU1AyMDEsSVRFMzAyYzwvdGQ+PHRkPjwvdGQ+PHRkPkV0aGljYWwgSGFja2luZyBhbmQgT2ZmZW5zaXZlIFNlY3VyaXR5PC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz43LjE8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4zNTwvdGQ+PHRkPjc8L3RkPjx0ZD5GYWxsMjAyMjwvdGQ+PHRkPklBVzMwMTwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5JVEUzMDJjPC90ZD48dGQ+PC90ZD48dGQ+V2ViIFNlY3VyaXR5PC90ZD48dGQ+MzwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1wcmltYXJ5Jz44LjE8L3NwYW4+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXN1Y2Nlc3MnPlBhc3NlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4zNjwvdGQ+PHRkPjc8L3RkPjx0ZD5GYWxsMjAyMjwvdGQ+PHRkPkVOVzQ5MmM8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PC90ZD48dGQ+QWNhZGVtaWMgV3JpdGluZyBTa2lsbHM8L3RkPjx0ZD4zPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjcuNjwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjM3PC90ZD48dGQ+NzwvdGQ+PHRkPkZhbGwyMDIyPC90ZD48dGQ+RlJTNDAxYzwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz48L3RkPjx0ZD48L3RkPjx0ZD5OZXR3b3JrIEZvcmVuc2ljczwvdGQ+PHRkPjM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+Ny4yPC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+Mzg8L3RkPjx0ZD44PC90ZD48dGQ+U3ByaW5nMjAyMzwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5JQVI0MDFjPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPkZSUzQwMWM8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtd2FybmluZyc+PC9zcGFuPjwvdGQ+PHRkPkluY2lkZW50IFJlc3BvbnNlPC90ZD48dGQ+PC90ZD48dGQ+IDwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1pbmZvJz5TdHVkeWluZzwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD4zOTwvdGQ+PHRkPjg8L3RkPjx0ZD5TcHJpbmcyMDIzPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPlBNRzIwMmM8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXdhcm5pbmcnPjwvc3Bhbj48L3RkPjx0ZD5Qcm9qZWN0IG1hbmFnZW1lbnQ8L3RkPjx0ZD48L3RkPjx0ZD4gPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLWluZm8nPlN0dWR5aW5nPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjQwPC90ZD48dGQ+ODwvdGQ+PHRkPlNwcmluZzIwMjM8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+REJTNDAxPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPkRCSTIwMixPU1AyMDE8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtd2FybmluZyc+PC9zcGFuPjwvdGQ+PHRkPkRhdGFiYXNlIFNlY3VyaXR5PC90ZD48dGQ+PC90ZD48dGQ+IDwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1pbmZvJz5TdHVkeWluZzwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD40MTwvdGQ+PHRkPjg8L3RkPjx0ZD5TcHJpbmcyMDIzPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPk5XQzMwMjwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5PU1AyMDE8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtd2FybmluZyc+PC9zcGFuPjwvdGQ+PHRkPk5ldHdvcmsgQ29ubmVjdGl2aXR5PC90ZD48dGQ+PC90ZD48dGQ+IDwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1pbmZvJz5TdHVkeWluZzwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD40MjwvdGQ+PHRkPjg8L3RkPjx0ZD5TcHJpbmcyMDIzPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPk1MTjEyMjwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtd2FybmluZyc+PC9zcGFuPjwvdGQ+PHRkPlBvbGl0aWNhbCBlY29ub21pY3Mgb2YgTWFyeGlzbSDigJMgTGVuaW5pc208L3RkPjx0ZD48L3RkPjx0ZD4gPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLWluZm8nPlN0dWR5aW5nPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjQzPC90ZD48dGQ+ODwvdGQ+PHRkPlNwcmluZzIwMjM8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+TUxOMTExPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC13YXJuaW5nJz48L3NwYW4+PC90ZD48dGQ+UGhpbG9zb3BoeSBvZiBNYXJ4aXNtIOKAkyBMZW5pbmlzbTwvdGQ+PHRkPjwvdGQ+PHRkPiA8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtaW5mbyc+U3R1ZHlpbmc8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+NDQ8L3RkPjx0ZD45PC90ZD48dGQ+PC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPlZOUjIwMjwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtd2FybmluZyc+PC9zcGFuPjwvdGQ+PHRkPkhpc3Rvcnkgb2YgQ1BWPC90ZD48dGQ+PC90ZD48dGQ+IDwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1kZWZhdWx0Jz5Ob3Qgc3RhcnRlZDwvc3Bhbj48L3RkPjwvdHI+PHRyPjx0ZD40NTwvdGQ+PHRkPjk8L3RkPjx0ZD48L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+TUxOMTMxPC90ZD48dGQgc3R5bGU9J3dpZHRoOjYwcHgnPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC13YXJuaW5nJz48L3NwYW4+PC90ZD48dGQ+U2NpZW50aWZpYyBzb2NpYWxpc208L3RkPjx0ZD48L3RkPjx0ZD4gPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLWRlZmF1bHQnPk5vdCBzdGFydGVkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjQ2PC90ZD48dGQ+OTwvdGQ+PHRkPjwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5IQ00yMDI8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXdhcm5pbmcnPjwvc3Bhbj48L3RkPjx0ZD5IQ00gSWRlb2xvZ3k8L3RkPjx0ZD48L3RkPjx0ZD4gPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLWRlZmF1bHQnPk5vdCBzdGFydGVkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjQ3PC90ZD48dGQ+OTwvdGQ+PHRkPjwvdGQ+PHRkIHN0eWxlPSd3aWR0aDo2MHB4Jz5JQVA0OTE8L3RkPjx0ZCBzdHlsZT0nd2lkdGg6NjBweCc+PC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXdhcm5pbmcnPjwvc3Bhbj48L3RkPjx0ZD5JQSBDYXBzdG9uZSBQcm9qZWN0PC90ZD48dGQ+PC90ZD48dGQ+IDwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1kZWZhdWx0Jz5Ob3Qgc3RhcnRlZDwvc3Bhbj48L3RkPjwvdHI+ICA8L3Rib2R5PjxUYWJsZT4NCmQCBQ8WAh8BBa4KPFRhYmxlIGNsYXNzPSd0YWJsZSB0YWJsZS1ob3Zlcic+PHRoZWFkIGNsYXNzPSd0aGVhZC1pbnZlcnNlJz48dHI+PHRoICBzdHlsZT0nd2lkdGg6MTBweCc+Tm88L3RoPjx0aCAgc3R5bGU9J3dpZHRoOjQwcHgnPlNlbWVzdGVyPC90aD48dGggc3R5bGU9J3dpZHRoOjQwcHgnPlN1YmplY3RDb2RlPC90aD48dGg+U3ViamVjdE5hbWU8L3RoPjx0aD5DcmVkaXQ8L3RoPjx0aCBzdHlsZT0nd2lkdGg6MjBweCc+R3JhZGU8L3RoPjx0aCBzdHlsZT0nd2lkdGg6NTVweCc+U3RhdHVzPC90aD48L3RyPjwvdGhlYWQ+ICA8dGJvZHk+PHRyPjx0ZD4xPC90ZD48dGQ+RmFsbDIwMTk8L3RkPjx0ZD5FTlQxMDQ8L3RkPjx0ZD5FbmdsaXNoIDIgKFRvcCBOb3RjaCAxKTwvdGQ+PHRkPjA8L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtcHJpbWFyeSc+OC4xPC9zcGFuPjwvdGQ+PHRkPjxzcGFuIGNsYXNzPSdsYWJlbCBsYWJlbC1zdWNjZXNzJz5QYXNzZWQ8L3NwYW4+PC90ZD48L3RyPjx0cj48dGQ+MjwvdGQ+PHRkPkZhbGwyMDE5PC90ZD48dGQ+RU5UMjAzPC90ZD48dGQ+RW5nbGlzaCAzIChUb3AgTm90Y2ggMik8L3RkPjx0ZD4wPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjguMzwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjM8L3RkPjx0ZD5TcHJpbmcyMDIwPC90ZD48dGQ+RU5UMzAzPC90ZD48dGQ+RW5nbGlzaCA0IChUb3AgTm90Y2ggMyk8L3RkPjx0ZD4wPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjguNDwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjQ8L3RkPjx0ZD5TcHJpbmcyMDIwPC90ZD48dGQ+RU5UNDAzPC90ZD48dGQ+RW5nbGlzaCA1IChTdW1taXQgMSk8L3RkPjx0ZD4wPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjcuMjwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj48dHI+PHRkPjU8L3RkPjx0ZD5TdW1tZXIyMDIwPC90ZD48dGQ+RU5UNTAzPC90ZD48dGQ+RW5nbGlzaCA2IChTdW1taXQgMik8L3RkPjx0ZD4wPC90ZD48dGQ+PHNwYW4gY2xhc3M9J2xhYmVsIGxhYmVsLXByaW1hcnknPjcuNTwvc3Bhbj48L3RkPjx0ZD48c3BhbiBjbGFzcz0nbGFiZWwgbGFiZWwtc3VjY2Vzcyc+UGFzc2VkPC9zcGFuPjwvdGQ+PC90cj4gIDwvdGJvZHk+PFRhYmxlPg0KZGS0A4JPwkiPziUIMXcIT0JPGedXEBSRVu/0xsOfWORzdQ==',
    '__VIEWSTATEGENERATOR': 'C15613DB',
    '__EVENTVALIDATION': '/wEdAAS5b7x2OtllzRSQyqpgvHHnnWdsB9rlNEBkhSHxx91PtvjtxHNmdZFmtOVx202NsUGibNO/9NdS0yOHcZg6YLufjWbH8bdeXen/vuUyGkZZQUnGFSkFx72BASc8aS+XLDA=',
    'ctl00$mainContent$hfGridHtml': '',
    'ctl00$mainContent$btnExport': 'Export To Excel',
    'ctl00$mainContent$hdError': '',
}

response = requests.post(
    'https://fap.fpt.edu.vn/Phuhuynh/StudentTranscriptdn.aspx',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)

with open('asd.htm', 'wb') as f:
    f.write(response.content)
