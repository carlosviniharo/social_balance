import uuid
import socket
import requests
from django.contrib.postgres.search import SearchQuery, SearchVector


def get_mac_address():
    # Get the MAC address of the computer
    mac_address = ":".join(
        ["{:02x}".format((uuid.getnode() >> ele) & 0xFF) for ele in range(0, 48, 8)]
    )
    return mac_address


def get_public_ip_address():
    # Method 1: Use a public API to get the IP address
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        if response.status_code == 200:
            data = response.json()
            return data.get("ip")
    except requests.RequestException:
        pass

    # Method 2: Use a socket to connect to a remote server
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except socket.error:
        pass

    return None


def get_query(search_string, model):
    """
    This function search a specific string through the entire table/object
    using a SearchVector.
    :param search_string: str
    :param model: ORM object
    :return: query object
    """
    if search_string is not None:
        fields = [field.name for field in model._meta.fields]
        query = SearchQuery(search_string)
        vector = SearchVector(*fields)
        return model.objects.annotate(search=vector).filter(search=query)
    return model.objects.all()