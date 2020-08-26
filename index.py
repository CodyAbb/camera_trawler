# from cameraJungleFuncs import camera_jungle_cameras
# from mpbFuncs import mpb_cameras
# from wexPhotography import wex_photography_cameras
from functions import create_csv_from_generated_data

print('''\
  _____                                 _______                 _           
 / ____|                               |__   __|               | |          
| |     __ _ _ __ ___   ___ _ __ __ _     | |_ __ __ ___      _| | ___ _ __ 
| |    / _` | '_ ` _ \ / _ \ '__/ _` |    | | '__/ _` \ \ /\ / / |/ _ \ '__|
| |___| (_| | | | | | |  __/ | | (_| |    | | | | (_| |\ V  V /| |  __/ |   
 \_____\__,_|_| |_| |_|\___|_|  \__,_|    |_|_|  \__,_| \_/\_/ |_|\___|_|   
    
    ''')
print('Searches used camera sites and creates a CSV of the options available, including price and URL links')
print('\n')
print('Try Fujifilm, Sony, Canon, etc...')
user_input_brand = input('Please input a camera brand: ')
user_input_csv_file_name = input('What would you like the CSV file to be called (don\'t append .csv): ')

create_csv_from_generated_data(user_input_brand.lower(), user_input_csv_file_name)