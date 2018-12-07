import os

for folderName, subfolders, filenames in os.walk('D:\\BH3_Master\\Assets'):
    if folderName.endswith('\\Editor') :
        print(folderName)
        for filename in filenames:
            if(filename.endswith('.cs')):
                print('  --  ' + filename)

print('HelloWorld')