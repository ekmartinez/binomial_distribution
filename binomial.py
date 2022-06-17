import pandas as pd
from scipy.stats import binom
import matplotlib.pyplot as plt
import openpyxl as xl
from openpyxl import load_workbook

class distribution:
    ''''Displays the binomial probability distribution'''
    def __init__(self, tests, prb):
        self.tests = tests + 1
        self.prb = prb

    def Binomial(self):
        #Data Frame.
        lst = []
        for x in range(self.tests):
            lst.append(x)
            
        df = pd.DataFrame(lst, columns = ['Tests'])
        df['Binomial'] = binom.pmf(df['Tests'], self.tests, self.prb)
        pd.options.display.float_format = '{:.8f}'.format
        df.set_index('Tests', inplace = True)
        print(df)

        #Matplotlib Barchart
        plt.bar(df.index, df['Binomial'], color='slategray')
        plt.title('Binomial Probability Mass Function')
        plt.ylabel('Probability')
        plt.legend(loc = 'best')
        plt.savefig('pmf.png', dpi=100)
        plt.show()
        
        #Export to Excel.
        fname = 'Binomial_distribution.xlsx'
        df.to_excel(fname)
        wb = load_workbook(fname)
        ws = wb.active
        img = xl.drawing.image.Image('pmf.png')
        img.anchor = 'E2'
        ws.add_image(img)
        wb.save(fname) 