from selenium import webdriver
import pandas as pd

#This option stops the browser from popping up
opts = webdriver.ChromeOptions()
opts.headless =True

driver = webdriver.Chrome("./chromedriver", options = opts)

#Entry point function for terminal input
def create_csv_from_generated_data(brand, file_name):
    #These lists will contain data from all website sources for csv_write
    model_list = []
    price_list = []
    stock_level_list = []
    product_link_list = []

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
                        stock_level = camera.find_element_by_class_name('stock').text
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

        driver.quit()

    #Takes data from compiled lists and combines into csv
    #with table headings
    def create_csv(file_name):
        df = pd.DataFrame(list(zip(model_list, price_list, stock_level_list, product_link_list)), columns=['Model', 'Item_Price', 'Stock_Available', 'Link_To_Product'])
        df.to_csv(f'{file_name}.csv', index=False)

    camera_jungle_cameras(brand)
    create_csv(file_name)
