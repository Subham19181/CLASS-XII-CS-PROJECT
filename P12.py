#Program 12

info = 'subham19181@gmail.com Sunday Dec 12 06:20:45 2024'
start = info.find('@') + 1
end = info.find(".com") +4
mailservice = info[start:end]

start = end + 1
end = len(info)
d_t = info[start:end]

print("The email has been sent through ", mailservice)
print("It was sent on ", d_t)