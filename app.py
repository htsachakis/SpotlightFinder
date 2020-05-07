import os
import shutil
from os import listdir
from os.path import isfile, join

filename_suffix = 'jpg'
current_app_dir = os.path.dirname(os.path.realpath(__file__))
dest_directory = os.path.join(current_app_dir,'Spotlight-Images')

SpotlightPath = os.path.join('C:\\','Users',os.getlogin(),'AppData', 'Local','Packages','Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy','LocalState','Assets')
files = [f for f in listdir(SpotlightPath) if isfile(join(SpotlightPath, f))]

if not os.path.exists('Spotlight-Images'):
    os.makedirs('Spotlight-Images')


for file_name in files:
    full_file_name = os.path.join(SpotlightPath, file_name)
    if os.path.isfile(full_file_name):
        new_file = shutil.copy(full_file_name, dest_directory)
        os.rename(new_file, new_file + '.' + filename_suffix)

