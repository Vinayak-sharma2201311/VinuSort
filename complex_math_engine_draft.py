class cme:
    def reverse_array_write(array):
        ta = []
        for n in range((int(len(array)) * -1 + 1), 1):
            ta.append(int(array[-n]))

        for f in range(int(len(array))):
            array[f]=ta[f]    

    def reverse_array_print(array):
        ta = []
        for n in range((int(len(array)) * -1 + 1), 1):
            ta.append(int(array[-n]))
            
        print(ta)

    def reverse_array(array):
        ta = []
        for n in range((int(len(array)) * -1 + 1), 1):
            ta.append(int(array[-n]))
            
        return ta