import os

originalpath = '/Users/kelvi/Documents/Python V1'

end = []

def list_folder(path):
        for i in os.listdir(path):
            if os.path.isdir(os.path.join(path, i)):
                lol = [i[0] for i in list(os.walk(path))]
                if len(os.listdir(path)) != 2 and os.path.join(path, i) != lol[-1]:
                    print('\u2502  ' * (len(os.path.join(path, i).replace(originalpath, '').split('\\'))-2) + '\u251C' + '\u2500' * 2 + i)
                else:
                    print('\u2502  ' * (len(os.path.join(path, i).replace(originalpath, '').split('\\'))-2) + '\u2514' + '\u2500' * 2 + i)
                list_file(os.path.join(path, i))

def list_file(path, line):
        for i in os.listdir(path):
            if i != os.listdir(path)[-1]:
                print('\u2502  ' * line + '\u251C' + '\u2500' * 2 + i)
            else:
                print('\u2502  ' * line + '\u2514' + '\u2500' * 2 + i)
            if os.path.isdir(os.path.join(path, i)):
                list_file(os.path.join(path, i), (len(os.path.join(path, i).replace(originalpath, '').split('\\'))-2))

list_file(originalpath, 0)

input()
