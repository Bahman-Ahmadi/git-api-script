from requests import post, get, put
from json           import dumps
from base64    import b64encode, b64decode
from rich           import print

class GIT:
	def __init__(self, token):
		self.token = token

	def createRepository(self, **kwargs):
		# name: <RepoName:str>, auto_init: <bool>, private: <bool>, gitignore_template: <TempName:str>
		return post("https://api.github.com/user/repos", json=kwargs, headers={"Authorization": f"token {self.token}"})

	def getFile(self, path):
		return get(f"https://api.github.com/repos/{path}", headers={"Authorization": f"token {self.token}"})

	def createFile(self, path, **kwargs):
		# message: <CommitTitle:str>, content: <b64enced:str>
		return put(f"https://api.github.com/repos/{path}", data=dumps(kwargs), headers={"Authorization": f"token {self.token}"})

rubikalib = GIT("<GIT-TOKEN>")
rubikalib.NAME = "<GIT-USERNAME>"
rubikalib.REPO  = "<REPO-NAME>"
rubikalib.FILE     = "<FILE-NAME>"

# updateFile: print (rubikalib.createFile(f"{rubikalib.NAME}/{rubikalib.REPO}/contents/{rubikalib.FILE}", message="TestCommit", committer=dict(name="rubikalib", email="rubikalib@gmail.com"), content=b64encode(open(rubikalib.FILE, "rb").read()).decode(), sha=rubikalib.getFile(f"{rubikalib.NAME}/{rubikalib.REPO}/contents/{rubikalib.FILE}").json().get("sha")).json())

