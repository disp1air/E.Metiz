import requests

# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code: ", r.status_code)

# Сохранение ответа API в переменной.
response_dict = r.json()
print('Total repositories: ', response_dict['total_count'])

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print('Repositories returned: ', len(repo_dicts))

#Анализ первого репозитория
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print('Name: ', repo_dict['name'])
print('Owner: ', repo_dict['owner']['login'])
print('Stars: ', repo_dict['stargazers_count'])
print('Repository: ', repo_dict['html_url'])
print('Description: ', repo_dict['description'])

for key in sorted(repo_dict.keys()):
    print(key)

# Обработка результатов.
print(response_dict.keys())