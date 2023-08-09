from PictureFileFormat import JPG, PNG


class Picture():
    def __init__(self,
                 pixelHeight: int = 1920,
                 pixelWidth: int = 1080,
                 fileFormat: str = "JPG",
                 *,
                 content=None):  # 先用content代表picture的內容

        # 檢查輸入的type
        if not isinstance(pixelHeight, int):
            raise TypeError("Only integer are allowed in pixalHeight")

        if not isinstance(pixelWidth, int):
            raise TypeError("Only integer are allowed in pixalWidth")

        self._pixelHeight = pixelHeight
        self._pixelWidth = pixelWidth
        self._fileFormat = self._fileTypeSwitch(fileFormat)
        self._content = content

        # 設定一張圖片佔多少mb
        self._size = self._pixelHeight *\
            self._pixelWidth *\
            self._fileFormat.mbPixelRatio

    def _fileTypeSwitch(self, fileFormat: str):
        match fileFormat:
            case "PNG" | "png" | ".png":
                return PNG()
            case _:  # default選JPG
                return JPG()

    # fileFormat 的 setter與getter
    @property
    def fileFormat(self):
        return self._fileFormat.name

    @fileFormat.setter
    def fileFormat(self, newFormat: str):
        self._fileFormat = self._fileTypeSwitch(newFormat)

    # 也可以用function來更改
    def setFormat(self, newFormat: str):
        self._fileFormat = self._fileTypeSwitch(newFormat)

    # Picture 的大小，單位為mb
    @property  # 用getter把size設定成 read only
    def size(self):
        return self._size

    def getSize(self):  # 也可以用function來取得
        return self.size

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
        # 重新設定一張圖片佔多少mb
        self._size = self._pixelHeight *\
            self._pixelWidth *\
            self._fileFormat.mbPixelRatio

    # 也可以用function set或get
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
        # 重新設定一張圖片佔多少mb
        self._size = self._pixelHeight *\
            self._pixelWidth *\
            self._fileFormat.mbPixelRatio

    # 也可以用function set或get
    def getPixelWidth(self):
        return self.pixelWidth

    def setPixelWidth(self, newWidth: int):  # 也可以用function
        self.pixelWidth = newWidth

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

    # repr與 str, 用來print出instance
    def __repr__(self):
        picPixelHeight = f'pixelHeigh={self.pixelHeight}'
        picPixelWidth = f'pixelWidth={self.pixelWidth}'
        picFormat = f'fileFormat="{self.fileFormat}"'
        picContent = f'content="{self.content}"'
        return f'Picture({picPixelHeight}, {picPixelWidth}, {picFormat}, {picContent})'

    def __str__(self):
        className = self.__class__.__name__
        picFormat = f'Format: {self.fileFormat}'
        picPixel = f'Height * Width: {self.pixelHeight} * {self.pixelWidth}'
        picSize = f'Size: {self.size}'
        picContent = f'Content: {self.content}'
        return f'{className}:{{\n\t{picFormat},\n\t{picPixel},\n\t{picSize},\n\t{picContent}\n}}'
