from selenium import webdriver
import requests,time

#this program downloads facebook photos

##########
#enter the following into a python3 terminal:
##########

browser = webdriver.Firefox()
#log in to facebook in the browser. navigate to the slideshow
#of the album you want to download

#variable to hold current url in the loop
pic_url = ''
#url of last picture in slideshow
#copy and paste the starting/finishing picture url in the slideshow (start with this one)
#use 'view image' to get url
startlink = 'put_url_here'
i = 1
#copy and paste the following into the command line, then press enter twice to run
#note that the directory where pictures are saved needs to already exist
#loop until last picture is reached
while pic_url != startlink:
    #the main picture in the slidehow has class spotlight
    pic = browser.find_element_by_css_selector('.spotlight')
    print('found spotlight')
    #select the url for the main picture source
    pic_url = pic.get_attribute('src')
    print('got spotlight source')
    #go to main picture source
    browser.get(pic_url)
    print('going to pic url')
    #find the picture in the main picture source (possibly not necessary...?)
    #instead just click???
    pic = browser.find_element_by_css_selector('img')
    print('found image')
    #click to make picture bigger
    pic.click()
    print('clicked on image')
    #open the url in requests
    pic_site = requests.get(browser.current_url)
    print('created image requests site')
    #test that it worked out?
    pic_site.raise_for_status()
    print('image requests site ok')
    #I think the next line is not needed
    #pic = browser.find_element_by_css_selector('img')
    #make an image file using the url
    #save the file in folder 'myfbphotos' (this folder needs to already exist)
    pic_name = 'fb_photo' + str(i)
    i = i+1
    imagefile = open(os.path.join('fb_photos', os.path.basename(pic_name)), 'wb')
    print('created imagefile')
    #use requests to download picture to file
    for chunk in pic_site.iter_content(100000):
        imagefile.write(chunk)
    print('wrote imagefile to disk')
    #go back
    browser.execute_script('window.history.go(-1)')
    print('went back')
    #wait for page to load???
    time.sleep(10)
    print('waited 10 second')
    #click to go to next picture
    pic = browser.find_element_by_css_selector('.spotlight')
    print('found main picture again')
    pic.click()
    #the rest is redundant to try to get the escape sequence to work right
    pic = browser.find_element_by_css_selector('.spotlight')
    print('found redundant spotlight')
    # select the url for the main picture source
    pic_url = pic.get_attribute('src')
    print('found redundant source')
