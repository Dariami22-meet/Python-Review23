def create_youtube_video(title, description):
	video= {"title":title, "description" :description, "likes":0, "dislikes":0, "comments":{}}
	return(video)
def like(video):
	if "likes" in video:
		video["likes"]+=1
	return video
def dislike(video):
	if "dislike" in video:
		video["dislike"]+=1
	return video
def add_comment(video, username, comment_text):
	video["comments"][username]=comment_text
	return video


test=create_youtube_video("hello", "world")
for x in range(495):
	test=like(test)
test= dislike(test)
test=add_comment(test, "daria", "slay")
print(test)








		





