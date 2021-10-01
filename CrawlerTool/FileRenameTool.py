import os


def rename_files(filePath):
    path = filePath
    i = 1
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            new_name = file.replace(file, "%d.jpg" % i)
            os.rename(os.path.join(path, file), os.path.join(path, new_name))
            i += 1

    print("total image {}".format(i-1))

if __name__ == '__main__':
    path = './data_set/香蕉/'
    rename_files(filePath=path)
