import ffmpeg

host = '10.10.150.119'
rport = '554'
ruser = 'admin'
rpasswd = 'inf123456'
rtag = '/h264/ch2/main/av_stream'
rurl = 'rtsp://'  + ruser + ':'+ rpasswd + '@' + host + ':' + rport + rtag
print (rurl)

def main ():
    (
        ffmpeg
            .input(rurl)
            # 保存的文件名
            .hflip()
            .output('saved_rtsp.mp4')
            # 覆盖同名文件
            .overwrite_output()
            # 运行保存
            .run()
    )
    
if __name__ == '__main__':
    main()
