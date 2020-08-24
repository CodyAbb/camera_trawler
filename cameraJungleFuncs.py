from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.headless =True
driver = webdriver.Chrome("./chromedriver", options = opts)

def cameraJungleCameras(brand):
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
                try:
                    product_link = camera.find_element_by_tag_name('a').get_attribute('href')
                except:
                    product_link = "Link Not Available"
                print(model)
                print(price)
                print(stock_level)
                print(product_link)
                print('-' * 50)
            except:
                pass

    # Example, navigate to camera type and populate camera list
    driver.get(f'https://www.camerajungle.co.uk/cameras/digital-slr-cameras/{brand}')
    mirrorlessCameras = driver.find_elements_by_class_name('product-lister')
    generateCameraInfo(mirrorlessCameras)

    driver.get(f'https://www.camerajungle.co.uk/cameras/mirrorless/{brand}')
    mirrorlessCameras = driver.find_elements_by_class_name('product-lister')
    generateCameraInfo(mirrorlessCameras)

    driver.get(f'https://www.camerajungle.co.uk/cameras/compact-cameras/{brand}')
    compactCameras = driver.find_elements_by_class_name('product-lister')
    generateCameraInfo(compactCameras)