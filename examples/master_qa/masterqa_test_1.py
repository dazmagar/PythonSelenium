from pythonselenium import MasterQA

MasterQA.main(__name__, __file__)


class MasterQATests(MasterQA):
    def test_xkcd(self):
        self.open("https://xkcd.com/1512/")
        for i in range(4):
            self.click('a[rel="next"]')
        for i in range(3):
            self.click('a[rel="prev"]')
        self.verify()
        self.open("https://xkcd.com/1520/")
        for i in range(2):
            self.click('a[rel="next"]')
        self.verify("Can you find the moon?")
        self.click('a[rel="next"]')
        self.verify("Do the drones look safe?")

        self.open("https://xkcd.com/213/")
        for i in range(5):
            self.click('a[rel="prev"]')
        self.verify("Does the page say 'Abnormal Expressions'?")
