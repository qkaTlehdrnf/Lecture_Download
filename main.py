#f12 network https://cdn.yonsei.ac.kr/yonsei/_definst_/mp4:yscecictl_yscec/79308/1600154156/lecture%203.mp4/media_2.ts
import time
import webbrowser
def browser_change(name,url):
    if name=='chrome':
        webbrowser.register('{}'.format(name),
                            None,
                            webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif name=='edge':
        pass
    else:
        webbrowser.register('{}'.format(name),
                            None,
                            webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)

def url_changer(url,digit):
    i=0
    url_split1=url.split('/')
    url_split2=url_split1[-1].split('-')
    url_split2[1]=digit

    urlreform2='-'.join([ele for ele in url_split2])
    url_split1[-1]=urlreform2
    urlreform1='/'.join([ele for ele in url_split1])
    return urlreform1

def question(times=None):
    if times!=None:
        hour,minute,seconds=times
        time_in_secs=int(hour)*3600+int(minute)*60+int(seconds)
        file_number=time_in_secs//10
        return file_number

    url=input('url?')
    hour=input('hour?')
    minute=input('minute?')
    seconds=input('secs?')
    time_in_secs=int(hour)*3600+int(minute)*60+int(seconds)
    file_number=time_in_secs//10
    return file_number,url
#https://mszgmhihzdlo5752380.cdn.ntruss.com/hls/f5b93ad2-056a-45d5-9910-923b418986e8/mp4/f5b93ad2-056a-45d5-9910-923b418986e8.mp4/segment-2-v1-a1.ts
def main(url=None,times=None):
    if url!=None and times != None:
        many=question(times)
    else:
        url,many=question()
    for i in range(1,many+3):
        digit=str(i)
        while len(digit)!=4:
            digit='0'+digit


        url_f=url_changer(url,digit)
        print(url_f)
        time.sleep(0.5)
        browser_change('chrome',url_f)


if __name__=='__main__':
    url='https://mszgmhihzdlo5752380.cdn.ntruss.com/hls/f5b93ad2-056a-45d5-9910-923b418986e8/mp4/f5b93ad2-056a-45d5-9910-923b418986e8.mp4/segment-2-v1-a1.ts'
    times=0,28,0
    main(url,times)