from bs4 import BeautifulSoup
import webbrowser
import requests
import tkinter
import os

img_name = [222000004,222000004,222000005,222000006,222000007,222000008,222000009,
222000010,231000001,231000002,231000003,231000004,231000014,523000164,
523000165,523000183,523000190,523000207,523000238,523000241,523000243,523800001]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
}

#def updata_video():
#    print("lll")

def updata_img():
    num = 0
    url_list = []
    for page in range(1, 6):
        html1 = "https://wallhaven.cc/hot?page=" + str(page)
        html2 = "https://wallhaven.cc/hot?page=" + str(page)
        html_list = [html1, html2]
        for html in html_list:
            requests_html = requests.get(html, headers=headers)
            bs_html = BeautifulSoup(requests_html.text, "lxml")
            for link in bs_html.find_all('a', class_="preview"):
                image_link = link['href']
                url_list.append(image_link)
                num += 1
                print("已获取第" + str(num) + "个链接")

    a = os.path.exists("逍遥游\Texture\Fortuitous")
    if a:
        print("文件夹已存在，PASS")
    else:
        os.mkdir("逍遥游\Texture\Fortuitous")
        print("文件夹建立成功")
    # 建立文件夹存放图片
    num = 0
    for link in url_list:
        requests_html = requests.get(link, headers=headers)
        bs_html = BeautifulSoup(requests_html.text, "lxml")
        a_img = bs_html.find('img', id='wallpaper')
        r = requests.get(a_img['src'])
        num += 1
        if num == 23:
            break
        else:
            with open("逍遥游\Texture\Fortuitous" + str(img_name[num]) + ".jpg", 'wb') as f:
                f.write(r.content)
                print("第" + str(num) + "张写入成功")


def jr_web():
    print("访问官网")
    webbrowser.open("supermod.top")

top = tkinter.Tk()
top.geometry('500x300')
top.title("逍遥游 图片 更新器  BY-Flower")
down_img = tkinter.Button(top, text = "点我更新图片", command = updata_img)
# down_video = tkinter.Button(top, text = "点我更新视频", command = updata_video)
into_web = tkinter.Button(top, text= "点我访问官网", command = jr_web)

down_img.pack()
# down_video.pack()
into_web.pack()
top.mainloop()
