from tornado.web import url
from handler.login_handler import LoginHandler, UserInfoHandler
from handler.near_song_handler import SongNearHandler
from handler.song_story_handler import SongStoryHandler
from handler.story_handler import StoryHandler, PraiseHandler
from handler.comment_handler import CommentHandler
from handler.search_handler import SearchHandler

routes = [
    url(r"/login", LoginHandler),
    #url(r"/song",SongNearHandler),
    url(r"/story", StoryHandler),
    url(r"/story/([0-9]+)/up", PraiseHandler),
    url(r"/story/([0-9]+)/comment", CommentHandler),
    url(r"/song/([0-9]+)/story", SongStoryHandler),
    url(r"/userinfo", UserInfoHandler),
    url(r"/song/near", SongNearHandler),
    url(r"/song/search", SearchHandler)
]
