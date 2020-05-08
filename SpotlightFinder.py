# Version 1.0.1
import os
import shutil
from os import listdir
from os.path import isfile, join
import get_image_size

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
        # print(os.path.join(dest_directory, file_name + '.' + filename_suffix))
        if not os.path.isfile(os.path.join(dest_directory, file_name + '.' + filename_suffix)):
            new_file = shutil.copy(full_file_name, dest_directory)
            os.rename(new_file, new_file + '.' + filename_suffix)
            print('Image Found -> ' + os.path.join(file_name + '.' + filename_suffix))

print('All Images Can Be Found In -> ' + dest_directory)

images = [f for f in listdir(dest_directory) if isfile(join(dest_directory, f))]

for image in images:
    full_image_name = os.path.join(dest_directory, image)
    try:
        width, height = get_image_size.get_image_size(full_image_name)
        if not width >= 1080:
            os.remove(full_image_name)
    except get_image_size.UnknownImageFormat:
        width, height = -1, -1