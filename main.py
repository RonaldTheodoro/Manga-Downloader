import timeit
from download import download_file


def main():
    url = 'http://www.fileproject.com.br/pp/files/Mangas/pP_c{}.rar'

    for chapter in range(1, 100):
        download_file(url.format(str(chapter).zfill(3)))

if __name__ == '__main__':
    start_time = timeit.default_timer()
    main()
    end_time = timeit.default_timer()
    
    print("Execution time: {:.2f} seconds".format(end_time - start_time))
