filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt"]

for filename in filenames:
    filename = filename.replace('.', '_',1)
    print(filename)