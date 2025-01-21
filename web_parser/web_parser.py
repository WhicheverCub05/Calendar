import os
import random
from bs4 import BeautifulSoup as bs
from obj import engineer


def open_test_file():
    with open("test/test.html") as file:
        soup = bs(file, 'html.parser')
    
    print(soup.prettify())


def open_file_from_path(path:str) -> bs:
    try:
        with open(path) as file:
            soup = bs(file, 'html.parser')
            # print(soup.prettify())
            return soup

    except UnicodeDecodeError:
        print("file type unsupported")
    except Exception as e:
        print("couldn't open file. please close the file and make sure dicrecotry is accessable (yk, permissions and stuff)")
        print(f"Error msg: {e}")


def create_engineer_list(data:bs):
    engineer_list = []
    example_engineer_names = ["boog", "goop", "poog", "goob", "noob"]
    engineer_counter = 10 
    # parse the soup to populate engineer data
    # populate engineers:
    for i in range(engineer_counter):
        full_name = random.choices(population=example_engineer_names, k=2)
        full_name = ' '.join(full_name)
        tmp_engineer = engineer.Engineer(full_name=full_name, address=f"A..{i}")
        engineer_list.append(tmp_engineer)

    return engineer_list
    

def create_jobs(data):
    pass


def create_schedule(data):
    pass