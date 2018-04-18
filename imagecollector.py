import os
from urllib import request


class ImageCollector:

    example_img = 'https://s03.video.glbimg.com/x720/6671490.jpg'
    IMAGE_FOLDER = "/Users/placerda/Desktop/img_files/"

    def __init__(self, img_url):
        self._img_url = img_url

    def is_valid_file(self):
        return self._img_url.endswith('.jpg')

    def download_file(self):
        try:
            files = os.listdir(ImageCollector.IMAGE_FOLDER)
            filename = 1 if len(files) == 0 else len(files)
            f = open(ImageCollector.IMAGE_FOLDER + "{0}.jpg".format(filename), 'wb')
            file_stream = request.urlopen(self._img_url).read()
            f.write(file_stream)
        except Exception as e:
            print(str(e))


if __name__ == '__main__':

    image_collector = ImageCollector(ImageCollector.example_img)

    for item in range(0, 10):
        image_collector.download_file()
