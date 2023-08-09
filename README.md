# Digital Camara OOP Practice

## 簡介
本練習使用Python物件導向建立數位相機class以及它使用的鏡頭(用於產生圖片)、記憶卡(存放圖片)。

由於Python沒有區分private與public，因此class中的variable名稱前方會添加底線`_`，並使用Python 的getter、setter去提取與更改variable

例如：
```python
    def __init__(self, mbPixelRatio):
        self._mbPixelRatio = mbPixelRatio

    @property
    def mbPixelRatio(self) -> float:
        return self._mbPixelRatio

    @mbPixelRatio.setter
    def mbPixelRatio(self, newRatio: float):
        self._mbPixelRatio = newRatio
```
可以使用以下方法get與set`_mbPixelRatio`
```python
# get
self.mbPixelRatio
# set
self.mbPixelRatio = xxx
```

測試檔案為`main.py`，可直接由python3執行

## 主要Class

|Class Name|功能|
|:--|:--|
|PictureFileFormat|有JPG與PNG兩種，設定1 pixel會佔據多少mb的容量|
|Picture|存放PictureFileFormat, 圖片的內容(目前已字串代替), 圖片的長與寬|
|Lens|可設定光圈與焦距並拍攝照片，可以依照設定的PicturFileFormat與圖片長寬生成圖片|
|StorageCard|設有array儲存圖片，並紀錄記憶卡已使用容量與總容量|
|Camera|為操作Lens與Storage Card的界面，可新增照片存入記憶卡，也可以刪除圖片|

## 主要Function(getter與setter未列入)
### Camera
|Function Name|功能|
|:--|:--|
|getPicture|依照index回傳記憶卡中的相片，也可以直接使用`camera[i]` 取出|
|deletePicById|依照index刪除記憶卡中的相片，也可以使用`del camera[i]`|
|deleteByPic|可直接指定要刪除某個Picture物件|
|formatCard|可清除記憶卡中所有檔案|
|checkStorageCard|Print Camera中的記憶卡資訊|
|checkLens|Print Camera中的鏡頭資訊|

### StorageCard
|Function Name|功能|
|:--|:--|
|getPicByIndex|依照index回傳記憶卡中的相片，也可以直接使用`storageCard[i]` 取出|
|add|儲存Picture|
|deleteByIndex|依照index刪除記憶卡中的相片，也可以使用`del storageCard[i]`|
|deleteByPic|可直接指定要刪除某個Picture物件|
|formatCard|可清除記憶卡中所有檔案|

### Lens
|Function Name|功能|
|:--|:--|
|capture|依照鏡頭設定回傳相對應之Picture物件|