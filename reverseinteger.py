def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string_x = str(x)[::-1]
        if '-' in string_x:     
            out = '-' + string_x.replace('-','')
        else:
            out = string_x
        integer_out = int(out)
        if integer_out > 2**31 or integer_out < (-2**31):
            return 0
        else:
            return integer_out