import requests 
import json

url = 'https://randomuser.me/api/'


def get_version():
    '''get requests module'''
    return requests.__version__
    pass


def get_status_code(url: str) -> int:
    '''get status code of response
    
    Args:
        url (str): api url
    
    Returns:
        str: status code of response
    '''
    return requests.get(url).status_code
    
def get_content_type(url: str) -> str:
    '''get content type of response
    
    Args:
        url (str): api url
    
    Returns:
        str: content type of response
    '''
    return requests.get(url).content
    pass


def get_headers(url: str) -> dict:
    '''get headers of response
    
    Args:
        url (str): api url
    
    Returns:
        str: headers of response
    '''
    return requests.get(url).headers
    pass


def get_text(url: str) -> str:
    '''get text of response
    
    Args:
        url (str): api url
    
    Retusssrns:
        str: text of response
    '''
    return requests.get(url).text
    


def text_to_dict(text: str) -> dict:
    '''convert text to dict
    
    Args:
        text (str): text of response
    
    Returns:
        str: dict
    '''
    return json.loads(text)


def get_data(url: str) -> dict:
    '''get data of response. use method json()
    
    Args:
        url (str): api url
    
    Returns:
        dict: data
    '''
    return requests.get(url).json()
    pass

def get_user(url: str) -> dict:
    '''get user
    
    Args:
        url (str): api url
    
    Returns:
        dict: user
    '''
    return requests.get(url).json()["results"][0]
    pass

def get_users(url: str, n: int) -> list:
    '''get user
    
    Args:
        url (str): api url
        n (int): number of users
    
    Returns:
        list: list of users
    '''
    k=[]
    for i in range(n+1):
        k.append(requests.get(url).json()["results"][0])
    return k
    pass
print(get_status_code(url))
print(get_content_type(url))
print(get_headers(url))
print(get_text(url))
print(text_to_dict(get_text(url)))
print(get_data(url))
print(get_user(url))
print(get_users(url,10))