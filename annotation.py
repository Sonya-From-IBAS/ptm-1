import os
import csv


def create_csv_annotation(class_name: str , annotation_name: str) -> None:
    """This function create csv annotation with 3 parameters: absolute path to file, relative path and file's class name"""
    path_to_class = os.path.join('dataset', class_name)
    class_names = os.listdir(path_to_class)
    with open(annotation_name, mode="w", encoding="UTF-16", newline='') as file:
        file_writer = csv.writer(file , delimiter=",")
        for name in class_names:
            file_writer.writerow(
                [os.path.abspath(name) , os.path.join(path_to_class , name), class_name])


def scv_annotation_executer(class_name: str, annotation_name: str) -> None:
    """ This function call previous to run it in main"""
    create_csv_annotation(class_name, annotation_name)
