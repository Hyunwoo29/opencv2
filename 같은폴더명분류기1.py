import os
import pathlib
import shutil

#여러 폴더가 있는 경로
folderpath = "D:\Recogn1"

#폴더명 받아오기
folderlist = os.listdir(folderpath)
category = []
filename='1'
uniq=1
file_ext='.bmp'

file_list = 'D:/ab/1'

i=0 #파일명 변경하기 위한 넘버링 변수

#폴더리스트를 for문을 통해 반복
for fname1 in folderlist:
    #해당 test 폴더(1,2,3,4) 위치 설정
    current_folder = folderpath + "/" + fname1
    #각 test폴더(1,2,3,4) 안의 파일명 받아오기
    filelist = os.listdir(current_folder)

    # print("현재 폴더명 : ", fname1)
    #각 폴더명의 파일리스트를 다시 for문을 통해 반복
    for fname2 in filelist:
        val = '_0' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"0"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/0')
        else:
            print("no")
        
        val = '_1' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"1"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/1')
        else:
            print("no")
            
        val = '_2' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"2"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/2')
        else:
            print("no")
        
        val = '_3' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"3"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/3')
        else:
            print("no")
            
        val = '_4' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"4"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/4')
        else:
            print("no")
            
        val = '_5' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"5"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/5')
        else:
            print("no")
            
        val = '_6' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"6"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/6')
        else:
            print("no")
        
        val = '_7' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"7"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/7')
        else:
            print("no")
            
        val = '_8' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"8"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/8')
        else:
            print("no")
            
        val = '_9' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"9"+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/9')
        else:
            print("no")
        
        val = '_.' in fname2
        if val:
            if val == True:
                os.rename(current_folder+"/"+fname2, current_folder+"/"+"."+"_"+str(i)+".bmp")
                i = i+1
                shutil.move(current_folder+"/"+fname2, 'D:/number1/point')
        else:
            
            print("no")
            
        
            
            
# print(fname2)
        #os.rename(a, b) : a를 b로 이름 변경. b는 저장될 위치도 지정하는 것이므로 같은 폴더에하려면 폴더명 지정
        # print(fname2+"를 result"+str(i)+".bmp로 파일명을 변경합니다.")
        # os.rename(current_folder+"/"+fname2, current_folder+"/"+"이미지"+str(i)+".bmp")
        # i = i+1
