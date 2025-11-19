import os
import shutil

def copy_directory_recursively(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        raise Exception("Source directory does not exist")

    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)


    if os.path.isfile(source_dir):
        shutil.copy(source_dir, destination_dir)
    else:
        os.mkdir(destination_dir)
        directory_list = os.listdir(source_dir)

        for path in directory_list:
            new_source_dir = os.path.join(source_dir, path)
            new_destination_dir = os.path.join(destination_dir, path)
            copy_directory_recursively(new_source_dir, new_destination_dir)

