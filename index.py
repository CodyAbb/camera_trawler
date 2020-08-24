from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.headless =True
driver = webdriver.Chrome("./chromedriver", options = opts)

def cameraJungleCameras():
    print('Camera Jungle')
    driver.get('https://www.camerajungle.co.uk/cameras/mirrorless/fujifilm')
    cameraJungleCameras = driver.find_elements_by_class_name('product-lister')

    for camera in cameraJungleCameras:
        try:
            model = camera.find_element_by_tag_name('h4').text
            try:
                price = camera.find_elements_by_class_name('price').text
            except:
                price = "Price Not Available"
            try:
                stock_level = camera.find_elements_by_class_name('stock').text
            except:
                stock_level = "None Available"
            print(model)
            print(price)
            print(stock_level)
            print('-' * 50)
        except:
            pass


cameraJungleCameras()