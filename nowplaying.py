#coding: utf-8
import appscript as apps
import requests

itunes = apps.app('iTunes')
url = 'https://timeline.line.me/api/post/create.json'

headers = {
    'Host': 'timeline.line.me',
    'Connection': 'keep-alive',
    'Content-Length': '86',
    'Accept': '*/*',
    'X-Timeline-WebVersion': '1.2.1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36',
    'Origin': 'https://timeline.line.me',
    'Content-Type': 'application/json',
    'Referer': 'https://timeline.line.me/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ja,en-US;q=0.8,en;q=0.6',
    'Cookie': 'vc="HbgJ7el6ny4VyYrqSGzyNyKd+JJaZHhORrZfhm/yCmdiWOFpNKyCmOMeTcy9xjlvcevUHQBs38Dz5WhuRO51bhsbeYETUqz6XlhhV1CSxPj2mbIgm3UwiGHM7QNds6QbvDlqh7aPxIkfycO9ZnwPCg=="; _ga=GA1.2.526071454.1475310527; _gat=1; tc="euELlIpi1qDkE6y+qM4eQyqAXQnShGs0g2nzVd844HeWAQsFhiu/V0h4nkea7YtjETr70yAAFPu1Ocr7BMoakRgC3crxu6N+4GHvD0wcGki8Y7Kqoow/Yvx4Y20kHXFLyi4Ufop4Q0X4/J5apylfsg5Bbl8Vs+OUnD9vQkkXHUkC5RDQYlWjS9tuLpgwQucfqIQm+8gWbQvTb3QV+BOyZPArUFZ5MvkWycsaGZ3dASXrhbpYFWPko5ajAVCJld07RJw1iRMtbLlYNDPiPfa06x0thl8FWTfJeNlP/vX7PlTW8cBy5lJfvPB5jqLSUC32VFYRsy2XawVchcq4o2OWAMsGUuB21CaNU+gn9/GXQoExClKxSHO3W07DND9QtYkijnnMv3r310lm0PgYWahbh975KW68fFC4E14WZTR26kzICw2Bkz5tgB7X2Gy21AzMhGqsmdK8YKfngQm8Cnj4Kw=="; JSESSIONID=10E1A9345FECCBA83119B7E1A8A4FE02',#ブラウザから取得
}

params = {
    'sourceType': 'TIMELINE',
}

def getNowplaying():

    it = itunes.current_track

    song    = it.name.get()
    album   = it.album.get()
    artist  = it.artist.get()

    return (song,album,artist)

def postNowplaying(now):

    result = "#Nowplaying %s - %s by %s" % (now[0],now[1],now[2])
    print result
    json = {
        'contents': {u'text': result},
        'postInfo': {u'readPermission': {u'type': u'ALL', u'gids': None}},
    }

    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        params=params,
        json=json,
    )

    return True

if __name__ == "__main__":
    print postNowplaying(getNowplaying())
