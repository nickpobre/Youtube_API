from flask import Flask,request, jsonify, make_response
from pytube import YouTube
from flask_cors import CORS
from moviepy.editor import VideoFileClip, AudioFileClip
import os

app = Flask(__name__)
CORS(app, origins=["localhost:5000"])
url_base = "localhost:5000"

@app.route("/search")
def search():
  arg = request.args.get('link')
  yt = YouTube(arg)
  thumb = yt.thumbnail_url
  title = yt.title
  dw_link = url_base+"download?link="+arg
  resolution =[int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in yt.streams if i.resolution])))]
  resolution.sort()
  if request.environ.get("werkzeug.server.shutdown"):
    return jsonify({"server closed":"True"})
  else:
    return jsonify({'Thumbnail': thumb, 'Title': title, 'Download': dw_link, "Resolutions": resolution})

@app.route("/download")
def download():
  link = request.args.get("link")
  yt = YouTube(link)
  Res = request.args.get("res")
  yt = YouTube(link)
  v_name = "{}.webm".format(yt.title)
  a_name = "{}.mp3".format(yt.title)
  n_name = "{}.mp4".format(yt.title)
  yt.streams.filter(resolution=Res).first().download(filename=v_name)
  yt.streams.get_audio_only().download(filename=a_name)
  video_file = VideoFileClip(v_name)
  audio_file = AudioFileClip(a_name)
  video_file = video_file.set_audio(audio_file)
  video_file.write_videofile(n_name)
  audio_file.close()
  #retorna a função send que faz o envio do video
  return send(n_name),os.remove(v_name),os.remove(a_name)

def send(filename):
  if os.path.isfile(filename):
        # Lê o arquivo
      with open(filename, 'rb') as f:
          file_data = f.read()
      # Cria uma resposta Flask com o arquivo anexado
      response = make_response(file_data)
      response.headers["Content-Disposition"] = "attachment; filename=%s" % filename
      return response, os.remove(filename)
  else:
    # Enviar uma mensagem de erro se o arquivo não existir
    return 'Arquivo não encontrado', 404

app.run(debug=True)