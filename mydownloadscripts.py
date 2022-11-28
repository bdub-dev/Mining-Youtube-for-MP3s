# first, download locations
hd = 'cd /Volumes/THE\ SAFE'

hd_raw_samples = 'cd /Volumes/THE\ SAFE/youtube-dl/raw_samples'

hd_it_tutorials = 'cd /Volumes/THE\ SAFE/youtube-dl/it_tutorials'
hd_andre_navarro = 'cd /Volumes/THE\ SAFE/youtube-dl/raw_samples/andre_navarro_new'
hd_adventures = 'cd /Volumes/THE\ SAFE/youtube-dl/raw_samples/adventures_in_sound'
hd_yum_yam_ = ' cd /Volumes/THE\ SAFE/youtube-dl/raw_samples/yum_yam_'
hd_nicola = 'cd /Volumes/THE\ SAFE/youtube-dl/listening_albums/Nicola_Armellin'


# then choose youtubedl scripts
mp3 = ' youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" --embed-thumbnail --ignore-errors'
video_hq = ' youtube-dl --format "(bestvideo[vcodec=av01][height>=4320][fps>30]/bestvideo[vcodec=vp9.2][height>=4320][fps>30]/bestvideo[vcodec=vp9][height>=4320][fps>30]/bestvideo[vcodec=av01][height>=4320]/bestvideo[vcodec=vp9.2][height>=4320]/bestvideo[vcodec=vp9][height>=4320]/bestvideo[height>=4320]/bestvideo[vcodec=av01][height>=2880][fps>30]/bestvideo[vcodec=vp9.2][height>=2880][fps>30]/bestvideo[vcodec=vp9][height>=2880][fps>30]/bestvideo[vcodec=av01][height>=2880]/bestvideo[vcodec=vp9.2][height>=2880]/bestvideo[vcodec=vp9][height>=2880]/bestvideo[height>=2880]/bestvideo[vcodec=av01][height>=2160][fps>30]/bestvideo[vcodec=vp9.2][height>=2160][fps>30]/bestvideo[vcodec=vp9][height>=2160][fps>30]/bestvideo[vcodec=av01][height>=2160]/bestvideo[vcodec=vp9.2][height>=2160]/bestvideo[vcodec=vp9][height>=2160]/bestvideo[height>=2160]/bestvideo[vcodec=av01][height>=1440][fps>30]/bestvideo[vcodec=vp9.2][height>=1440][fps>30]/bestvideo[vcodec=vp9][height>=1440][fps>30]/bestvideo[vcodec=av01][height>=1440]/bestvideo[vcodec=vp9.2][height>=1440]/bestvideo[vcodec=vp9][height>=1440]/bestvideo[height>=1440]/bestvideo[vcodec=av01][height>=1080][fps>30]/bestvideo[vcodec=vp9.2][height>=1080][fps>30]/bestvideo[vcodec=vp9][height>=1080][fps>30]/bestvideo[vcodec=av01][height>=1080]/bestvideo[vcodec=vp9.2][height>=1080]/bestvideo[vcodec=vp9][height>=1080]/bestvideo[height>=1080]/bestvideo[vcodec=av01][height>=720][fps>30]/bestvideo[vcodec=vp9.2][height>=720][fps>30]/bestvideo[vcodec=vp9][height>=720][fps>30]/bestvideo[vcodec=av01][height>=720]/bestvideo[vcodec=vp9.2][height>=720]/bestvideo[vcodec=vp9][height>=720]/bestvideo[height>=720]/bestvideo)+(bestaudio[acodec=opus]/bestaudio)/best" --verbose --force-ipv4 --sleep-interval 5 --max-sleep-interval 30 --ignore-errors --no-continue --no-overwrites --download-archive archive.log --add-metadata --write-description --write-info-json --write-annotations --write-thumbnail --embed-thumbnail --all-subs --sub-format "srt" --embed-subs --output "%(uploader)s/%(uploader)s - %(upload_date)s - %(title)s/%(uploader)s - %(upload_date)s - %(title)s [%(id)s].%(ext)s" --merge-output-format "mkv" --dateafter "$(date +%Y)"0101 --batch-file "Source - Channels.txt"'
video = ' youtube-dl'
# french ghosty scripts
audio_playlist = ' youtube-dl --format "(bestaudio[acodec=opus]/bestaudio)/best" --verbose --force-ipv4 --sleep-interval 5 --max-sleep-interval 30 --ignore-errors --no-continue --no-overwrites --download-archive archive.log --add-metadata --write-description --write-info-json --write-annotations --write-thumbnail --embed-thumbnail --extract-audio --output "%(playlist)s - (%(uploader)s)/%(upload_date)s - %(title)s/%(upload_date)s - %(title)s [%(id)s].%(ext)s" --merge-output-format "mkv" --batch-file "Source - Playlists.txt"'


ghosty_channel = ' yt-dlp --format "(bestaudio[acodec^=opus]/bestaudio)/best" --verbose --force-ipv4 --sleep-requests 1 --sleep-interval 5 --max-sleep-interval 30 --ignore-errors --no-continue --no-overwrites --download-archive archive.log --add-metadata --write-description --write-info-json --write-annotations --write-thumbnail --embed-thumbnail --extract-audio --match-filter "!is_live & !live" --output "%(uploader)s/%(uploader)s - %(upload_date)s - %(title)s/%(uploader)s - %(upload_date)s - %(title)s [%(id)s].%(ext)s" --batch-file "Source - Channels.txt" 2>&1 | tee output.log'

# playlist i want to get. delete as you go
nullByte_wireshark = ' https://www.youtube.com/playlist?list=PL4zzNO1AFRUmWWKvnWI9qnpnUw4vb-E1-'
nullByte_device_sec = ' https://www.youtube.com/playlist?list=PL4zzNO1AFRUl0qgcS61Z0imQfiRAMxCt0'
nullbyte_music = ' https://www.youtube.com/playlist?list=PL4zzNO1AFRUmJEtuoC-OobT33Clyu_Sgb'

##################################
########frequent channels ########
##################################
andre_navarro_ii = ' https://www.youtube.com/channel/UCv5OAW45h67CJEY6kJLyisg'
adventures_sound = ' https://www.youtube.com/channel/UCAMuwfmjImYPY2Xq_PACrvQ'
yum_yam = ' https://www.youtube.com/channel/UCwdZe5YX1M31q5DNRxgHKFg'
nullbyte = ' https://www.youtube.com/channel/UCgTNupxATBfWmfehv21ym-g'
nicola_armellin= ' https://www.youtube.com/c/NicolaArmellin'
nicola_rare_tracks = ' https://www.youtube.com/playlist?list=PL4G14zsHQYcVSXfpqXqvKdoNPEauMzce2'

#########insert one time url############
channel = ' [insert channel here without brackets]'
playlist = ' [insert playlist here without brackets]'
single = ' [insert single here without brackets]'


# hot commands
navarro = (mp3 + andre_navarro_ii)
adventures = (mp3 + adventures_sound)
yumyam = (mp3 + yum_yam)
nullbyte = (video + nullbyte)
nullbyte_hacker_music = (mp3 + nullbyte_music)
nicola = (mp3 + nicola_armellin)
rare = (mp3 + nicola_rare_tracks)


print(adventures)

