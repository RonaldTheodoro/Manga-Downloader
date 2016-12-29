from tqdm import tqdm


def create_status_bar_iterable(response):
    name_file = response.url.split('/')[-1]
    return tqdm(response.iter_content(chunk_size=1024), desc=name_file)
