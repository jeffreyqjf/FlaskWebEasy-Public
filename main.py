from flask import Flask,request,render_template,redirect
import sqlite3
app = Flask(__name__)

data = sqlite3.connect('data.db')
cursor = data.cursor()
@app.route('/')
def index():
    return redirect('/load/210')
@app.route('/load/210',methods=["get","post"])
def load():#登录界面
    data = sqlite3.connect('data.db')
    cursor = data.cursor()

    if request.method == 'POST':
        name = request.args.get('name')#注销
        cursor.execute('''delete from loading where name="{0}"'''.format(name))
        data.commit()
        print('delete finish')
    cursor.close()
    data.close()
    return render_template('load.html')



@app.route('/load/210/judje',methods=["post"])
def judje():#判断登录并转跳界面
    data = sqlite3.connect('data.db')
    cursor = data.cursor()
    
    name = request.form.get('name')
    password = request.form.get('password')
    cursor.execute('select * from user where name="{0}"'.format(name))
    result = cursor.fetchall()
    if result:
        print(result)
        print(type(password))#str
        result = result[0]
        if result[0] and result[1] and name and password:

            if result[1] == int(password):#
                print(1)
                cursor.execute('select * from loading where name="{0}"'.format(name))
                repeat = cursor.fetchall()#是否登陆
                if not repeat:
                    cursor.execute('''insert into
                                    loading(name) values('{0}')'''.format(name))
                    data.commit()
            return render_template('user.html', user=result)
    cursor.close()
    data.close()
    return 'name or password error'




@app.route('/load/210/leaveword',methods=['get','post'])
def leaveword(): #留言版
    name = request.args.get('name')
    data = sqlite3.connect('data.db')
    cursor = data.cursor()

    cursor.execute('select * from loading')#判断是否登录
    result = cursor.fetchall()
    result_last = []
    for i in result:
        result_last.append(i[0])
        
    print(result_last)

    if name in result_last:
        cursor.execute("select*from leaveword")
        result_say = cursor.fetchall()
        print(result_say)
        if request.method == 'GET':
            pass
        else:
            box = request.form.get('box')
            cursor.execute('''insert into
            leaveword(name,value) values('{0}','{1}')'''.format(name,box))
            data.commit()
            cursor.close()
            data.close()
        print(request.method)
        return render_template('leaveword.html',name=name,result=result_say)
    else:
        cursor.close()
        data.close()

        return 'error'



if __name__ == '__main__':
    app.run(debug=True)
    
