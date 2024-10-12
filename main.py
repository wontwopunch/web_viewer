from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>대용량 파일 다운로드</h1>
        <p>여기에서 파일을 다운로드하세요: <a href="https://drive.google.com/drive/folders/18DlOEfa_A-i5157AAYsHt5Alf1gQ2Lba?usp=drive_link">파일 다운로드</a></p>
    '''

if __name__ == '__main__':
    app.run()
