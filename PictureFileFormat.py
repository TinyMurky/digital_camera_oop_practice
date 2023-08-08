
class PictureFileFormat():
    '''
    設定照片格式的class，是PNG 與 JPG的super class
    '''
    def __init__(self, name: str, mbPixelRatio: float):
        self._name = name
        self._mbPixalRatio = mbPixelRatio  # 記錄1單位像素可轉換為多少mb

    # 使用 Getter與setter保護原始__init__的值
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter  # 可用 pictureFileFormat.name 的方法改變 _name
    def name(self, newName: str):
        self._name = newName

    @property
    def mbPixalRatio(self) -> float:
        return self._mbPixalRatio

    @mbPixalRatio.setter
    def mbPixalRatio(self, newRatio: float):
        self._mbPixalRatio = newRatio


class JPG(PictureFileFormat):
    def __init__(self):

        # JPG 約是 1000萬像素轉 1mb
        super(JPG, self).__init__(name="JPG", mbPixelRatio=1/10000000)


class PNG(PictureFileFormat):
    def __init__(self):

        # PNG 約是 1mb 可存放350000像素
        super(JPG, self).__init__(name="JPG", mbPixelRatio=1/350000)
