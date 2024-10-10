from flask import Flask, request, jsonify
import os
import sys


sys.path.insert(1, os.path.join(sys.path[0], '..'))


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    res = {
        'img': 'url',
        'name': 'имя',
        'exp': 'опыт',
        'time': 'dd.mm.yyyy',
        'youtube': 'url',
        'inst': 'url',
        'vk': 'url',
        'cakes': [
            {
                'name': 'Название торта',
                'photo': 'url',
                'desc': 'Описание торт'
            },
            {
                'name': 'Название торта1',
                'photo': 'url1',
                'desc': 'Описание торт1'
            },
            {
                'name': 'Название торта2',
                'photo': 'url2',
                'desc': 'Описание торт2'
            },
            {
                'name': 'Название торта3',
                'photo': 'url3',
                'desc': 'Описание торт3'
            },
        ]
    }


    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)