# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygal
import requests

#执行api调用并储存响应
# url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
# r = requests.get(url)
# print("Status code:",r.status_code)
#
# #将api响应储存在一个变量中
# response_dict = r.json()
#
# # #处理结果
# # print(response_dict.keys())
#
# print("Total repositories:" , response_dict['total_count'])

# #搜索有关仓库的信息
# repo_dicts = response_dict['items']
# print("Repositories returned: ",len(repo_dicts))
#
# #研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# import pygal as gal
# from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#
# repo_dicts = response_dict['items']
#
# names,starts = [],[]
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     starts.append(repo_dict['stargazers_count'])
#
# #可视化
# my_config = gal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False
# my_config.title_font_size = 24
#
#
# my_style = LS('#333366',base_style=LCS)
# chart = pygal.Bar(my_config,style = my_style)
# chart.title = 'Most-Starred Python Projects on GitHub'
# chart.x_labels = names
#
# chart.add('',starts)
# chart.render_to_file('python_repos.svg')

#最热门的的文章的api
import requests
from operator import itemgetter

#执行API并且保存响应
url = 'https://hacker-news.firebaseio.com/v0/item/9884165.json'
r = requests.get(url)
print("Status code: ",r.status_code)

#处理相关信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    #对于每个文章调用一个api
    url = 'https://hacker-news.firebaseio.com/v0/item/'+str(submission_id)+'.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    submission_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id='+str(submission_id),
        'comments':response_dict.get('descendants',0)
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),reverse=True)
for submission_dict in submission_dicts:
    print(submission_dict['title'])
    print(submission_dict['link'])
    print(submission_dict['comments'])

