import os, zipfile
print("""Welcome to the zip bomb generator!\nThis will make a nonmalicious zip bomb.""")
file_name = input("What would you like to call the zip bomb?: ")
file_size = int(input("What do you want the the unforked zip bomb file size to be(in MB)?: "))
file_count = int(input("What do you want the file count inside of the zip file to be?: "))
zip_file_name = input("What do you want the name of the files inside of the zip file to be?: ")
zip_file_format = input("What format do you want the file format of the files inside of the zip file to be?: ")
def create_files(zip_bomb_file_name,file_name,file_format, file_size,file_count):
    try:
        with zipfile.ZipFile(f'{zip_bomb_file_name}.zip', mode='w') as zip: 
            for i in range(file_count):
                print(f"Opened for iteration {i}")
                n = open(f'{file_name}-{i}.{file_format}','w')
                print(f"Opened file {file_name}.{file_format}")
                n.write(int((file_size/file_count)*512)*'01')
                print(f"Wrote for iteration {i}")
                n.close()
                zip.write(f'{file_name}-{i}.{file_format}')
                os.remove(f'{file_name}-{i}.{file_format}')
            zip.close()

    except Exception as e:
        print('Error in process. Exiting Maker.')
        print(e)

create_files(file_name,zip_file_name,zip_file_format,file_size,file_count)
