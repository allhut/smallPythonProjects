import os



def rename_files():
    list_file = os.listdir(r"C:\Users\inderjex\Videos\prank\prank");
    dir_path = r'C:\Users\inderjex\Videos\prank\prank';

    # we can also change working directory to prank and do rename and revert it back
    #prev_path = os.getcwd();
    #os.chdir(dir_path); at end os.chdir(prev_path);
    for file in list_file:
        if file.endswith(".jpg"):
            result = ''.join([i for i in file if not i.isdigit()]);
            #or file.translate(none,0123456789);
            os.rename(dir_path+'\\'+file, dir_path+'\\'+result);
        


print ("we are gone encode the Secret message\n");
rename_files();


