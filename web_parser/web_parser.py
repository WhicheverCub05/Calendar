import os
import random
from bs4 import BeautifulSoup as bs
from obj import engineer


def open_test_file():
    """Opens a test file stores locally
    """
    with open("test/test1.html") as file:
        soup = bs(file, 'html.parser')
    
    # print(soup.prettify())
    return soup


def open_file_from_path(path:str) -> bs:
    """Opens an html given a path and returns it as a bs4.BeautifulSoup object. Used for parsing

    Args:
        path (str): File path to the html file 

    Returns:
        bs: bs4.BeautifulSoup object from the html file
    """
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


def create_test_engineer_list(data:bs):
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


def create_engineer_list(data:bs):
    """ data (bs): Creates a list of engineers based off of the beautifulsoup data
    Args:
         
        bs4.BeautifulSoup Object which contains the webpage with the data
    Returns:
        list[Engineer]: List of engineers obtained from the web calendar
    """
    engineer_list = []

    calendar_container_class = 'sc-300e6012-0 kVaTLA'

    engineer_container_class = 'sc-8d378678-0 jGCHpv'

    engineer_li_id = '67df1661-a600-4601-878a-795459aeaf0c'


    start_time_box_class = 'sc-ad0a9d27-0 jeLybI'
    start_time_tag_class = 'sc-bkcml6-0 gcTrkp tako-component '

    engineer_calendar_container_class = 'sc-ef45b3be-1 dUHnUe'
    
    engineer_meta_container_class = 'sc-65d29e01-0 bOhfoX'
    engineer_name_contianer_class = 'sc-c7982388-1 fJzbCV'
    engineer_name_text_tag = 'h6'
    engineer_address_container_class = 'sc-c7982388-1 kLwNDD'
    engineer_address_text_tag = 'span' # 0

    engineer_schedule_container_class = 'sc-306u1c-0 kSNedy tako-component sc-6bd3894b-2 hYESoc'

    break_time_tag_class = 'sc-bkcml6-0 gcTrkp tako-component sc-c86dab9f-0 hZkeFu'

    job_container_class = 'sc-2e24d968-0 sYvUM'

    job_title_container_class = 'sc-5fe5ba4b-1 jgssQk'
    job_length_and_location_container_class = 'sc-5fe5ba4b-1 jgssQk'

    job_continer_text_class = 'sc-bkcml6-0 gcTrkp tako-component '

    job_id_container_class = 'sc-5fe5ba4b-1 hBFpsR'
    job_id_text_class = 'sc-bkcml6-0 gcTrkp tako-component '

    calander_container = data.select(f'.{calendar_container_class}')

    engineer_container_list = calander_container.select('li') 

    for engineer_row in engineer_container_list:
        
        engineer_meta_container = engineer_row.select(f'.{engineer_meta_container_class}')[0]
        name = engineer_meta_container.select(f'.{engineer_name_contianer_class}')[0].select(engineer_name_text_tag)[0]
        address = engineer_meta_container.select(f'.{engineer_address_container_class}')[0].select(engineer_address_text_tag)[0]

        tmp_engineer = engineer.Engineer(full_name=name, address=address)

        engineer_schedule_container = bs.soup.select(f'.{engineer_schedule_container_class}')
        engineer_jobs_containter_list = engineer_schedule_container.select(f'{job_container_class}')

        job_counter = len(engineer_jobs_containter_list)
        print(f'Engineer: {name} has {job_counter} jobs')
        for job_container in engineer_jobs_containter_list:
            pass

        engineer_list.append(tmp_engineer)

    return engineer_list


def create_jobs(data):
    pass


def create_schedule(data):
    pass