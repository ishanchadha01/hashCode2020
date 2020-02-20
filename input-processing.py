data = [
    "a_example.txt",
    "b-read_on.txt",
    "c_icunabula.txt",
    "d_tough_choices",
    "e_so_many_books",
    "f_libraries_of_the_world"
]

def createLibrary(file):
    with open(file, "r") as f:
        line = f.readline().split(" ")
        numbooks = int(line[0])
        numlibs = int(line[1])
        days = int(line[2])
        line = f.readline().split(" ")
        booklist = []
        for i in range(numbooks):
            booklist.append(int(line[i]))
        liblist = []
        signuplist = []
        for i in range(numlibs):
            line = f.readline().split(" ")
            numbooks = int(line[0])
            signup = int(line[1])
            rate = int(line[2])
            signuplist.append(signup)
            libbooks = []
            line = f.readline().split(" ")
            for j in range(numbooks):
                libbooks.append(int(line[j]))
            liblist.append(libbooks)
        return(booklist, signuplist, liblist)

