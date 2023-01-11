from json import load
with open("./db.json","r") as f:
    data=load(f)
#print(data)
#print(len(data))
#*******print movies where genre is comedy

#movies=[movie.get("title") for movie in data if "Comedy" in movie.get("genres")]
#print(movies)

#********print movies released after 2000
#movies=[movie.get("title") for movie in data if int(movie.get("year"))>2000]
#print(movies)

#******max run time
run_time=max(data,key=lambda movie:int(movie.get("runtime")))
movie=run_time.get("title")
print(movie)