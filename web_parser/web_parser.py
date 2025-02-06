import os
import random
from bs4 import BeautifulSoup as bs
from obj import engineer
from obj import job


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
    
    engineer_meta_container_class = 'sc-65d29e01-0 bOhfoX'
    engineer_name_contianer_class = 'sc-c7982388-1 fJzbCV'
    engineer_name_text_tag = 'h6'
    engineer_address_container_class = 'sc-c7982388-1 kLwNDD'
    engineer_address_text_tag = 'span' # 0

    calander_container = data.find("div", class_=calendar_container_class)

    engineer_container_list = calander_container.find_all("li", class_='sc-294f72b7-0 hUAXfA') 

    for engineer_row in engineer_container_list:
        
        engineer_meta_container = engineer_row.select_one("div", class_=engineer_meta_container_class)
        name = engineer_meta_container.select_one("div", class_=engineer_name_contianer_class).select_one(engineer_name_text_tag).text
        address = engineer_meta_container.select_one("div", class_=engineer_address_container_class).select_one(engineer_address_text_tag).text

        tmp_engineer = engineer.Engineer(full_name=name, address=address)

        engineer_schedule_container = engineer_row.find("div", class_="sc-ef45b3be-1 dUHnUe")
        
        # print(engineer_schedule_container.prettify())

        engineer_jobs_containter_list = engineer_schedule_container.select('[class="sc-2e24d968-0 sYvUM"]')

        job_counter = 0

        if engineer_jobs_containter_list == []:
            continue

        for job_container in engineer_jobs_containter_list:
            
            if job_container.select_one("p", class_="sc-bkcml6-0 aqmIf tako-component ") == None:
                continue
            
            job_details = job_container.select("p", class_="sc-bkcml6-0 gcTrkp tako-component ")

            tmp_job = job.Job()
            
            if len(job_details) >= 4:
                tmp_job.description = job_details[0].text
                tmp_job.duration = job_details[1].text
                tmp_job.location = job_details[2].text
                tmp_job.id = job_details[3].text

                tmp_engineer.add_job(tmp_job)
                job_counter += 1

        print(f'Engineer: {name} has {job_counter} jobs')

        engineer_list.append(tmp_engineer)

    return engineer_list


def create_jobs(data):
    pass


def create_schedule(data):
    pass