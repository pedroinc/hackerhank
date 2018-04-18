import os
from urllib import request


class ImageCollector:

    example_img = 'https://s03.video.glbimg.com/x720/6671490.jpg'
    example_img_folder = 'https://s03.video.glbimg.com/x720/'
    IMAGE_FOLDER = "/Users/placerda/Desktop/img_files/"

    def __init__(self, img_url=None, img_folder=None):
        self._img_url_folder = img_folder
        self._img_url = img_url

    def is_valid_file(self):
        return self._img_url.endswith('.jpg')

    @staticmethod
    def get_file_number():
        return len(os.listdir(ImageCollector.IMAGE_FOLDER))

    def download_file(self):
        try:
            file_number = self.get_file_number()
            filename = 1 if file_number == 0 else file_number
            f = open(ImageCollector.IMAGE_FOLDER + "{0}.jpg".format(filename), 'wb')
            file_stream = request.urlopen(self._img_url).read()
            f.write(file_stream)
        except Exception as e:
            print(str(e))

    def download_file(self, number):
        try:
            file_number = self.get_file_number()
            filename = 1 if file_number == 0 else file_number
            f = open(ImageCollector.IMAGE_FOLDER + "{0}.jpg".format(filename), 'wb')
            print("{0}{1}.jpg".format(self._img_url_folder, number))
            file_stream = request.urlopen("{0}{1}.jpg".format(self._img_url_folder, number)).read()
            f.write(file_stream)
        except Exception as e:
            print("erro: {0}".format(e))


if __name__ == '__main__':

    image_collector = ImageCollector(img_folder=ImageCollector.example_img_folder)

    start_pos = 6671400
    end_pos = 6671500

    for i in range(start_pos, end_pos):
        image_collector.download_file(i)
