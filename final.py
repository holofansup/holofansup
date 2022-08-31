import pandas as pd
import math
import os


### Phase 1: Chinh ve dinh dang yeu cau
### Moi file exel gom 4 cot: Cot 1: ten tinh, Cot 2: ten huyen/thanh pho, Cot 3: ten phuong/xa, Cot 4: ma code

def Change_format(url):
    
    # them cot province va district
    df = pd.read_csv(url)
    df['province'] = url.split('zipcode\\')[-1].split('.csv')[0]
    df['district'] = None

    # lay nhung vi tri tai do gia tri tai cot "ma buu chinh" = NaN
    df_check= df.loc[(df['Mã bưu chính'].isna()) | (df['Mã bưu chính'].str.isnumeric() == False)]
    index = []
    for i in df_check.index:
        index.append(i)

    # Cap nhat thong tin cho cot district
    for i in range(len(index)-1):
        df['district'].iloc[index[i]:index[i+1]] = df.iloc[index[i],0].split('THÀNH PHỐ ')[-1].split('HUYỆN ')[-1].split('THỊ XÃ ')[-1].split('QUẬN ')[-1]
    df['district'].iloc[index[-1]:len(df)] = df.iloc[index[-1],0].split('thành phố ')[-1].split('huyện ')[-1].split('thị xã ')[-1].split('QUẬN ')[-1]

    df.rename(columns={"Mã bưu chính": "ward_code", "Đối tượng gán mã" : "ward"}, inplace= True)
    df = df[['province', 'district', 'ward', 'ward_code']]

    #drop 
    #df = df.loc[( (df.district.isna() == False) & (df.ward_code.isna() == False) ) & ( (df.district.isna() == False) & (df.ward_code.str.isnumeric()))].reset_index(drop = True)

    df.to_csv("folder\\" + url.split('zipcode\\')[-1], index = False, encoding = 'utf-8-sig')

provinces = os.listdir('zipcode\\')
provinces.remove('TP. Hồ Chí Minh.csv')
for province in provinces:
    path = 'zipcode\\' + province
    Change_format(path)


### Phase 2:  Concatenate file
list = os.listdir("folder\\")
pdList = []
for i in list:
    dtf = pd.read_csv('folder\\' + i)
    pdList.append(dtf)
new_df = pd.concat(pdList)
new_df.to_csv(r'C:\Users\quyk5\Desktop\CNN_Architechture\selenium\Data_Code.csv', index= False, encoding= 'utf-8-sig')
