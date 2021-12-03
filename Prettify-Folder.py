import os

def prettifyFolder(path, file, ext):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    # print(files)
    with open(file) as f:
        filelist = f.read().split("\n")
    # print(filelist)    
    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        # print(os.path.splitext(file)[1])
        if os.path.splitext(file)[1] == ext:
            os.rename(file, f"{i}{ext}") 
            i += 1
        
prettifyFolder(r"I:\Projects\Python-Practice-Programs\Prettify",     
                r"I:\Projects\Python-Practice-Programs\not_to_read.txt",
                ".jpg")

