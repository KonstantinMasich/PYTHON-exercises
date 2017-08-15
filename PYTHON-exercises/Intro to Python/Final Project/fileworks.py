import csv

def write_to_file(f, data):
    """
    Overwrites data into specified file.
    Returns True if write attempt was successful, False otherwise.
    """
    try:
        with open(f, 'a') as out:
            out.seek(0)
            out.truncate()
            out.write(data)
        out.close()    
        return True
    except Exception as e:
        print(type(e), "\n", str(e))
        return False    
    

def read_csv(filepath, filetype):
    """
    Opens a csv file, reads its content and returns is as a list or a
    dictionary, depending on a specified filetype.
    """
    if filetype == "Grades":
        try:
            with open(filepath, newline = '') as f:
                reader = csv.reader(f, delimiter=',')
                d = dict()
                for row in reader:
                    d.update([(row[0], row[1:])])  
                return d
        except FileNotFoundError:
            print("ERROR:", filetype, "file was not found @ location", filepath)
            return
    elif filetype == "Settings":
        try:
            with open(filepath, newline = '') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    return row # returns the first row as it should
        except FileNotFoundError:
            print("ERROR:", filetype, "file was not found @ location", filepath)
            return
    else:
        return
    return
    
def print_grades(filepath):
    "Prints students' grades from a specified csv file"
    try:
        with open(filepath, newline = '') as csvfile:
            print("================================\nSTUDENTS GRADES TABLE:")
            print("================================")
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                print(row[0], row[1], ":", ', '.join(row[2:-1]), \
                "  Project:",row[-1])
            print("================================")
    except FileNotFoundError:
        print("ERROR:", filetype, "file was not found at location", filepath)
    return
