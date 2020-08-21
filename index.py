from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")

driver.get('https://www.camerajungle.co.uk/cameras/mirrorless/fujifilm')

cameraJungleCameras = driver.find_elements_by_class_name('product-lister')

print(len(cameraJungleCameras))

