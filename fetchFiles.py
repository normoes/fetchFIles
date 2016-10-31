import os
import shutil


#temp_dir = r'C:\Temp\Python_Backup'

def fetchFilesFrom(root_dirs, file_extensions):
    print 'Start:'
    file_list = list()
    for root_dir in root_dirs:
        for root, subFolders, files in os.walk(root_dir):
            ## get file extension
            filenames = [os.path.join(root, name) for name in files for e in file_extensions if os.path.splitext(os.path.join(root, name))[1] == e ]
            #for name in filenames:
            #    print name
            for name in filenames:
                file_list.append(os.path.join(root, name));
    print 'Done.'
    print '---------'
    return file_list

def emptyCreateTarget(path):
    if os.path.exists(path):
        #if os.path.getsize(path) > 0:
        try:
            shutil.rmtree(path)
        except Exception, e:
            print e
    try:
        os.makedirs(path)
        return True
    except Exception, e:
        print e
    return False

if __name__ == '__main__':
    #root_dirs = (r'C:\Users\nom\Documents\SVN\old\src', )
    #target_dir = r'C:\Users\nom\Documents\SVN\modelmakerOLDsources'
    root_dirs = (r'C:\Users\nom\Documents\SVN\CodeBeamer\src', r'C:\Users\nom\Documents\SVN\CodeBeamer_Components\trunk')

    target_dir = r'C:\Users\nom\Documents\SVN\modelmakerNEWsources'

    if emptyCreateTarget(target_dir):
        file_extensions = ('.dfm', '.pas')
        #files = list()
        dry_run = True
        files = fetchFilesFrom(root_dirs=root_dirs, file_extensions=file_extensions)
        for name in files:
            print name
            try:
                shutil.copy(name, target_dir)
                print 'copied'
            except Exception, e:
                print e
