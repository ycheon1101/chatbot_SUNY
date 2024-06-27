# sudo service mysql restart

from flask import Flask, jsonify, request
import sys
import pymysql
import pdb
application = Flask(__name__)
import random

db = pymysql.connect(host='Your ip address', port=52774, user='cse416', password='Your Password', db='cse416', charset='utf8mb4')
cursor = db.cursor()
sql_select = 'select * from tb_prof'
cursor.execute(sql_select)
result= cursor.fetchall()
# pdb.set_trace()

cursor_course = db.cursor()
sql_select_course = 'select * from tb_course'
# pdb.set_trace()
cursor_course.execute(sql_select_course)
result_course = cursor_course.fetchall()


@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/random", methods=["POST"])
def random_function():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": str(random.randint(1, 10))
                    }
                }
            ]
        }
    }
    return jsonify(response)

# prof
@application.route("/professors", methods=["POST"])
def professors():
    cursor.execute(sql_select)  
    professors = cursor.fetchall()
    
    # prof_list = [{"id": prof[0], "name": prof[1], "room": prof[2], "phone": prof[3], "email": prof[4]} for prof in professors]
    # return jsonify(prof_list)
    req = request.get_json()
    # pdb.set_trace()
    params = req['action']['detailParams']
    utterance = str(req['userRequest']['utterance'])
    info = ''
    # pdb.set_trace()
    temp = []
    for prof in professors:
        if utterance in prof[-1]:
            info = prof
            break
    #     temp.append(str(prof[1]).lower())
    for prof in professors:
        if utterance in prof[1]:
            info = prof
            break
        
            
    # if utterance in str(temp):
    #     info = '1'
            
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": str('name: '+ info[1] + '\n' + 'office: ' + info[2] + '\n' + 'phone number: ' + info[3] + '\n' + 'email: ' + info[4])
                        # "text": str(info)
                    }
                }
            ]
        }
    }
    return jsonify(response)

# course
@application.route("/courses", methods=["POST"])
def course():
    cursor_course.execute(sql_select_course)
    courses = cursor_course.fetchall()
    
    req = request.get_json()
    # pdb.set_trace()
    # pdb.set_trace()
    params = req['action']['detailParams']
    # params = req
    utterance = str(req['userRequest']['utterance'])
    info = ''
    for course in courses:
        if utterance == course[1]:
            info = course
            break
    for course in courses:
        if utterance in course[-1]:
            info = course
            break
            
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": str('Course name: '+ info[1] + \
                                    '\n\n' + 'Course title: ' + info[2] + \
                                    '\n\n' + 'Course credit: ' + info[3] + \
                                    '\n\n' + 'Instructor: ' + info[4] + \
                                    '\n\n' + 'Course Info: ' + info[5] + \
                                    '\n\n' + 'Course requirement: ' + info[6] + \
                                    '\n\n' + 'Course outcome: ' + info[7] \
                                    
                                   )
                        # "text": str(info)
                    }
                }
            ]
        }
    }
    return jsonify(response)
    # return '1'

        
    


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
