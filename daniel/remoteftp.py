import pysftp as sftp

cnopts = sftp.CnOpts()
cnopts.hostkeys = None

myHostname = '107.180.28.75'
myUsername = 'yxkvyuufng4e'
myPassword = 'Kericho152!'

path_file = 'updatedlibrarycatalog.csv'
remote_path = 'booklibrary'

def download_file_to_local():
    with sftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as s:
        print("Connection successfully established...")
        print("Obtaining strcture of remote directory...")
        directory_structure = s.listdir_attr()
        print("Printing data")
        for attr in directory_structure:
            print(attr)
        print("Chdir to Rugutt Library Folder...")
        with s.cd(remote_path):
            booklibrary_structure = s.listdir_attr()
            print("Printing data")
            for attr in booklibrary_structure:
                print(attr)
            try:
                s.get(path_file)
                print("File Successfully Downloaded")
            except:
                print("Could not connect to ftp")

def push_file_to_server():
    with sftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as s:
        print("Connection successfully established...")
        print("Obtaining strcture of remote directory...")
        directory_structure = s.listdir_attr()
        print("Printing data")
        for attr in directory_structure:
            print(attr)
        print("Chdir to Rugutt Library Folder...")
        with s.cd(remote_path):
            booklibrary_structure = s.listdir_attr()
            print("Printing data")
            for attr in booklibrary_structure:
                print(attr)
            try:
                s.put(path_file)
                print("File Successfully Transfer")
            except:
                print("Could not connect to ftp")
