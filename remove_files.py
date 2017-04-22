import os

my_path = r"C:\Users\Acer\Desktop\book1-exercises-master\chp09\practice_files\little pics"

for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        path = os.path.join(current_folder, file_name)
        # check if file is a jpg
        check_pic = file_name.lower().endswith(".jpg")
        # check if file is less than 2kb
        check_size = os.path.getsize(path) < 2000
        if check_pic and check_size == True:
            print ('Deleting "{}" ...'.format(file_name))
            os.remove(path)
