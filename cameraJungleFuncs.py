from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.headless =True
driver = webdriver.Chrome("./chromedriver", options = opts)

def cameraJungleCameras():
    print('Camera Jungle')
    print('-' * 10)
    
    # cycles through cameras populating and printing data
    def generateCameraInfo(cameras):
        for camera in cameras:
            try:
                model = camera.find_element_by_tag_name('h4').text
                try:
                    price = camera.find_element_by_class_name('price').text
                except:
                    price = "Price Not Available"
                try:
                    stock_level = camera.find_element_by_class_name('stock').text
                except:
                    stock_level = "None Available"
                print(model)
                print(price)
                print(stock_level)
                print('-' * 50)
            except:
                pass

    # Example, navigate to camera type and populate camera list
    driver.get('https://www.camerajungle.co.uk/cameras/digital-slr-cameras/fujifilm')
    mirrorlessCameras = driver.find_elements_by_class_name('product-lister')
    generateCameraInfo(mirrorlessCameras)

    driver.get('https://www.camerajungle.co.uk/cameras/mirrorless/fujifilm')
    mirrorlessCameras = driver.find_elements_by_class_name('product-lister')
    generateCameraInfo(mirrorlessCameras)

    driver.get('https://www.camerajungle.co.uk/cameras/compact-cameras/fujifilm')
    compactCameras = driver.find_elements_by_class_name('product-lister')
    generateCameraInfo(compactCameras)