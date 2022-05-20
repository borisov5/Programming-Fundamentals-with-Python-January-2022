import webbrowser as wb


def web_automation():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    urls = ('stackoverflow.com', 'github.com', 'google.com', 'gmail.com')

    for url in urls:
        print('Opening: ' + url)
        wb.get(chrome_path).open(url)


web_automation()
