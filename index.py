from cameraJungleFuncs import cameraJungleCameras
from mpbFuncs import mpbCameras

print('''\
  _____                                 _______                 _           
 / ____|                               |__   __|               | |          
| |     __ _ _ __ ___   ___ _ __ __ _     | |_ __ __ ___      _| | ___ _ __ 
| |    / _` | '_ ` _ \ / _ \ '__/ _` |    | | '__/ _` \ \ /\ / / |/ _ \ '__|
| |___| (_| | | | | | |  __/ | | (_| |    | | | | (_| |\ V  V /| |  __/ |   
 \_____\__,_|_| |_| |_|\___|_|  \__,_|    |_|_|  \__,_| \_/\_/ |_|\___|_|   
    
    ''')
print('Searches used camera sites and returns a list of the options available, including price and URL links')
print('\n')
userInput = input('Please input a camera brand: ')

cameraJungleCameras(userInput.lower())
print('\n')
mpbCameras(userInput.lower())
