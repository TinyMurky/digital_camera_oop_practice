from Picture import Picture


class StorageCard():
    def __init__(self, totalStorage):
        if not isinstance(totalStorage, (int, float)):
            raise TypeError('totalStorage should be int or float')
        self._totalStorage = totalStorage
        self._storageUsed = 0
        self._storage = []

    # 存放的picture只可以用index取出，不可以set
    def __getitem__(self, idx):
        return self._storage[idx]

    def __len__(self):
        return len(self._storage)

    def getPicByIndex(self, idx):
        return self[idx]

    def add(self, pic):
        if not isinstance(pic, Picture):
            raise TypeError('This storage card can only store Picture type of data')

        # 如果還有空間才可以存入照片
        newStorageUsed = self._storageUsed + pic.size
        if newStorageUsed > self.totalStorage:
            raise MemoryError('Storage card is run out of storage.')
        self._storageUsed = newStorageUsed
        self._storage.append(pic)

    # 刪除pic by id
    def __delitem__(self, index):
        if index >= len(self._storage):
            raise IndexError("Index is out of range of stored picture array")
        # 已使用空間九除要刪去的檔案
        self._storageUsed -= self._storage[index].size
        del self._storage[index]

    def deleteByIndex(self, index):
        del self[index]

    def deleteByPic(self, pic):
        if not isinstance(pic, Picture):
            raise TypeError('This storage card can only remove Picture type of data')

        # 如果pic 不在_storage中，reraise error
        try:
            index = self._storage.index(pic)
        except ValueError:
            raise ValueError('The picture you try to remove is not in the storage card.')

        self._storageUsed -= self._storage[index].size
        del self._storage[index]

    def formatCard(self):
        # reset整張記憶卡
        self._storageUsed = 0
        del self._storage
        self._storage = []

    #-------------------------------------
    # 以下為getter與setter
    # totalStorage只可以get不可以更改
    @property
    def totalStorage(self):
        return self._totalStorage

    def getTotalStorage(self):
        return self.totalStorage

    # storageUsed也只能get不可以直接set  
    @property
    def storageUsed(self):
        return self._storageUsed

    def getStorageUsed(self):
        return self.storageUsed

    # 剩餘的storage
    @property
    def storageRemain(self):
        return self.totalStorage - self.storageUsed

    def getStorageRemain(self):
        return self.storageRemain

    # -----------------------
    # repr 與 str
    def __repr__(self):
        className = self.__class__.__name__
        return f"{className}(totalStorage={self.totalStorage})"

    def __str__(self):
        className = self.__class__.__name__
        return f"{className}:{{\n\ttotalStorage: {self.totalStorage} mb\n\tstorageUsed: {self.storageUsed} mb\n\tstorageRemain: {self.storageRemain} mb\n\tPicture Amount: {len(self)}}}"


class SixteenGBStorageCard(StorageCard):
    def __init__(self):
        totalStorage = 16 * 1024  # 用mb表述儲存空間
        super(SixteenGBStorageCard, self).__init__(totalStorage)
