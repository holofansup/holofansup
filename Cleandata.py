import pandas as pd
import os
import re



def clean(cmd):
    if '.' in cmd:
        return 1
    elif "Phường " in cmd:
        return 1
    elif re.search("^Xã.*", cmd) :
        return 1
    elif 'THÀNH PHỐ' in cmd:
        return 1
    elif 'HUYỆN' in cmd:
        return 1
    elif 'THỊ XÃ' in cmd:
        return 1
    elif 'QUẬN' in cmd:
        return 1
    elif 'Thành phố' in cmd:
        return 1
    elif 'Huyện' in cmd:
        return 1
    elif 'Thị trấn' in cmd:
        return 1
    elif 'Thị xã' in cmd:
        return 1
    else:
        return 0

def clean_sign(cmd):
    return cmd.split(". ")[-1].split("Phường ")[-1].split("Xã ")[-1].split('Thị trấn ')[-1]
def Clean_Data(url):
    df = pd.read_csv(url)
    # Loai bo nhung dong chua du lieu rong
    df = df.dropna(how= "all").reset_index(drop = True)
    df['check'] = df['Đối tượng gán mã'].apply(lambda x: clean(x))
    df['Đối tượng gán mã'] = df['Đối tượng gán mã'].apply(lambda x: clean_sign(x))
    df = df.loc[df.check  == 1][['Đối tượng gán mã', 'Mã bưu chính']]
    df.to_csv(url, index = False, encoding = 'utf-8-sig')
    


a = os.listdir("C:\\Users\\quyk5\\Desktop\\CNN_Architechture\\selenium\\zipcode\\")
for i in range(0, 63):
    path = "zipcode\\" + str(a[i])
    Clean_Data(path)


    