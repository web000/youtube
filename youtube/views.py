from logging.config import valid_ident
from django.shortcuts import render
from pytube import Playlist
from pathlib import Path
import os 


# Create your views here.


def playlist_input(request):
    result = ''
    downloads_path = str(Path.home() / "Downloads")

    if request.method  == 'POST':
        
 
        play_list_url = request.POST['link']
        playlist_number = request.POST['number']

        try:
            p = Playlist(play_list_url)
            print(f'Downloading: {p.title}')
            # print('video size *****  : ', p.filesize)
            # print(type(p), '*****************', p, len(p))
            # print('\n')
            # print(type(p.videos), '*****************', p.videos)
            # print(playlist_number, type(playlist_number))
            if playlist_number != '' and playlist_number.isdigit():
            # p = Playlist('https://www.youtube.com/watch?v=hEgO047GxaQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=1&t=0s')
     
                video_number = 1 
                for video in p.videos:
                    if video_number >= int(playlist_number):
                        title = video.title
                        print('Download  Start  : ', title)
                        st = video.streams.get_highest_resolution()
                        print('video size : ', st.filesize//1024**2, 'MB')
                        st.download(output_path=os.path.join(downloads_path, 'YoutubeVideos') )
                        print('Downloaded Video : ', title )
                        result = 'Playlist download successfully' 
                    video_number += 1     
            elif playlist_number == '' :
                for video in p.videos:
                        title = video.title
                        # print('channel name ****************** : ', video.channel_name)
                        print('Download  Start  : ', title)
                        st = video.streams.get_highest_resolution()
                        print('video size : ', st.filesize//1024**2, 'MB')
                        st.download(output_path=os.path.join(downloads_path, 'YoutubeVideos') )
                        print('Downloaded Video : ', title )  
                        result = 'Playlist download successfully' 
            else: 
                result = 'Enter valid input'                       
        except:        
    
            result = 'Enter Valid URL'

    return render(request, 'youtube/index.html', {'result': result})