from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql

app=Flask(__name__)




@app.route('/')
def youtubehome():
    conn=sql.connect('videos.db')
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("Select * from videos_table")
    data=cur.fetchall()
    return render_template('youtubu.html',data=data)


@app.route('/play')
def youtubeplayed():
    return render_template('videoplayer.html')

@app.route('/add',methods=['POST','GET'])
def youtubeadd():
    if request.method =='POST':
        thumbnaildp = request.form['thumbnaildp']
        thumbnail = request.form['thumbnail']
        description =request.form['description']
        channel =request.form['channel']
        views =request.form['views']
        video  =request.form[' video ']
      
        conn = sql.connect('videos.db')
        conn.row_factory = sql.Row
        cur =conn.cursor()
        cur.execute('Insert into videos_table (THUMBNAILDP,THUMBNAIL,DESCRIPTION,CHANNEL,VIEWS,VIDEO) values(?,?,?,?,?)',(thumbnaildp,thumbnail,description,channel,views,video))
        conn.commit()
        return redirect(url_for('youtubehome'))
    return render_template('uplaod.html')

@app.route('/play/<id>')
def playfunc(id):
    conn =sql.connect('videos.db')
    conn.row_factory =sql.Row
    cur = conn.cursor()
    cur = cur.execute("Select * from videos_table where ID=? ",(id,))
    data_play  = cur.fetchone()
    return render_template('videoplayer.html',data_play=data_play)

if __name__=='__main__':
    app.run(debug=True)











