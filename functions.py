from selenium import webdriver
from yaspin import yaspin
import pandas as pd

#This option stops the browser from popping up
opts = webdriver.ChromeOptions()
opts.headless =True

driver = webdriver.Chrome("./chromedriver", options = opts)

#Entry point function for terminal input
@yaspin(text="Searching...")
def create_csv_from_generated_data(brand, file_name):
    #These lists will contain data from all website sources for csv_write
    model_list = []
    price_list = []
    stock_level_list = []
    product_link_list = []

    # Function that works with Camera Jungle's HTML layout
    def camera_jungle_cameras(brand):

        def generate_camera_info_for_csv(cameras):
            for camera in cameras:
                try:
                    model = camera.find_element_by_tag_name('h4').text
                    try:
                        price = camera.find_element_by_class_name('price').text
                    except:
                        price = "Price Not Available"
                    try:
                        stock_level = camera.find_element_by_class_name('stock').text[1]
                    except:
                        stock_level = "None Available"
                    try:
                        product_link = camera.find_element_by_tag_name('a').get_attribute('href')
                    except:
                        product_link = "Link Not Available"
                    model_list.append(model)
                    price_list.append(price)
                    stock_level_list.append(stock_level)
                    product_link_list.append(product_link)
                except:
                    pass

        # Example, navigate to camera type and populate camera list
        driver.get(f'https://www.camerajungle.co.uk/cameras/digital-slr-cameras/{brand}')
        dslr_cameras = driver.find_elements_by_class_name('product-lister')
        camera_jungle_dslr_information_lists = generate_camera_info_for_csv(dslr_cameras)

        driver.get(f'https://www.camerajungle.co.uk/cameras/mirrorless/{brand}')
        mirrorless_cameras = driver.find_elements_by_class_name('product-lister')
        camera_jungle_mirrorless_information_lists = generate_camera_info_for_csv(mirrorless_cameras)

        driver.get(f'https://www.camerajungle.co.uk/cameras/compact-cameras/{brand}')
        compact_cameras = driver.find_elements_by_class_name('product-lister')
        camera_jungle_compact_information_lists = generate_camera_info_for_csv(compact_cameras)


    # Function that works with MPB's HTML layout
    def mpb_cameras(brand):
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
                    model_list.append(model)
                    price_list.append(price)
                    stock_level_list.append(stock_level)
                    product_link_list.append(product_link)
                except:
                    pass

        driver.get(f'https://www.mpb.com/en-uk/used-equipment/used-photo-and-video/used-compact-system-cameras/{brand_search}-cameras/')
        mirrorless_cameras = driver.find_elements_by_class_name('theme-category-model-list-item')
        generate_camera_info(mirrorless_cameras)

        driver.get(f'https://www.mpb.com/en-uk/used-equipment/used-photo-and-video/used-digital-slr-cameras/used-{brand}-digital-slr-cameras/')
        dslr_cameras = driver.find_elements_by_class_name('theme-category-model-list-item')
        generate_camera_info(dslr_cameras)

    # Function that works with Wex Photo Video's HTML layout
    def wex_photography_cameras(brand):
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
                    model_list.append(model)
                    price_list.append(price)
                    stock_level_list.append('Not Applicable')
                    product_link_list.append(product_link)
                except:
                    pass

        driver.get(f'https://www.wexphotovideo.com/used-cameras/#esp_category_cf=Manufacturer&esp_category_filter_Manufacturer={brand_search}&esp_category_viewall=y')
        brand_cameras = driver.find_elements_by_class_name('listing-product')
        generate_camera_info(brand_cameras)

    #Takes data from compiled lists and combines into csv
    #with table headings
    def create_csv(file_name):
        df = pd.DataFrame(list(zip(model_list, price_list, stock_level_list, product_link_list)), columns=['Model', 'Item_Price', 'Stock_Available', 'Link_To_Product'])
        df.to_csv(f'{file_name}.csv', index=False)

    camera_jungle_cameras(brand)
    mpb_cameras(brand)
    wex_photography_cameras(brand)
    create_csv(file_name)

    #Important that driver is only quit at the end of all sites being opened
    driver.quit()
