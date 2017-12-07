class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
    	# for (var i = 0; i < args.length; i++)
        for i in args:
            if type(i) == list: #or type(i) == tuple:
                for k in i:
                    self.result += k
            # else:
            #     self.result += i
        # print self.result
        return self


md = MathDojo()
print md.add([2,3,3]).result



# add(2).