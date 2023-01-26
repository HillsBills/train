import csv


# does none none work? do i need if? if it doesnt work then write fieldnames anyway.
def write_file(rows, address, fieldnames, mode='w'):
    """
    writes rows to a file, either appending or new write.
    @param rows: list
    @param address: str
    @param fieldnames: list
    @param mode: str
    """
    with open(address, mode, newline='') as w:
        writer = csv.DictWriter(w, fieldnames, extrasaction='ignore')
        if mode == 'w':
            writer.writeheader()
        writer.writerows(rows)


def get_reader(address):
    """
    creates a list of dictReader, or an empty list if the file doesnt exist.
    @param address: str
    @return: list dictReader
    """
    try:
        with open(address) as r:
            return list(csv.DictReader(r))
    except FileNotFoundError:
        # not sure i need this. yes in case its empty so no error appears
        return []
        # return


# print(get_reader('C:\\Users\\hillaky\\PycharmProjects\\pythonProject\\h'))
