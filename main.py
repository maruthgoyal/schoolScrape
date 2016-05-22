import urllib2
from bs4 import BeautifulSoup

URL = 'http://cbseresults.nic.in/class12/cbse1216.asp?regno=%s&schcode=%s&B1=Submit&FrontPage_Form1=true'

ENGLISH_FILE_PATH = 'english'
PHYSICS_FILE_PATH = 'phy'
CHEMISTRY_FILE_PATH = 'chem'
MATH_FILE_PATH = 'math'

SCHOOL_CODE = '08544'
MAX_ROLL_NO = 5859301
def main():

    regno = '5859001'

    while int(regno) < MAX_ROLL_NO:
        try:
            web = urllib2.urlopen(URL % (regno, SCHOOL_CODE))
            print web.read()
            if web.getcode() == 200:

                print "HOLLA"

                bs = BeautifulSoup(web.read(), 'html.parser')

                table = bs.find_all('table', bordercolor='#000000', recursive=True)[0]

                english_table = table.contents[1]
                physics_table = table.contents[2]
                chemistry_table = table.contents[3]
                math_table = table.contents[4]

                english_row = None
                physics_row = None
                chem_row = None
                math_row = None

                if english_table.contents[1] == 'ENGLISH CORE':
                    english_row = int(english_table.contents[2])

                if physics_table.contents[1] == 'PHYSICS':
                    physics_row = int(physics_table.contents[2])

                if chemistry_table.contents[1] == 'CHEMISTRY':
                    chem_row = int(chemistry_table.contents[2])

                if math_table.contents[1] == 'MATHEMATICS':
                    math_row = int(math_table.contents[2])

                if english_row:

                    with open(ENGLISH_FILE_PATH,'a') as f:
                        f.write(str(english_row))

                if physics_row:

                    with open(PHYSICS_FILE_PATH, 'a') as f:
                        f.write(str(physics_row))

                if chem_row:

                    with open(CHEMISTRY_FILE_PATH, 'a') as f:
                        f.write(str(chem_row))

                if math_row:

                    with open(MATH_FILE_PATH, 'a') as f:
                        f.write(str(math_row))

                print(english_row, math_row, physics_row, chem_row)

        except IndexError:
            print "NO RESULT"

        regno = str(int(regno) + 1).zfill(7)

if __name__ == '__main__':
    main()
