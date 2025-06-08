











import os



os.system("pip install beautifulsoup4 requests")





import requests
from bs4 import BeautifulSoup

# عنوان الصفحة التي تريد تحليلها
url = "https://universaldependencies.org/"

# اجلب محتوى الصفحة

response = requests.get(url)

html = response.text


#with open("page.html", "r", encoding="utf-8") as f:
    #html = f.read()




# استخدم BeautifulSoup لتحليل HTML
soup = BeautifulSoup(html, 'html.parser')

# استخرج جميع الروابط <a href="...">
all_links = [a['href'] for a in soup.find_all('a', href=True)]

# روابط تحتوي على github.com (سواء http أو https)


github_links = []


counter_0 = 0


while (counter_0 < len(all_links)):





    if (all_links[counter_0].startswith("https://github.com/")):
    
        
        v_0 = all_links[counter_0].split("https://github.com/")
    
        v_1 = v_0[-1].split("/")
        
        link = "https://github.com/" + v_1[0] + "/" + v_1[1] + ".git"
    
        if (not link in github_links):
    
        
            github_links.append(link)
        
    
    elif (all_links[counter_0].startswith("http://github.com/")):
    
        v_0 = all_links[counter_0].split("http://github.com/")
    
        v_1 = v_0[-1].split("/")
        
        link = "http://github.com/" + v_1[0] + "/" + v_1[1] + ".git"
    
        if (not link in github_links):
    
            github_links.append(link)
        

    

    counter_0 += 1




#github_links = [link for link in all_links if link.startswith("https://github.com/") or link.startswith("http://github.com/")]

# احذف التكرارات إن وجدت
github_links = list(set(github_links))

# احفظها في ملف نصي


with open(os.path.join(os.getcwd(), "github_links.txt"), "w", encoding="utf-8") as f:
    for link in github_links:
        f.write(link + "\n")

print(f"تم استخراج {len(github_links)} رابطًا من GitHub وحفظها في github_links.txt")







#import requests

#def get_git_repo_size(repo_url):
    #try:
        ## تأكد أن الرابط ينتهي بـ .git
        #if not repo_url.endswith(".git"):
            #print(f"تخطي: {repo_url} ليس رابط git صالح")
            #return None

        ## أرسل طلب HEAD بدل GET
        #response = requests.head(repo_url, allow_redirects=True, timeout=10)

        ## إذا كان الرد ناجحًا
        #if response.status_code == 200:
            #size_bytes = response.headers.get('Content-Length')
            #if size_bytes:
                #size_mb = int(size_bytes) / (1024 * 1024)
                #return round(size_mb, 2)
            #else:
                #print(f"الرابط لا يحتوي على Content-Length: {repo_url}")
        #else:
            #print(f"فشل في الوصول إلى {repo_url}, كود الحالة: {response.status_code}")
    #except Exception as e:
        #print(f"خطأ في {repo_url}: {e}")

    #return None







#import requests
#from bs4 import BeautifulSoup
#import re

## 1. الرابط المستهدف

##url = "https://example.com"



#url = "https://universaldependencies.org/"

## 2. تحميل الصفحة
#response = requests.get(url)
#html = response.text

## 3. تحليل الصفحة
#soup = BeautifulSoup(html, 'html.parser')

## 4. استخراج كل الروابط
#all_links = [a['href'] for a in soup.find_all('a', href=True)]

## 5. تجميع روابط github بالشكل الصحيح فقط: github.com/username/reponame
#github_repo_links = set()  # نستخدم set لمنع التكرار
#pattern = re.compile(r'(https?://)?(www\.)?github\.com/([^/]+)/([^/#?]+)')

#number_0 = 0.0


#list_0 = []

#for link in all_links:
    #match = pattern.match(link)
    #if match:
        #user = match.group(3)
        #repo = match.group(4)
        ## نبني رابط .git المباشر
        #git_url = f"https://github.com/{user}/{repo}.git"


        #if (git_url not in list_0):

            #github_repo_links.add(git_url)

            #size_of_git_url = get_git_repo_size(git_url)

            #if (size_of_git_url is not None):

                #number_0 += size_of_git_url

            #else:

                #print("error")


            #list_0.append(git_url)

## 6. حفظها في ملف




#with open(os.path.join(os.getcwd(), "github_repos.txt"), "w", encoding="utf-8") as f:
    #for repo_link in sorted(github_repo_links):
        #f.write(repo_link + "\n")

    #f.write(str(number_0))

#print(f"تم استخراج {len(github_repo_links)} مستودع GitHub بنجاح.")





















