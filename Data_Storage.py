import json 
from Musiclib import MusicLibrary

class DataStorage:
  @staticmethod
  def save(library,playlists):
    data = {
      "Music_Library": [],
      "Playlist" : []
      }
     
    with open ('MusicData.json','w') as file:
      json.dump(data,file)
      
  @staticmethod
  def load():
    try:
      with open ('MusicData.json','r') as file:
        data = json.load(file)
        Library = MusicLibrary()
        playlist = []

