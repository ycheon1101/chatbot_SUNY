import pandas as pd
import sys
import pymysql

def db_save (field, datasets):
    sql_insert_courses="""insert into tb_course (course_name, course_fullname, course_credit, course_coordinator, course_info, course_prereq, course_outcome, course_requirement, course_sbc) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # Define sql_insert_prof here
    sql_insert_prof = """insert into tb_prof (prof_name, prof_office, prof_contact, prof_email) values (%s,%s,%s,%s)"""


#     if field == 'cse':
# "excel.py" [dos] 191L, 9374C                                                                    1,1           Top
# # !pip install pandas
# # !pip install pymysql

# # https://devpouch.tistory.com/196

import pandas as pd
import sys
import pymysql

def db_save (field, datasets):
    sql_insert_courses="""insert into tb_course (course_name, course_fullname, course_credit, course_coordinator, course_info, course_prereq, course_outcome, course_requirement, course_sbc) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # Define sql_insert_prof here
    sql_insert_prof = """insert into tb_prof (prof_name, prof_office, prof_contact, prof_email) values (%s,%s,%s,%s)"""


    if field == 'cse':
        for i in range(len(datasets[0])):
            course_elem = datasets[0].loc[i]
            cursor.execute(sql_insert_courses,
                           (
                                str(course_elem['course_name']).split('\n')[0],
                                str(course_elem['course_fullname']).split('\n')[0],
                                str(course_elem['course_credit']).split('\n')[0],
                                str(course_elem['course_coordinator']).split('\n')[0],
                                str(course_elem['course_info']).split('\n')[0],
                                str(course_elem['course_prereq']).split('\n')[0],
                                str(course_elem['course_outcome']).split('\n')[0],
                                str(course_elem['course_requirement']).split('\n')[0],
                                str(course_elem['course_sbc']).split('\n')[0]
                            ))
        print('### LOG : successfully added to the database!!!')


    elif field == 'ese':
        for i in range(len(datasets[1])):
            course_elem = datasets[1].loc[i]
            cursor.execute(sql_insert_courses,
                           (
                                str(course_elem['course_name']).split('\n')[0],
                                str(course_elem['course_fullname']).split('\n')[0],
                                str(course_elem['course_credit']).split('\n')[0],
                                str(course_elem['course_coordinator']).split('\n')[0],
                                str(course_elem['course_info']).split('\n')[0],
                                str(course_elem['course_prereq']).split('\n')[0],
                                str(course_elem['course_outcome']).split('\n')[0],
                                str(course_elem['course_requirement']).split('\n')[0],
                                str(course_elem['course_sbc']).split('\n')[0]
                            ))
        print('### LOG : successfully added to the database!!!')


    elif field == 'est':
        for i in range(len(datasets[2])):
            course_elem = datasets[2].loc[i]
            cursor.execute(sql_insert_courses,
                           (
                                str(course_elem['course_name']).split('\n')[0],
                                str(course_elem['course_fullname']).split('\n')[0],
                                str(course_elem['course_credit']).split('\n')[0],
                                str(course_elem['course_coordinator']).split('\n')[0],
                                str(course_elem['course_info']).split('\n')[0],
                                str(course_elem['course_prereq']).split('\n')[0],
                                str(course_elem['course_outcome']).split('\n')[0],
                                str(course_elem['course_requirement']).split('\n')[0],
                                str(course_elem['course_sbc']).split('\n')[0]
                            ))
        print('### LOG : successfully added to the database!!!')


    elif field == 'mec':
        for i in range(len(datasets[3])):
            course_elem = datasets[3].loc[i]
            cursor.execute(sql_insert_courses,
                           (
                                str(course_elem['course_name']).split('\n')[0],
                                str(course_elem['course_fullname']).split('\n')[0],
                                str(course_elem['course_credit']).split('\n')[0],
                                str(course_elem['course_coordinator']).split('\n')[0],
                                str(course_elem['course_info']).split('\n')[0],
                                str(course_elem['course_prereq']).split('\n')[0],
                                str(course_elem['course_outcome']).split('\n')[0],
                                str(course_elem['course_requirement']).split('\n')[0],
                                str(course_elem['course_sbc']).split('\n')[0]
                            ))
        print('### LOG : successfully added to the database!!!')


    elif field == 'bm':
        for i in range(len(datasets[4])):
            course_elem = datasets[4].loc[i]
            cursor.execute(sql_insert_courses,
                           (
                                str(course_elem['course_name']).split('\n')[0],
                                str(course_elem['course_fullname']).split('\n')[0],
                                str(course_elem['course_credit']).split('\n')[0],
                                str(course_elem['course_coordinator']).split('\n')[0],
                                str(course_elem['course_info']).split('\n')[0],
                                str(course_elem['course_prereq']).split('\n')[0],
                                str(course_elem['course_outcome']).split('\n')[0],
                                str(course_elem['course_requirement']).split('\n')[0],
                                str(course_elem['course_sbc']).split('\n')[0]
                            ))
        print('### LOG : successfully added to the database!!!')


    elif field == 'ams':
        for i in range(len(datasets[5])):
            course_elem = datasets[5].loc[i]
            cursor.execute(sql_insert_courses,
                           (
                                str(course_elem['course_name']).split('\n')[0],
                                str(course_elem['course_fullname']).split('\n')[0],
                                str(course_elem['course_credit']).split('\n')[0],
                                str(course_elem['course_coordinator']).split('\n')[0],
                                str(course_elem['course_info']).split('\n')[0],
                                str(course_elem['course_prereq']).split('\n')[0],
                                str(course_elem['course_outcome']).split('\n')[0],
                                str(course_elem['course_requirement']).split('\n')[0],
                                str(course_elem['course_sbc']).split('\n')[0]
                            ))
        print('### LOG : successfully added to the database!!!')


    elif field == 'prof':
        for i in range (len(datasets[6])):
            prof_elem = datasets[6].loc[i]
            cursor.execute(sql_insert_prof,
                        (str(prof_elem['prof_name']).split('\n')[0],
                            str(prof_elem['prof_office']).split('\n')[0],
                            str(prof_elem['prof_contact']).split('\n')[0],
                            str(prof_elem['prof_email']).split('\n')[0])
                        )
        print('### LOG : successfully added to the database!!')

if __name__ == "__main__":

    course_list = './courses.xlsx'
    prof_list = './professors.xlsx'

    df_CSE = pd.read_excel(course_list, sheet_name='CSE', engine='openpyxl')
    df_ESE = pd.read_excel(course_list, sheet_name='ESE', engine='openpyxl')
    df_EST = pd.read_excel(course_list, sheet_name='EST', engine='openpyxl')
    df_MEC = pd.read_excel(course_list, sheet_name='MEC', engine='openpyxl')
    df_BM = pd.read_excel(course_list, sheet_name='BM', engine='openpyxl')
    df_AMS = pd.read_excel(course_list, sheet_name='AMS', engine='openpyxl')
    df_prof = pd.read_excel(prof_list, engine='openpyxl')

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # set up connection
    # db = pymysql.connect(host='15.165.115.190:55108', user='root', password='1111', db='cse416', charset='utf8mb4')
    db = pymysql.connect(host='13.124.68.247', port=55488, user='cse416', password='1111', db='cse416', charset='utf8mb4')

    cursor = db.cursor()
    sql_select = 'select * from tb_courses'

    # result= cursor.fetchall() use this only select


    args = sys.argv
    if len(args) < 2 :
        sql_course="select * from tb_prof where course_name = 'cse114'"
        result_course = cursor.execute(sql_course)
        print('result_course : ', result_course)
        sql_prof="select * from tb_prof where prof_name = 'Jihoon Ryoo'"
        result_prof = cursor.execute(sql_prof)
        print('result_prof : ', result_prof)
        # db saves all

    elif len(args) == 2 :
        db_save(args[1], [df_CSE,df_ESE,df_EST,df_MEC,df_BM,df_AMS,df_prof])

    args = sys.argv
    if len(args) < 2 :
        sql_course="select * from tb_prof where course_name = 'cse114'"
        result_course = cursor.execute(sql_course)
        print('result_course : ', result_course)
        sql_prof="select * from tb_prof where prof_name = 'Jihoon Ryoo'"
        result_prof = cursor.execute(sql_prof)
        print('result_prof : ', result_prof)
        # db saves all

    elif len(args) == 2 :
        db_save(args[1], [df_CSE,df_ESE,df_EST,df_MEC,df_BM,df_AMS,df_prof])
        #cursor.execute('select * from tb_test;')
        #result = cursor.fetchall()
        #print(result)


    db.commit()
    db.close()



    #cursor.execute(sql)






    # print(df_CSE)
    # print(df_CSE['course_name'])
    # print(df_CSE[0:3])
