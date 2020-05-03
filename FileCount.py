#**********************************************
#       Name: 謝佩容
#       Class: 資管系三年級
#       SID: S06490038
#       Program Name: S06490038hw1.py
#       Function: 檔案與檔案目錄的處理
#       Homework: No.1
#       Date: 2020/03/28
#**********************************************

import os,glob,fnmatch
import datetime

#========使用者輸入欲搜尋之路徑

way = input('請輸入指定工作目錄:\t')

all_num = 0   #全部檔案數量

search_num = 0   #符合副檔名的檔案數量

#========判斷輸入之路徑是否存在

if (os.path.exists(way)) == True:

    os.chdir(way)   #改變到path所指定的資料夾下
    
    #print(os.getcwd()) 檢查路徑是否相符
    
    print('\n')
    
    print('使用者指定工作目錄存在，系統現行工作區已轉至該目錄！')
    
    print('\n')

#========使用者輸入欲搜尋之副檔名，並計算路徑中所有的檔案數量
    
    name = input('請輸入指定檔案型式：\t')
    
    for fn in os.listdir(way):  #用for迴圈計算路經中所有檔案數量

        all_num += 1  #加總檔案數量

#========搜尋並計算符合使用者輸入的副檔名
    
    files = (glob.glob('*' + name))     #將欲搜尋之副檔名指定給files

    print('\n')

    print('\t=======================================')

    print('\n')

    print('\t\t符合的檔案名稱:')

    print('\n')
    
    #for file in files:  #用fo迴圈計算符合副檔名的檔案數量
      
    search_num = len(files)   #加總檔案數量

    for i in range(1,search_num+1):

        print('\t\t',i , '.', files[i-1]) #印出搜尋結果


    print('\n')

    print('\t\t本目錄中共有 ' , all_num , ' 個檔案')
    
    print('\t\t其中共有 ', search_num , ' 個是' , name , '的檔案型態')

    print('\t=======================================')

#========印出程式結束時間    

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("程式結束: ",now)

        
    
        


    
    
        
        
    


