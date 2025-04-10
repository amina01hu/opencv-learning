import cv2 #importing opencv

img = cv2.imread("assets/amina.jpg", cv2.IMREAD_COLOR) #reading image from assets
print(img.shape)
print(img[0, 0])
# rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(rgb_img[0, 0])
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img[i, j] = max(254, img[i, j] * 2)
cv2.imshow("Amina", img) #showing image
cv2.waitKey(0) #freezes program when a key is clicked
cv2.destroyAllWindows() #closes all the windows

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("assets/amina_gray.jpg", gray_img)