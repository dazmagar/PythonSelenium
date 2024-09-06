from pythonselenium import MasterQA

MasterQA.main(__name__, __file__)


class MasterQATests(MasterQA):
    def test_masterqa(self):
        self.open("https://xkcd.com/1700/")
        self.verify("Do you see a webcomic?")

        self.open("https://www.saucedemo.com/")
        self.highlight("//div[@class='form_group'][1]")
        self.verify("Do you see Username input?")
        self.highlight("input[id='login-button']")
        self.verify("Do you see Login button?")
