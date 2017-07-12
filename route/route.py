from tornado.web import url
from handler.login_handler import LoginHandler, UserInfoHandler
from handler.near_song_handler import SongNearHandler
from handler.song_story_handler import SongStoryHandler
from handler.comment_handler import CommentHandler

routes = [
        url(r"/login", LoginHandler),
        #url(r"/song",SongNearHandler),
		#url(r"/story", StoryHandler, name='story'),
		# url(r"/story/([0-9]+)/up", PraiseHandler, name='praisestory'),
        url(r"/story/([0-9]+)/comment", CommentHandler),
        url(r"/userinfo",UserInfoHandler),
        url(r"/song", SongNearHandler),
        url(r"/song/story", SongStoryHandler)
        ]
