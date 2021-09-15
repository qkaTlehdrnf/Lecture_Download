import webbrowser
def browser_change(name,url):
    if name=='chrome':
        webbrowser.register('{}'.format(name),
                            None,
                            webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)
    elif name=='edge':
        pass
    else:
        webbrowser.register('{}'.format(name),
                            None,
                            webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)
