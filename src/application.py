from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import requests, sys, json, random, base64

application = Flask(__name__)

@application.route('/grade', methods=["POST"])
def grade():
    path = "workspace%2Fchatbot%2Fgradedistribution%2F"
    req = request.get_json()
    params = req['action']['detailParams']
    imageurl = ''
    
    if 'sys_number' in params.keys() and 'sys_number1' in params.keys() and 'coursename' in params.keys() and 'semester' in params.keys():
        if 'sys_number2' in params.keys() : 
            imageurl = params['coursename']['origin'].upper() +params['sys_number']['origin']+'-'+params['sys_number1']['origin']+'-'+params['semester']['origin'].lower()+'-'+params['sys_number2']['origin'] +'.png'
        else : 
            imageurl = params['coursename']['origin'].upper() +params['sys_number']['origin']+'-'+params['sys_number1']['origin']+'-'+params['semester']['origin'].lower() +'.png'

        print(imageurl)
        path += imageurl
        base64_encoded_path = base64.urlsafe_b64encode(path.encode()).decode()
        retImage = "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/"
        retImage += imageurl
        retImage += "?path="
        retImage += base64_encoded_path
        retImage += "&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=PvDMMqyOTDRZOCQzsttrBSDL60xXRqmb"
        print(retImage)
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleImage": {
                            "imageUrl": retImage,
                            "altText": "The file is either nonexistent or the format you entered is incorrect."
                        }
                    }
                ]
            }
        }
    else:
        response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "Your message format is incorrect. If more than one course is offered simultaneously in a single semester, you must also include the section number"
                        }
                    }
                ]
            }
        }        
    return jsonify(response)

@application.route('/menu', methods=["POST"])
def index():
    req = request.get_json()
    params = req['action']['detailParams']
    month = ""
    day = ""
    ret = ""
    ret2 = ""
    url = "https://housing.igc.or.kr/about/cafeteria_menu.do?c_date=2024-"
    if 'sys_date' not in params.keys() and 'sys_number' not in params.keys() and 'todaytomorrow' not in params.keys():
        ret2 = "학식 정보가 궁금하신 날짜를 함께 입력해주세요"
        
    elif 'sys_number' in params.keys():
        if 'sys_number1' in params.keys():
            month = params['sys_number']['origin']
            day = params['sys_number1']['origin']
            url = url + month +"-"+ day
        else : 
            mid = len(params['sys_number']['origin'])//2
            month = params['sys_number']['origin'][:mid]
            day = params['sys_number']['origin'][mid:]
            url = url + month +"-"+ day
    
    elif 'sys_date' in params.keys():
        if "월" in params['sys_date']['origin'] and "일" in params['sys_date']['origin'] : 
            index_of_month = params['sys_date']['origin'].find("월")
            date_str_with_space = params['sys_date']['origin'][:index_of_month+1] + " " + params['sys_date']['origin'][index_of_month+1:]
            
            parts = date_str_with_space.split()
            month = (parts[0].replace("월", ""))
            day = (parts[1].replace("일", ""))
            url = url + month +"-"+ day
        elif params['sys_date']['origin']=="오늘":
            today = date.today()
            today_string = today.strftime("%Y-%m-%d")
            today_part = today_string.split("-")
            month = today_part[1]
            day = today_part[2]
            url = url + month +"-"+ day
        elif params['sys_date']['origin']=="내일":
            today = date.today()
            tomorrow = today + timedelta(days=1)
            tomorrow_string = tomorrow.strftime("%Y-%m-%d")
            tomorrow_part = tomorrow_string.split("-")
            month = tomorrow_part[1]
            day = tomorrow_part[2]
            url = url + month +"-"+ day
        elif params['sys_date']['origin']=="어제":
            today = date.today()
            yesterday = today - timedelta(days=1)
            yesterday_string = yesterday.strftime("%Y-%m-%d")
            yesterday_part = yesterday_string.split("-")
            month = yesterday_part[1]
            day = yesterday_part[2]
            url = url + month +"-"+ day
        else : 
            ret2 = "날짜를 잘 못 입력하셨습니다"
    elif 'todaytomorrow' in params.keys():
        if params['todaytomorrow']['origin']=="today":
            today = date.today()
            today_string = today.strftime("%Y-%m-%d")
            today_part = today_string.split("-")
            month = today_part[1]
            day = today_part[2]
            url = url + month +"-"+ day
        elif params['todaytomorrow']['origin']=="tomorrow":
            today = date.today()
            tomorrow = today + timedelta(days=1)
            tomorrow_string = tomorrow.strftime("%Y-%m-%d")
            tomorrow_part = tomorrow_string.split("-")
            month = tomorrow_part[1]
            day = tomorrow_part[2]
            url = url + month +"-"+ day
        elif params['todaytomorrow']['origin']=="yesterday":
            today = date.today()
            yesterday = today - timedelta(days=1)
            yesterday_string = yesterday.strftime("%Y-%m-%d")
            yesterday_part = yesterday_string.split("-")
            month = yesterday_part[1]
            day = yesterday_part[2]
            url = url + month +"-"+ day
        else : 
            ret2 = "날짜를 잘 못 입력하셨습니다"
        
    if month != "": 
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    
        dl_elements = []
        list_wrap_divs = soup.find_all('div', class_='list_wrap')
    
        for list_wrap_div in list_wrap_divs:
            dl_elements += list_wrap_div.find_all('dl')
        dl_strings = []
        for dl in dl_elements:
            dt_dd_pairs = dl.find_all(['dt', 'dd'])
            dt_dd_strings = []
            for i in range(0, len(dt_dd_pairs), 2):
                dt_text = dt_dd_pairs[i].get_text(strip=True)
                dd_text = dt_dd_pairs[i+1].get_text(strip=True)
                dt_dd_strings.append(f'{dt_text}\n{dd_text}')
            dl_strings.append('\n\n'.join(dt_dd_strings))
        if not dl_strings:
            dl_strings.append("No Operation on " + month +" "+day)
        ret = '\n'.join(dl_strings)
    else:
        ret = ret2
        
    response = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": ret
                        }
                    }
                ]
            }
        }
    return jsonify(response)

@application.route("/webhook/", methods=["POST"])
def webhook():
    request_data = request.json
    call_back = requests.post(request_data['callback_url'], json={
        "version": "2.0", "template": { "outputs": [{
            "simpleText": {"text": request_data['result']['choices'][0]['message']['content']}
        }]}})
    print(call_back.status_code, call_back.json())
    return 'OK'
@application.route("/question", methods=["POST"])
def call_openai_api():
    user_request = request.json.get('userRequest', {})
    callback_url = user_request.get('callbackUrl')
    try:
        api = requests.post('https://api.asyncia.com/v1/api/request/', json={
            "apikey": "YOUR_PROJECT_API_KEY_HERE",
            "messages" :[{"role": "user", "content": user_request.get('utterance', '')}],
            "userdata": [["callback_url", callback_url]]},
            headers={"apikey":"YOUR_HEADER_API_KEY_HERE"}, timeout=2)
    except requests.exceptions.ReadTimeout:
        pass    
    return jsonify({
      "version" : "2.0",
      "useCallback" : True
    })

@application.route("/welcome2", methods=["POST"])
def welcome2block():
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "SUNY Korea Chatbot"
              },
              "items": [
                {
                  "title": "Course Description",
                  "description": "ex : CSE114, AMS161, PHY131",
                  "imageUrl": "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/CourseDescriptions.png?path=d29ya3NwYWNlJTJGY2hhdGJvdCUyRmljb24lMkZDb3Vyc2VEZXNjcmlwdGlvbnMucG5n&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=PvDMMqyOTDRZOCQzsttrBSDL60xXRqmb",
                  "action": "message",
                  "messageText": "Course Description",
                },
                {
                  "title": "Professor Information",
                  "description": "ex : Jihoon Ryoo, Arthur Lee",
                  "imageUrl": "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/info.jpg?path=d29ya3NwYWNlJTJGY2hhdGJvdCUyRmljb24lMkZpbmZvLmpwZw==&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=PvDMMqyOTDRZOCQzsttrBSDL60xXRqmb",
                  "action": "message",
                  "messageText": "Professor Information",
                },
                {
                  "title": "IGC Cafeteria Menu",
                  "description": "ex : 0522 menu, today's menu ,오늘 학식",
                  "imageUrl": "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/menu.png?path=d29ya3NwYWNlJTJGY2hhdGJvdCUyRmljb24lMkZtZW51LnBuZw==&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=PvDMMqyOTDRZOCQzsttrBSDL60xXRqmb",
                  "action": "message",
                  "messageText": "IGC Cafeteria Menu",
                },
                {
                  "title": "Grade Distribution",
                  "description": "ex : CSE114 2023 fall, ams161 2023 Spring, phy133 2023 Fall 91",
                  "imageUrl": "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/histogram.jpg?path=d29ya3NwYWNlJTJGY2hhdGJvdCUyRmljb24lMkZoaXN0b2dyYW0uanBn&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=PvDMMqyOTDRZOCQzsttrBSDL60xXRqmb",
                  "action": "message",
                  "messageText": "Grade Distribution",
                },
                {
                  "title": "Chat GPT",
                  "description": "Just ask it in the chat!",
                  "imageUrl": "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/chatgpt.png?path=d29ya3NwYWNlJTJGY2hhdGJvdCUyRmljb24lMkZjaGF0Z3B0LnBuZw==&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=PvDMMqyOTDRZOCQzsttrBSDL60xXRqmb",
                  "action": "message",
                  "messageText": "Chat GPT",
                }
              ],
              "buttons": [
                {
                  "label": "More features",
                  "action": "block",
                  "blockId": "664a39332b2f2f1765b01222"
                }
              ]
            }
          }
        ]
      }
    }
    return jsonify(response)

@application.route("/welcomeskill", methods=["POST"])
def welcomeskill():
    req = request.get_json()
    params = req['action']['detailParams']
    ret = ""
    
    if params['welcomeblock']['origin'] == "Course Description" :
        ret = "If you send a course name, the chatbot gives course name, course title, course credit, instructor,  course info,  course requirements, and course outcome.\n(ex : CSE114, AMS161, PHY131)"
    elif params['welcomeblock']['origin'] == "Professor Information" :
        ret = "If you send a message with the professor name, chatbot answers including 'name, office, phone number and email'\n(ex : Jihoon Ryoo, Arthur Lee)"
    elif params['welcomeblock']['origin'] == "IGC Cafeteria Menu" :
        ret = "You can enter the date with the word 'menu' or '학식', to find out the meal menu at the IGC cafeteria.\n(ex : 0522 menu, today's menu ,오늘 학식)\nor you can follow the link\nhttps://housing.igc.or.kr/about/cafeteria_menu.do"    
    elif params['welcomeblock']['origin'] == "Grade Distribution" :
        ret = "You can enter the course with number, with year, and semester to find out the distribution of grades received by the students who took the class at that semester.\n(ex : CSE114 2023 fall, ams161 2023 Spring, Phy131 2023 Fall)\nor you can follow this link\nhttps://www.stonybrook.edu/celt/teaching-resources/academic-assessment/course-evaluations.php"
    elif params['welcomeblock']['origin'] == "Chat GPT" :
        ret = "All other unexpected messages are automatically redirected to ChatGPT. So, if you want to ask something to ChatGPT, just ask it in the chat!\n(ex : Recommend me a good drama to watch on Nexflix)\nor you can follow this link\nhttps://chat.openai.com/"
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": ret
                    }
                }
            ]
        }
    }
    return jsonify(response)
@application.route("/morefeature", methods=["POST"])
def morefeature():
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "listCard": {
              "header": {
                "title": "SUNY Korea Chatbot"
              },
              "items": [
                {
                  "title": "IGC VR Tour",
                  "description": "Experience Incheon Global Campus in VR",
                  "imageUrl": "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/vrtour.jpg?path=d29ya3NwYWNlJTJGY2hhdGJvdCUyRmljb24lMkZ2cnRvdXIuanBn&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=PvDMMqyOTDRZOCQzsttrBSDL60xXRqmb",
                  "link": {
                    "web": "https://www.igc.or.kr/vr/indexe.html"
                  }
                },
                {
                  "title": "Degree Work",
                  "description": "",
                  "imageUrl": "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/degreework.jpg?path=d29ya3NwYWNlJTJGY2hhdGJvdCUyRmljb24lMkZkZWdyZWV3b3JrLmpwZw==&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=PvDMMqyOTDRZOCQzsttrBSDL60xXRqmb",
                  "link": {
                    "web": "https://it.stonybrook.edu/services/degree-works"
                  }
                },
                {
                  "title": "Room Reservation",
                  "description": "Incheon Global Campus Library Seat Reservation System",
                  "imageUrl": "https://proxy.goorm.io/service/660a974df45fd80abdb557d6_d1PKsuFrqIDFCf5G8hV.run.goorm.io/9080/file/load/reservation.png?path=d29ya3NwYWNlJTJGY2hhdGJvdCUyRmljb24lMkZyZXNlcnZhdGlvbi5wbmc=&docker_id=d1PKsuFrqIDFCf5G8hV&secure_session_id=XRHB465PhL0bYpp89e6I3lehUbkNFq7d",
                  "link": {
                    "web": "https://seat.igc.or.kr/"
                  }
                }
              ],
              "buttons": [
                {
                  "label": "More features",
                  "action": "block",
                  "blockId": "62654c249ac8ed78441532de",
                  "extra": {
                    "key1": "value1",
                    "key2": "value2"
                  }
                }
              ]
            }
          }
        ]
      }
    }
    return jsonify(response)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)