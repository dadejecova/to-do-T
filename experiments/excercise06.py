filenames = ['doc.txt', 'report.txt', 'presentation.txt']
contents = ["Hello",
            "Hello",
            "Hello"]
for filename, content in zip(filenames, contents):
    file = open(f"{filename}", 'w')
    file.write(content)

"""
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(filename, 'w')
    file.write("Hello")
    file.close()
"""