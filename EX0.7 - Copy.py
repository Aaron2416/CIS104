s_score = input('Enter score: ')
try:
    def computegrade():
        if float(s_score) >= 0.9:
            print ('A')
        elif float(s_score) >= 0.8:
             print ('B')
        elif float(s_score) >= 0.7:
            print ('C')
        elif float(s_score) >= 0.6:
            print ('D')
        else:
            print ('F')
    computegrade()
except:
    print('Numbers only')
