
class PictureFileFormat():
    '''
    設定照片格式的class，是PNG 與 JPG的super class
    '''
    def __init__(self, name: str, mbPixelRatio: float):
        self._name = name
        self._mbPixelRatio = mbPixelRatio  # 記錄1單位像素可轉換為多少mb

    # 使用 Getter與setter保護原始__init__的值
    @property
    def name(self) -> str:
        return self._name

    @name.setter  # 可用 pictureFileFormat.name 的方法改變 _name
    def name(self, newName: str):
        self._name = newName

    @property
    def mbPixelRatio(self) -> float:
        return self._mbPixelRatio

    @mbPixelRatio.setter
    def mbPixelRatio(self, newRatio: float):
        self._mbPixelRatio = newRatio

    # 直接print Class instance的時候會出現的文字
    def __repr__(self):
        className = self.__class__.__name__
        return f'''{className}(name="{self._name}", mbPixelRatio={self._mbPixelRatio})'''

    def __str__(self):
        pic_type = f"Picture type: {self.__class__.__name__},"
        ext_name = f"Extention File name: {self._name},"
        pixel_ratio = f"Pixel convert to MB Ratio: {self._mbPixelRatio:.5}"
        return f"{pic_type} {ext_name} {pixel_ratio}"


class JPG(PictureFileFormat):
    def __init__(self):

        # JPG 約是 1000萬像素轉 1mb
        super(JPG, self).__init__(name=".jpg", mbPixelRatio=1/10000000)


class PNG(PictureFileFormat):
    def __init__(self):

        # PNG 約是 1mb 可存放350000像素
        super(PNG, self).__init__(name=".png", mbPixelRatio=1/350000)
