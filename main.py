import os, shutil

dict_extentions = {
    'audio_extentions' : ('.mp3', '.m4a', '.wav', '.flac','.aif','.cda','.iff','.mid','.midi','.mpa','.wma','.wpl'),
    'video_extentions' : ('.mp4', '.mkv', '.MKV', '.flv', '.avi','.flv','.h264','.mov','.mpg','.mpeg','.rm','.swf','.vob','.wmv','.3gp','.3g2'),
    'doc_extentions' : ('.doc', '.pdf', '.txt', '.docx', '.apk','.bat', '.bin', '.cgi', '.com','.exe','.jar', '.py' ,'.wsf' ,'.cpp' ,'.c' ,'.java','.odt','.msg','.rtf','.tex','.wks','.wps','.wpd','.ods','.xlr','.xls','.xlsx','.key','.odp','.pps','.ppt','.bak','.cab','.cgf','.cpl','.cur','.dll','.dmp','.drv','.icns','.ico','.ini','.lnk','.msi','.sys','.tmp','.js','.jsp','.php','.part','.rss','.xhtml','.xml','.css','.cfm','.cer','.asp','.aspx','.cgi','.pl'),
}

all_files = []
all_directories = []
Name = "Files"

while(True):
    folderpath = input('\nEnter folder path : ')
    if not os.path.exists(folderpath):
        print("Error, please check the path again!\n")
    else:
        break
    # print(os.path.dirname(folderpath))

print("\n################## TOTAL FILES ##################\n")
#calculating total files and directries
def show_directories(dir_list, path):
    # s = "%s%d%s" %("\n", len(dir_list), "directories of" + os.path.abspath(path))
    # l = len(s)
    # print(s)
    # print("="*l)
    for dir in (dir_list):
        all_directories.append(dir)

def show_files(file_list, path):
    for file in (file_list):
        all_files.append(file)

def show_cwd_contents(path):
    f_list = []
    d_list = list()

    try:
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                f_list.append(f)
            else:
                if os.path.isdir(os.path.join(path, f)):
                    d_list.append(f)

    except:
        print("\nError, please check the path again")
        return

    show_files(f_list, path)
    show_directories(d_list, path)

if __name__ == "__main__":
    show_cwd_contents(folderpath)


    # print("all files: ")
    # print(all_files)
    # print("\nall directories")
    # print(all_directories)



#counting audio video and document files
def file_counter(folder_path, file_extentions, num):
    Count = []
    for file in os.listdir(folder_path):
        for extention in file_extentions:
            if file.endswith(extention):
                Count.append(file)
    if(num == 1):
        print(f"Audio Files    : {len(Count)} files found")
    elif(num == 2):
        print(f"Video Files    : {len(Count)} files found")
    else:
        print(f"Document Files : {len(Count)} files found")

num=0
for ext_type, ext_tupe in dict_extentions.items():
    num+=1
    file_counter(folderpath, ext_tupe, num)
    


#Seperating the files
def file_finder(folder_path, file_extentions):
    files = []
    for file in os.listdir(folder_path):
        for extention in file_extentions:
            if file.endswith(extention):
                files.append(file)
    return files

K=0
for extentnions_type, extentions_tuple in dict_extentions.items():
    folder_name = extentnions_type.split('_')[0] + Name
    folder_path = os.path.join(folderpath, folder_name)
    flag = False
    if(K == 0):
        i=0
        while(i<len(all_directories)):
            if all_directories[i] == 'audioFiles':
                flag=True
            i += 1
        if(not flag):     
            os.mkdir(folder_path)

    elif(K == 1):
        i=0
        while(i<len(all_directories)):
            if all_directories[i] == 'videoFiles':
                flag=True
            i += 1
        if(not flag):     
            os.mkdir(folder_path)

    elif(K == 2):
        i=0
        while(i<len(all_directories)):
            if all_directories[i] == 'docFiles':
                flag=True
            i += 1
        if(not flag):     
            os.mkdir(folder_path)
    K += 1

    for item in (file_finder(folderpath, extentions_tuple)):
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(folder_path, item)
        shutil.move(item_path, item_new_path)
    file_finder(folderpath, extentions_tuple)    

print("\n################# Task Completed ################\n")
print("All Audio files are moved to 'audioFiles' folder ")
print("All Video files are moved to 'videoFiles' folder ")
print("All Document files are moved to 'docFiles' folder ")