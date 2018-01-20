from flask import Flask, Blueprint
from flask_restplus import Api, Resource,fields
from decouple import config
import json
import requests
app = Flask(__name__)
api = Api(app, version='1.0', title='ATT Open Issues API',
    description="Returns att open issues from public repositories owned by Att organization",
)
#blueprint = Blueprint('api',__name__,url_prefix='/api')
#api = Api(blueprint,doc='/documentation')#app)
#app.register_blueprint(blueprint)
#att_model = api.model('AttOpenIssues',{'id':fields.Integer('ID')})
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')

@api.route('/att-open-issues')
#@api.doc(params={'id': 'An ID'})
class AttOpenIssues(Resource):
    """Returns att open issues 
	from public repositories owned by Att organization. 
	Each issue object also contains comments data if exists for that issue 
    Attributes:CLIENT_ID and CLIENT_SECRET: Required for large rate limit
    """
    
    
    def get_modified_list(self,obj):
    	#returns updated open issues list with comments if exists
    	#Parameters: Obj- list all att open issues from public repos
        for each_obj in obj:
            if each_obj['comments']:
                rate_limit = '?client_id='+CLIENT_ID+'&client_secret='+CLIENT_SECRET
                each_obj["comments_data"] = \
                json.loads(requests.get(each_obj["comments_url"]+rate_limit).text)
        return obj

    def get(self):
        """
           Returns list of all open issues for all public repositories owned 
           by the "att" organization. Each issue object also contain a 
           list of comments if any exists
        """
        try:
        	#request to get att public repositories
        	att_repos_obj = requests.get(
        	"https://api.github.com/orgs/att/repos?client_id="+CLIENT_ID+"&client_secret="+CLIENT_SECRET)
        except TypeError:
        	#Exceptional handling for exceded rate limit
        	return JsonResponse("Rate Limit Exceded.")
        #Att Repos Data extraction from response object att_repos_obj 
        att_repos_dict_objs = json.loads(att_repos_obj.text)
        repo_names = [reponame['name'] for reponame in att_repos_dict_objs]
        att_open_issues_list=[]
        for repo_name in repo_names:
            url = "https://api.github.com/repos/att/"+repo_name+"/issues?state=open&client_id="+CLIENT_ID+"&client_secret="+CLIENT_SECRET
            att_repo_response = requests.get(url)
            #convert the request object to python native 
            #data type object list
            att_repo_list_of_dict_objs = json.loads(
            	att_repo_response.text)
            #extends the issues list for each iteration
            att_open_issues_list.extend(
            	att_repo_list_of_dict_objs)
        att_open_issues_list = self.get_modified_list(
        	att_open_issues_list)
        # return JsonResponse(att_open_issues_list,safe=False)
        return att_open_issues_list

if __name__ == '__main__':
	app.run(debug=True)