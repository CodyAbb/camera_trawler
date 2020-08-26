from selenium import webdriver

#This option stops the browser from popping up
opts = webdriver.ChromeOptions()
opts.headless =True

driver = webdriver.Chrome("./chromedriver", options = opts)

def camera_jungle_cameras(brand, output_option):
    print('Camera Jungle')
    print('-' * 10)
    
    # cycles through cameras populating and printing data
    def generate_camera_info_for_terminal(cameras):
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

    def generate_camera_info_for_csv(cameras):
        model_list = []
        price_list = []
        stock_level_list = []
        product_link_list = []

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
        
        return [model_list, price_list, stock_level_list, product_link_list]

    # Example, navigate to camera type and populate camera list
    driver.get(f'https://www.camerajungle.co.uk/cameras/digital-slr-cameras/{brand}')
    dslr_cameras = driver.find_elements_by_class_name('product-lister')

    driver.get(f'https://www.camerajungle.co.uk/cameras/mirrorless/{brand}')
    mirrorless_cameras = driver.find_elements_by_class_name('product-lister')

    driver.get(f'https://www.camerajungle.co.uk/cameras/compact-cameras/{brand}')
    compact_cameras = driver.find_elements_by_class_name('product-lister')

    if output_option == 'terminal':
        generate_camera_info_for_terminal(dslr_cameras)
        generate_camera_info_for_terminal(mirrorless_cameras)
        generate_camera_info_for_terminal(compact_cameras)
    else:
        camera_jungle_dslr_information_lists = generate_camera_info_for_csv(dslr_cameras)
        camera_jungle_mirrorless_information_lists = generate_camera_info_for_csv(mirrorless_cameras)
        camera_jungle_compact_information_lists = generate_camera_info_for_csv(compact_cameras)
    
    driver.quit()