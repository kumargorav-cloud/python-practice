import webbrowser as wb
def work_auto():
    path  = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    urls = [
        'youtube.com',
        'github.com'
    ]
    for url in urls:
        wb.get(path).open(url)

work_auto()