# Extract the company name from the url
def extract_name(url):
    name = ""
    if url[0:4] == "http":
        arr = url.split('.')
        if len(arr) > 2:
            # http://www.flexusbio.com/
            name = arr[1]
        else:
            # http://flexusbio.com/
            copy = arr[0]
            l = len(copy)
            left = l-1
            while copy[left]!='/':
                left -= 1
            left+=1
            name =  copy[left:l]
    else:
        l = len(url)
        left = l-1
        if url[l-1] == '/':
            l-=1
        while url[left]!='/':
            left -= 1
        left+=1
        name =  url[left:l]
    return name
    
"""
if __name__ == "__main__":
    print extract_name("/companies/twitter")
    print extract_name("http://www.dji.com")"""
