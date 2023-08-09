from Picture import Picture


class Lens():
    def __init__(self,
                 pixelHeight,
                 pixelWidth,
                 fileFormat,
                 apertureLimits,  # 鏡頭光圈可以接受的上下限
                 focalLengthLimits):  # 鏡頭焦距可以接受上下限
        # 檢查輸入的type
        if not isinstance(pixelHeight, int):
            raise TypeError("Only integer are allowed in pixalHeight")

        if not isinstance(pixelWidth, int):
            raise TypeError("Only integer are allowed in pixalWidth")

        if not self._checkLimitsType(apertureLimits):
            raise TypeError("apertureLimits should be list and contain 2 numbers")

        if not self._checkLimitsType(focalLengthLimits):
            raise TypeError("focalLengthLimits should be list and contain 2 numbers")

        self._pixelHeight = pixelHeight
        self._pixelWidth = pixelWidth
        self._fileFormat = fileFormat  # 拍出的照片格式
        self._apertureLimits = apertureLimits  # 鏡頭光圈可以接受的上下限
        self._aperture = sum(self._apertureLimits)/2  # 鏡頭光圈設定，預定設在limits正中間
        self._focalLengthLimits = focalLengthLimits  # 鏡頭焦距可以接受上下限
        self._focalLength = sum(self._focalLengthLimits)/2  # 鏡頭光圈設定，預定設在limits正中間

    def _checkLimitsType(self, limits):
        # 檢測apertureLimits 與 focalLengthLimits 是list 並且內含兩個int or float
        if isinstance(limits, list) and len(limits) == 2:
            if all(isinstance(limit, (int, float)) for limit in limits):
                return True
        return False

    def capture(self, newContent=""):
        # 拍照，依照鏡頭規格回傳一個Picture 物件
        content = f"Content: {newContent}, Aperture: {self.aperture}, Focal Length: {self.focalLength}"
        picture = Picture(self.pixelHeight, self.pixelWidth, self.fileFormat, content=content)
        return picture

    # -----------------------------------------------
    # 以下是所有__init__內的數值的setter與getter
    # get/set pixelHeight
    @property
    def pixelHeight(self):
        return self._pixelHeight

    @pixelHeight.setter
    def pixelHeight(self, newHeight: int):
        # 檢查輸入的type
        if not isinstance(newHeight, int):
            raise TypeError("Only integers are allowed in pixalHeight") 

        self._pixelHeight = newHeight

    def getPixelHeight(self):
        return self.pixelHeight

    def setPixelHeight(self, newHeight: int):
        self.pixelHeight = newHeight

    # get/set pixelwidth
    @property
    def pixelWidth(self):
        return self._pixelWidth

    @pixelWidth.setter
    def pixelWidth(self, newWidth: int):
        # 檢查輸入的type
        if not isinstance(newWidth, int):
            raise TypeError("Only integers are allowed in pixalHeight") 

        self._pixelWidth = newWidth

    def getPixelWidth(self):
        return self.pixelWidth

    def setPixelWidth(self, newWidth: int):
        self.pixelWidth = newWidth

    # fileFormat 的 setter與getter
    @property
    def fileFormat(self):
        return self._fileFormat

    @fileFormat.setter
    def fileFormat(self, newFormat: str):
        self._fileFormat = self.newFormat

    def getFileFormat(self):
        return self.fileFormat

    def setFileFormat(self, newFormat: str):
        self.fileFormat = newFormat    
    # content setter/getter
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, newContent):
        self._content = newContent

    def getContent(self):
        return self.content

    def setContent(self, newContent):
        self.content = newContent

    @property
    def aperture(self):
        return self._aperture

    @aperture.setter
    def aperture(self, newAperture):
        if not isinstance(newAperture, int):
            raise TypeError("Only integer are allowed in aperture")

        if newAperture < self.apertureLimits[0] or newAperture >= self.apertureLimits[1]:
            raise ValueError('Aperture was set outside of aperture limits ')
        self._aperture = newAperture

    def getAperture(self):
        return self.aperture

    def setAperture(self, newAperture):
        self.aperture = newAperture

    @property
    def focalLength(self):
        return self._focalLength

    @focalLength.setter
    def focalLength(self, newFocalLength):
        if not isinstance(newFocalLength, int):
            raise TypeError("Only integer are allowed in focalLength")

        if newFocalLength < self.focalLengthLimits[0] or newFocalLength >= self.focalLengthLimits[1]:
            raise ValueError('Aperture was set outside of focalLength limits ')
        self._focalLength = newFocalLength

    def getFocalLength(self):
        return self.focalLength

    def setFocalLength(self, newFocalLength):
        self.focalLength = newFocalLength

    @property
    def apertureLimits(self):
        return self._apertureLimits

    @apertureLimits.setter
    def apertureLimits(self, newLimit):
        if not self._checkLimitsType(newLimit):
            raise TypeError("apertureLimits should be list and contain 2 numbers")
        self._apertureLimits = newLimit

    def getApertureLimits(self):
        return self.apertureLimits

    def setApertureLimits(self, newLimit):
        self.apertureLimits = newLimit

    @property
    def focalLengthLimits(self):
        return self._focalLengthLimits

    @focalLengthLimits.setter
    def focalLengthLimits(self, newLimit):
        if not self._checkLimitsType(newLimit):
            raise TypeError("focalLengthLimits should be list and contain 2 numbers")
        self._focalLengthLimits = newLimit

    def getFocalLengthLimits(self):
        return self.focalLengthLimits

    def setFocalLengthLimits(self, newLimit):
        self.focalLengthLimits = newLimit
    
    # str 與 repr
    def __repr__(self):
        className = self.__class__.__name__
        return f"{className}(pixelHeight={self.pixelHeight}, pixelWidth={self.pixelWidth}, fileFormat={self.fileFormat}, apetureLimits={self.apertureLimits}, focalLengthLimits={self.focalLengthLimits})"

    def __str__(self):
        className = self.__class__.__name__
        height = f"pixelHeight: {self.pixelHeight}"
        width = f"pixelWidth: {self.pixelWidth}"
        fileFormat = f"fileFormat: {self.fileFormat}"
        aperture = f"aperture setting: {self.aperture}"
        apertureLimits = f"aperture Limits: {self.apertureLimits}"
        focalLength = f"focalLength setting: {self.focalLength}"
        focalLengthLimits = f"focalLength Limits: {self.focalLengthLimits}"

        return f"{className}:{{\n\t{height},\n\t{width},\n\t{fileFormat},\n\t{aperture},\n\t{apertureLimits},\n\t{focalLength},\n\t{focalLengthLimits}\n}}"


class EightMillionLens(Lens):
    # 4k 800萬畫素鏡頭
    def __init__(self):
        pixelHeight = 4196
        pixelWidth = 2160
        fileFormat = "JPG"
        apertureLimits = [1, 20]
        focalLengthLimits = [24, 500]
        super(EightMillionLens, self).__init__(
            pixelHeight,
            pixelWidth,
            fileFormat,
            apertureLimits,
            focalLengthLimits
        )

