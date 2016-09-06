# class A(object):
#     def go(self):
#         print "go A go!"
#
#     def stop(self):
#         print "stop A stop!"
#
#     def pause(self):
#         raise Exception("Not Implemented")
#
#
# class B(A):
#     def go(self):
#         super(B, self).go()
#         print "go B go"
#
#
# class C(A):
#     def go(self):
#         super(C, self).go()
#         print "go C go!"
#
#
# class D(B, C):
#     def go(self):
#         super(D, self).go()
#         print "go D go!"
#
#     def stop(self):
#         super(D, self).stop()
#         print "stop D stop!"
#
#     def pause(self):
#         print "wait D wait!"
#
#
# class E(B, C):
#     pass
#
#
# a = A()
# b = B()
# c = C()
# d = D()
# e = E()
#
# print a.go()
# print b.go()
# print c.go()
# print d.go()
# print e.go()
#


class Node(object):
    def __init__(self, sName):
        self._lChildren = []
        self.sName = sName

    def __repr__(self):
        return "<Node '{}'>".format(self.sName)

    def append(self, *args, **kwargs):
        self._lChildren.append(*args, **kwargs)

    def print_all_1(self):
        print self

        for oChild in self._lChildren:
            oChild.print_all_1()

    def print_all_2(self):
        def gen(o):
            pass
