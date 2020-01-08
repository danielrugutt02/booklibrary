import remoteftp as ftp
import isbnsorter as isbn

ftp.download_file_to_local()

isbn.update_catalog()

ftp.push_file_to_server()



