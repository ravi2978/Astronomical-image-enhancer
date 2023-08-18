import cv2

def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered1 = img
    filtered2 = img
    filtered3 = img
    filtered4 = img
    filtered5 = img
    filtered  = img

    if action == 'NO_FILTER':
        # filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # filtered1 = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
        # width, height = img.shape[:2]
        # if width > 500:
        #         k = (50, 50)
        # elif width > 200 and width <=500:
        #         k = (25,25)
        # else:
        #         k = (10,10)
        # blur = cv2.blur(filtered1, k)
        # filtered2 = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
        # gray = cv2.cvtColor(filtered1, cv2.COLOR_BGR2GRAY)
        # _, filtered2 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        # filtered3 = cv2.threshold(filtered2, 100, 255, cv2.THRESH_BINARY)
        return image
        # filtered5 = cv2.bitwise_not(filtered4)
        # return filtered5    
    elif (action == 'COLORIZED' ):
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        return filtered
    elif (action == 'GRAYSCALE' ):
        filtered1 = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)
        return filtered1
    elif (action == 'BLURRED'):
        width, height = img.shape[:2]
        if width > 500:
                k = (50, 50)
        elif width > 200 and width <=500:
                k = (25,25)
        else:
                k = (10,10)
        blur = cv2.blur(filtered1, k)
        filtered2 = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
        return filtered2
    elif(action == 'BINARY'):
        gray = cv2.cvtColor(filtered2, cv2.COLOR_BGR2GRAY)
        _, filtered3 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        return filtered3
    elif (action == 'INVERT'):
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, filtered4 = cv2.threshold(filtered3, 100, 255, cv2.THRESH_BINARY)
        return filtered4
    filtered5 = cv2.bitwise_not(filtered4)
    return filtered5