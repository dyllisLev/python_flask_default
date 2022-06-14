# file name : index.py
# pwd : /project_name/app/main/index.py
 
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
# 추가할 모듈이 있다면 추가
 
main= Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def root():
    testData= 'root'
 
    return render_template('/main/index.html', testDataHtml=testData)

@main.route('/main', methods=['GET'])
def index():
    testData= 'testData array'
 
    return render_template('/main/index.html', testDataHtml=testData)