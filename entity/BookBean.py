


class BookBean :


    def __init__(self):
        self.__id = None
        self.__booktitle = None
        self.__autorname = None


    def set_id(self,id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_booktitle(self,booktitle):
        self.__booktitle = booktitle

    def get_booktitle(self):
        return self.__booktitle

    def set_authorname(self,autorname):
        self.__autorname = autorname

    def get_authorname(self):
        return self.__autorname