import tls_client
from tls_client.response import Response


def get_data(url: str):
    session = tls_client.Session(
         random_tls_extension_order=True
    )

    resp: Response = session.get(url, headers = {
    "Accept-Encoding": "deflate, br",
})


    if resp.status_code != 200:
        raise Exception(f"Failed to get data from {url}. Status code: {resp.status_code}")

    return resp.content.decode('utf-8')

def check_for_string(data: str, string: str):
    return string in data
