from subprocess import call

class CallPythonObj():
    def __init__(self, path = 'Regex/Introduction.py'):
        path = self.path

    def call_into(self):
        call(['python3','{}'.format(self.path)])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    callobj = CallPythonObj()
    callobj.call_into()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
