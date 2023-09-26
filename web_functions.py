import webbrowser

# Open a windows <ith multiple tables
# The path of the browser for windows should be exactly in the following format
# "\"path/of/the/browser/app\""
# Example ! "\"X:/Folder/Folder1/Folder2/brave.exe\""
# You need to open a first windows in non incognito
def browser_with_multi_tabs(browser_path, urls_list=["https://www.google.com"]):
    for url in urls_list:
        webbrowser.get(f"{browser_path} %s --incognito").open(url)