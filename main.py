from Camera import NiconCamera
from Lens import TwoMillionLens
from StorageCard import OneGBStorageCard

nicon = NiconCamera()

print("測試1: 直接輸出Camara資訊")
print(nicon, "\n")

print("測試2: 拍照")
nicon.capture("測試照片")
print("檢查是否存入記憶卡:\n", nicon.storageCard)
print("檢視第0張照片:\n", nicon[0], "\n")

print("測試3: 刪除照片")
del nicon[0]
print("檢查是否從記憶卡刪除:\n", nicon.storageCard)
print("檢查nicon[0]是否還存放圖片:")
try:
    print("\t", nicon[0])
except:
    print("\tnicon[0]已正確刪除\n")

print("測試4: 修改camara的各參數")
# 修改儲存type
nicon.fileFormat = 'png'
nicon.lens.apertureLimits = [1, 2]  # 光圈上下限必須敬入鏡頭內改，禁止直接從camera更改
nicon.aperture = 1  # camera 可以直接set 光圈
nicon.lens.focalLengthLimits = [1, 2]  # 焦距上下限必須敬入鏡頭內改，禁止直接從camera更改
nicon.focalLength = 1  # camera 可以直接 set焦距
print("更改完的nicon:\n", nicon, "\n")

print("測試5: 更換鏡頭與記憶卡")
print("原本是800萬像素與16GB, 更改為200萬像素與1GB, 並拍照")
twoMillionLens = TwoMillionLens()
oneGBStorageCard = OneGBStorageCard()
nicon.setLens(twoMillionLens)
nicon.setStorageCard(oneGBStorageCard)
nicon.capture("測試照片2")
nicon.capture("測試照片3")
nicon.capture("測試照片4")
print("結果：\n", nicon, "\n")
print("照片:\n", "\n".join([str(i) for i in nicon[0:]]))
