from selenium import webdriver
opts = webdriver.ChromeOptions()
#This option stops the browser from popping up
opts.headless =True
driver = webdriver.Chrome("./chromedriver", options=opts)

def mpb_cameras(brand):
    print('MPB')
    print('-' * 10)

    brand_search = ''

    #This statement gets around the fuji naming convention on MPB's site
    if brand == 'fujifilm':
        brand_search = 'used-fuji-x-series'
    else :
        brand_search = f'used-{brand}-compact-system'

    def generate_camera_info(cameras):
        for camera in cameras:
            try:
                model = camera.find_element_by_class_name('www-model-list-name').text
                try:
                    #Having to use xpath to fix strange min_price bug
                    price = camera.find_element_by_xpath(f'//*[@id="www-listing"]/li[{(cameras.index(camera) + 1)}]/article/ul/li[3]/h5/strong/span').text
                except:
                    price = "Price Not Available"
                try:
                    stock_level = camera.find_element_by_class_name('www-model-available').text
                except:
                    stock_level = "1"
                try:
                    product_link = camera.find_element_by_tag_name('a').get_attribute('href')
                except:
                    product_link = "Link Not Available"
                print(model)
                print(f'From {price}')
                print(f'({stock_level} available)')
                print(product_link)
                print('-' * 50)
            except:
                pass

    driver.get(f'https://www.mpb.com/en-uk/used-equipment/used-photo-and-video/used-compact-system-cameras/{brand_search}-cameras/')
    mirrorless_cameras = driver.find_elements_by_class_name('theme-category-model-list-item')
    generate_camera_info(mirrorless_cameras)

    driver.get(f'https://www.mpb.com/en-uk/used-equipment/used-photo-and-video/used-digital-slr-cameras/used-{brand}-digital-slr-cameras/')
    dslr_cameras = driver.find_elements_by_class_name('theme-category-model-list-item')
    generate_camera_info(dslr_cameras)