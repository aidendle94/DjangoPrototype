class ImageLibrary():
    def __init__(self):
        self.imageLibraryID = None
        self.imageLibrary = {}
    def assembleLibrary(self,Image):
        self.imageLibrary.update(Image.imageID,Image.imageUrl)
        return self.imageLibrary