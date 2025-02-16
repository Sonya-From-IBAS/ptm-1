import csv
import os

from typing import Optional


class IteratorTask1:
    def __init__(self) -> None:  
        self.__file_names = []
        self.__counter = 0
        self.__limit = 0
        self.__path = ""

    def __next__(self) -> Optional[str]:
        if self.__counter < self.__limit:
            self.__counter += 1
            return os.path.join(self.__path, self.__file_names[self.__counter-1])
        else:
            raise StopIteration

    def clear(self) -> None:
        self.__counter = 0

    def file_names_init(self) -> None:
        self.__file_names = os.listdir(self.__path)

    def path_init(self, path: str) -> None:
        self.__path = path

    def limit_init(self) -> None:
        self.__limit=len(self.__file_names)

    @property
    def path(self)->Optional[str]:
        return self.__path


class IteratorTask2:
    def __init__(self, class_name: str,  path: str) -> None:
        self.file_names = os.listdir(os.path.join(path))
        for name in self.file_names:
            if not class_name in name:
                self.file_names.remove(name)
        self.limit = len(self.file_names)
        self.counter = 0
        self.path = path

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration


class IteratorTask3:
    def __init__(self, class_name: str,  path: str, annotation_name: str) -> None:
        self.file_names = list()
        with open(os.path.join(path, annotation_name), encoding='UTF-16') as file:
            reader = csv.reader(file, delimiter=',')
            for file_info in reader:
                if file_info[1] == class_name:
                    self.file_names.append(file_info[0])

        self.limit = len(self.file_names)
        self.counter = 0
        self.path = path

    def __next__(self) -> str:
        if self.counter < self.limit:
            self.counter += 1
            return os.path.join(self.path, self.file_names[self.counter-1])
        else:
            raise StopIteration

