from selenium import webdriver

#This option stops the browser from popping up
opts = webdriver.ChromeOptions()
opts.headless =True

driver = webdriver.Chrome("./chromedriver", options=opts)

def wex_photography_cameras(brand):
    print('Wex Photography')
    print('-' * 10)

    brand_search = ''

    if brand == 'fujifilm':
        brand_search = 'Fuji'
    else:
        brand_search = brand.capitalize()

    def generate_camera_info(cameras):
        for camera in cameras:
            try:
                model = camera.find_element_by_tag_name('h3').text.split('Used ')[1]
                try:
                    price = camera.find_element_by_class_name('price').text
                except:
                    price = 'Price Not Available'
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

    driver.get(f'https://www.wexphotovideo.com/used-cameras/#esp_category_cf=Manufacturer&esp_category_filter_Manufacturer={brand_search}&esp_category_viewall=y')
    brand_cameras = driver.find_elements_by_class_name('listing-product')
    generate_camera_info(brand_cameras)

    driver.quit()
