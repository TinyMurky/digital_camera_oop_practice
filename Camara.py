from StorageCard import SixteenGBStorageCard, StorageCard
from Lens import EightMillionLens, Lens


class Camera():
    def __init__(self, lens=EightMillionLens(), storageCard=SixteenGBStorageCard()):
        if not isinstance(lens, Lens):
            raise TypeError("lens should be Lens Type")
        if not isinstance(storageCard, StorageCard):
            raise TypeError("storageCard should be StorageCard Type")
        self._lens = lens
        self._storageCard = storageCard

    def capture(self, content: str = ""):
        # 鏡頭生成影像，存放於記憶卡
        newPic = self.lens.capture(content)
        self.storageCard.add(newPic)

    def __getitem__(self, index):
        # 直接用 camera[i]的方法可以直接取出記憶卡內的照片
        return self.storageCard[index]

    def getPicture(self, index):
        # 也可以提供index取出picture
        return self[index]

    # 刪除pic by id
    def __delitem__(self, index):
        # 已使用空間九除要刪去的檔案
        del self.storageCard[index]

    def deletePicById(self, index):
        # 也可以用function刪除
        del self[index]

    def deleteByPic(self, pic):
        # 可以直接把pic物件從記憶卡中刪除
        self.storageCard.deleteByPic(pic)

    def formatCard(self):
        # reset storageCard
        self.storageCard.formatCard()

    def checkStorageCard(self):
        # 查看 StorageCard的狀態
        print(self.storageCard)

    def checkLens(self):
        # 查看鏡頭狀態
        print(self.lens)

    # 設定直接print camara物件會長什麼樣子
    def __repr__(self):
        className = self.__class__.__name__
        return f"{className}(lens={repr(self.lens)}, storageCard={repr(self.storageCard)})"

    def __str__(self):
        className = self.__class__.__name__
        return f"{className}:{{\n\t{str(self.lens)},\n\t{str(self.storageCard)}\n}}"

    # ----------------------
    # 以下是基本屬性的getter與setter
    # 設定圖片的pixel高與寬
    @property
    def pixelHeight(self):
        return self.lens.pixelHeight

    @pixelHeight.setter
    def pixelHeight(self, newHeight: int):
        self.lens.pixelHeight = newHeight

    def getPixelHeight(self):
        return self.pixelHeight

    def setPixelHeight(self, newHeight: int):
        self.pixelHeight = newHeight

    # get/set pixelwidth
    @property
    def pixelWidth(self):
        return self.lens.pixelWidth

    @pixelWidth.setter
    def pixelWidth(self, newWidth: int):
        self.lens.pixelWidth = newWidth

    def getPixelWidth(self):
        return self.pixelWidth

    def setPixelWidth(self, newWidth: int):
        self.pixelWidth = newWidth

    # 設定鏡頭的光圈
    @property
    def aperture(self):
        return self.lens.aperture

    @aperture.setter
    def aperture(self, newAperture):
        # 可以直接更改光圈設定
        self.lens.aperture = newAperture

    def setAperture(self, newAperture):
        # 也可以用function set 光圈
        self.aperture = newAperture

    # 設定鏡頭的焦距
    @property
    def focalLength(self):
        return self.lens.focalLength

    @focalLength.setter
    def focalLength(self, newFocalLength):
        self.lens.focalLength = newFocalLength

    def getFocalLength(self):
        return self.focalLength

    def setFocalLength(self, newFocalLength):
        self.focalLength = newFocalLength

    # fileFormat 的 setter與getter
    # 可以設定要PNG還是JPG
    @property
    def fileFormat(self):
        return self.lens.fileFormat

    @fileFormat.setter
    def fileFormat(self, newFormat: str):
        self.lens.fileFormat = newFormat

    def getFileFormat(self):
        return self.fileFormat

    def setFileFormat(self, newFormat: str):
        self.fileFormat = newFormat    

    # 用property屬性保護原本的_lens與_storageCard
    @property
    def lens(self):
        return self._lens

    @lens.setter
    def lens(self, newLens):
        if not isinstance(newLens, Lens):
            raise TypeError("lens should be Lens Type")
        self._lens = newLens

    def getLens(self):
        return self.lens

    def setLens(self, newLens):
        self.lens = newLens

    @property
    def storageCard(self):
        return self._storageCard

    @storageCard.setter
    def storageCard(self, newCard):
        if not isinstance(newCard, StorageCard):
            raise TypeError("storageCard should be Storage Type")
        self._storageCard = newCard

    def getStorageCard(self):
        return self.storageCard

    def setStorageCard(self, newCard):
        self.storageCard = newCard


class NiconCamera(Camera):
    def __init__(self):
        lens = EightMillionLens()
        storageCard = SixteenGBStorageCard()
        super(NiconCamera, self).__init__(lens, storageCard)
