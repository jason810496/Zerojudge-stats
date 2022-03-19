

class ZJ:
    # Raw html , Stats:dic ,cookie:str , last_connect:{stats code ,time } ,div:bs4 obj

    Stats = {}
    Cookie = "Current logged in Zerojudge account cookieID"
    user_id ="122857"
    def __init__(self ,stats ,cookie ):
        self.Stats = stats
        self.Cookie = cookie
    
    @classmethod
    def Update_Cookie( self,cookie):
        self.Cookie = cookie

    @classmethod
    def Is_Connect(self):
        import requests as req
        H = { "cookie":f"JSESSIONID={self.Cookie}" }
        r=req.get(f"https://zerojudge.tw/UserStatistic?id=122578",headers=H, timeout=20)
        
        if r.history: # not conect
            return False
        return True

    @classmethod
    def Get_Data(self):
        import requests as req
        from bs4 import BeautifulSoup as bs
        import re
        H = { "cookie":f"JSESSIONID={self.Cookie}" }
        r=req.get(f"https://zerojudge.tw/UserStatistic?id={self.user_id}",headers=H, timeout=20)
        Raw = r.text
        soup  = bs( Raw, "html.parser")
        
        if not r.headers.get('Content-Language') :
            self.Stats={}
            return 

        div = soup.find(text=re.compile('AC')).parent
        
        Str = div.getText()
        idx = Str.find("%")

        total = ""

        while Str[idx]!='(':
            total+=Str[idx]
            idx-=1

        total=total[::-1] #reverse string
        total=re.sub("[^0-9]", "",total)
        self.Stats["Total"]=total

        temp = div.findChildren()
        temp_list = [x.getText() for x in temp]

        if temp_list:
            self.Stats["AC"] = temp_list[0]
            self.Stats["WA"] = temp_list[2]
            self.Stats["TLE"] = temp_list[4]


    @classmethod
    def query(self,usr):
        self.user_id = usr

        self.Get_Data()

        return self.Stats

