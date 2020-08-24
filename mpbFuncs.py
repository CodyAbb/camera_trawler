from selenium import webdriver
opts = webdriver.ChromeOptions()
#This option stops the browser from popping up
opts.headless =True
driver = webdriver.Chrome("./chromedriver", options=opts)

def mpbCameras(brand):
    print('MPB')
    print('-' * 10)

    brandSeach = ''

    #This statement gets around the fuji naming convention on MPB's site
    if brand == 'fujifilm':
        brandSearch = 'used-fuji-x-series'
    else :
        brandSeach = f'used-{brand}-compact-system'

    def generateCameraInfo(cameras):
        for camera in cameras:
            try:
                model = camera.find_element_by_class_name('www-model-list-name').text
                try:
                    price = camera.find_element_by_class_name('www-model-min-price').text
                except:
                    price = "Price Not Available"
                try:
                    product_link = camera.find_element_by_tag_name('a').get_attribute('href')
                except:
                    product_link = "Link Not Available"
                print(model)
                print(f'From {price}')
                print(product_link)
                print('-' * 50)
            except:
                pass

    driver.get(f'https://www.mpb.com/en-uk/used-equipment/used-photo-and-video/used-compact-system-cameras/{brandSeach}-cameras/')
    mirrorlessCameras = driver.find_elements_by_class_name('theme-category-model-list-item')
    generateCameraInfo(mirrorlessCameras)

    driver.get(f'https://www.mpb.com/en-uk/used-equipment/used-photo-and-video/used-digital-slr-cameras/used-{brand}-digital-slr-cameras/')
    dslrCameras = driver.find_elements_by_class_name('theme-category-model-list-item')
    generateCameraInfo(dslrCameras)