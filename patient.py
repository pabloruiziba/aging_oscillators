import os
import urllib

class Patient(object):

    #print(dict_ages['APOE-4-01'])

    def __init__(self, p_name=None):

        dict_ages = {
                    'APOE-3_01': 75.95,
                    'APOE-3_02': 50.88,
                    'APOE-3_03': 69.41,
                    'APOE-3_04': 67.51,
                    'APOE-3_05': 78.62,
                    'APOE-3_06': 65.49,
                    'APOE-3_07': 64.99,
                    'APOE-3_08': 53.95,
                    'APOE-3_09': 56.53,
                    'APOE-3_10': 67.00,
                    'APOE-3_11': 54.65,
                    'APOE-3_12': 66.52,
                    'APOE-3_13': 65.19,
                    'APOE-3_14': 73.07,
                    'APOE-3_15': 70.56,
                    'APOE-3_16': 61.82,
                    'APOE-3_17': 68.22,
                    'APOE-3_18': 45.96,
                    'APOE-3_19': 68.06,
                    'APOE-3_20': 69.75,
                    'APOE-3_21': 64.26,
                    'APOE-3_22': 78.73,
                    'APOE-3_23': 59.84,
                    'APOE-3_24': 53.97,
                    'APOE-3_25': 55.84,
                    'APOE-3_26': 65.14,
                    'APOE-3_27': 52.27,
                    'APOE-3_28': 56.67,
                    'APOE-3_29': 63.92,
                    'APOE-3_30': 69.43,
                    'APOE-4_01': 67.75,
                    'APOE-4_02': 62.11,
                    'APOE-4_03': 46.59,
                    'APOE-4_04': 72.08,
                    'APOE-4_05': 72.39,
                    'APOE-4_06': 45.83,
                    'APOE-4_07': 60.54,
                    'APOE-4_08': 68.41,
                    'APOE-4_09': 59.05,
                    'APOE-4_10': 61.75,
                    'APOE-4_11': 78.27,
                    'APOE-4_12': 65.94,
                    'APOE-4_13': 53.23,
                    'APOE-4_14': 59.41,
                    'APOE-4_15': 69.84,
                    'APOE-4_16': 42.80,
                    'APOE-4_17': 50.00,
                    'APOE-4_18': 67.33,
                    'APOE-4_19': 50.50,
                    'APOE-4_20': 70.86,
                    'APOE-4_21': 65.39,
                    'APOE-4_22': 61.33,
                    'APOE-4_23': 49.18,
                    'APOE-4_24': 68.27,
                    'APOE-4_25': 51.58
                    }

        if p_name is None:
            self.id = 'APOE-4_01'
        else:
            self.id = p_name

        try:
            self.age = dict_ages[self.id]
            #UCLA_CCN_APOE_DTI_APOE-4_1_connectmat.txt
            #printing patient info:
            
            if os.path.exists('data/'):
                print('dir data exists')
                if os.path.exists('data/connectivity/'):
                    print('subdir connectivity exists')
                    print('data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt')
                    if os.path.exists('data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt'):
                        print('connectivity file exists')
                    else:
                        #download patient file
                        file = urllib.URLopener()
                        file.retrieve('https://raw.githubusercontent.com/pabloruiziba/aging_oscillators/master/data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt',
                                      'data/connectivity/UCLA_CCN_APOE_DTI_'+self.id+'_connectmat.txt')

            print('##################################################')
            print('Id: '+self.id+', Age:'+str(self.age))        
            print('##################################################')


        except KeyError:
            print('##################################################')
            print('Patient id does not exist or was misspelled!!!')
            print('##################################################')
            quit()
#        except:
#            print('##################################################')
#            print('An error ocurred, program stopped')
#            print('##################################################')
#            quit()



        
Patient('APOE-4_03')
