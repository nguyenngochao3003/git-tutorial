import cv2

# #show anh
# img= cv2.imread('images.jpg', cv2.IMREAD_GRAYSCALE)
# #show anh
# cv2.imshow('Anh', img)       
# #dong tat ban phim
# cv2.waitKey(5000)         
# # dong tat cua so  
# cv2.destroyAllWindows() 


# # ///mo camera

# camera_id = 0


# #mo camera
# cap = cv2.VideoCapture(camera_id)
# #doc anh tu camera
# while(True):
#     # doc anh
#     ret, frame = cap.read()
#     # hien anh
#     cv2.imshow('cam',frame)

#     # kiem tra neu bam q thi thoat
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# # giai phong camera

# cap.release()
# cv2.destroyAllWindows()

# # // bien anh mau thanh anh xam
# image = cv2.imread('images.jpg')
# cv2.imshow("anh mau", image)
# cv2.waitKey()
# img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# cv2.imshow("anh xam", img_gray)
# cv2.waitKey()
# cv2.destroyAllWindows()

###imread, imwrite, imshow, resize,cvtcolor, waikey, destroyallwindow(), videocapture, threshold
## libary imutils .rotate(image, 90)


# import imutils

# image = cv2.imread('images.jpg')
# cv2.imshow("anh mau", image)
# cv2.waitKey()
# img_resize = cv2.resize(image,dsize=None, fx=0.5, fy=0.5)
# img_rotate = imutils.rotate(image, 90)

# cv2.imshow("anh rotate", img_rotate)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ham threshold


img = cv2.imread("images.jpg")
cv2.imshow("anh mau",img)
cv2.waitKey()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray,threshold1=100, threshold2=200)

cv2.imshow("edges",edges)
cv2.waitKey()
cv2.destroyAllWindows()


