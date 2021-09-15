def question():
    url=input('url?')
    hour=input('hour?')
    minute=input('minute?')
    seconds=input('secs?')
    time_in_secs=int(hour)*3600+int(minute)*60+int(seconds)
    file_number=time_in_secs//10
    return file_number,url