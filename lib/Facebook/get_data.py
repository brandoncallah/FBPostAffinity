import facebook


class FaceBook:

    def __init__(self, start_date, end_date):

        self.start_date = start_date
        self.end_date = end_date
        self.token = 'EAAET7crXWzMBAG94VswKsId39Cg0fKhop9O8W1OlwNQlZB5GIoihIqnAY3cR8rw6pebaJMrv49mZAPZCZCbP16CZANPN7ZAhKHcFR6Di9HyGZBWYxCZBr6IwQEk7hDZCuQXCF8g6i5UAEOlzhjQyxf0okqrCLf4Bgyicu3CkhUOeM7iZC8cTRYMDGI1vVAew5tklP7on2s0XtiPFMRzUBgvUB6BkqEeLMOtAcwMwTziJrfZCAIdni9xkztf'

        self.graph = facebook.GraphAPI(access_token=self.token, version="2.12")
        self.user_id = ''
        self.aggr_messages = []
        self.get_user_id()
        self.get_posts()

    def get_user_id(self):

        self.user_id = self.graph.get_object(id='me')
        self.user_id = self.user_id['id']

    def get_posts(self):

        posts = self.graph.get_object(id=f"{self.user_id}/posts?since={self.start_date}&until={self.end_date}&limit=1000")
        self.aggr_messages = [x['message'] for x in posts['data'] if "message" in x.keys()]







