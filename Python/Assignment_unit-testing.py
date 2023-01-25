#Assignment
'''
Q.) Test for list Methods
List Method - 
 - insert
 - extend
 - find
'''
'''
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.l = [1,2,3,4]
        self.m = [5,6,7,8]

    def test_insert(self):
        self.l.insert(2,2.5)
        self.assertEqual(self.l,[1,2,2.5,3,4], "Not inserted")

    def test_extend(self):
        self.l.extend(self.m)
        self.assertEqual(self.l, [1,2,3,4,5,6,7,8], "Not extended")

    def test_find(self):
        self.assertEqual(self.l.index(3), 2, "Didnt find")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/akshitkhamesra/Desktop/Training/Python/"))
'''
'''
Q.) Make a emp class and test for give_raise
'''
'''
import HtmlTestRunner
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid = eid
        self.ename = ename
        self.esal = esal
    def get_name(self):
        return self.ename
    def get_eid(self):
        return self.eid
    def get_esal(self):
        return self.esal
    def give_raise(self,percent):
        self.esal = int(self.esal+(self.esal * percent/100))
        
    
class TestMethods(unittest.TestCase):
    def setUp(self):
        self.emp = Emp("EO1","Akshit",30000)
    def test_give_raise(self):
        self.emp.give_raise(10)
        self.assertEqual(self.emp.esal,33000,"Error in give_raise")
        self.emp.give_raise(0)
        self.assertEqual(self.emp.esal, 33000, "Error while raising salary by 0")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/akshitkhamesra/Desktop/Training/Python/"))
    '''