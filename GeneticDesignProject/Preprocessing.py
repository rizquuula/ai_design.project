import cv2 
def preprocessing(img_source,img_size):
    #img_source = str(img_source)
    #img = cv2.imread(img_source)
    img = img_source
    old_size = img.shape[:2]       #Original size
    #print(old_size)     
    # => (288, 352)
    ratio = float(img_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])      #Changed to the new size in same ratio
    #print(ratio,' and ',new_size)      
    # => 0.6363636363636364  and  (183, 224)#
    img = cv2.resize(img, (new_size[1], new_size[0]))

    delta_h = img_size - new_size[0]
    delta_w = img_size - new_size[1]
    #print(delta_w,' and ',delta_h)
    # => 0 and 41
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    #print (top,bottom,left,right)
    # => 20 21 0 0                  // is for integer divide

    #color = [255, 255, 255]
    color = [100, 100, 100]

    new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    #print(new_img.shape)
    #print(new_img)
    #new_img.reshape(-1,img_size,img_size,1)
    #new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    #print(new_img.shape)
    '''a = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print(a)
    a.reshape(-1,2,2,2)
    print(a)'''
    '''
    cv2.imshow('This is image',new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    return new_img