# Extract the company name from the url
# url format:
# http://www.flexusbio.com/ or http://flexusbio.com/
def extract_name_from_url(url):
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

def extract_name_from_string(s):
    i = 0
    while i <len(s):
        if s[i] == '\n' or s[i] == ' ' or s[i] == '\t':
            break
        else:
            i += 1
    return s[:i]

#if __name__ == "__main__":
#    print extract_name_from_string("Percolate\nMarketing platform that helps brands create and manage content and social media at scale.")
