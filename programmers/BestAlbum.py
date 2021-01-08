def solution(genres, plays):
    length = len(plays)
    answer = []
    genre = dict(map(lambda x: (x, 0), genres))
    playlist = dict()
    for i in range(length):
        genre[genres[i]] += plays[i]
        playlist[genres[i] + ' ' + str(i)] = plays[i]

    genre = sorted(genre.items(), key=(lambda x: x[1]), reverse=True)
    playlist = sorted(playlist.items(), key=(lambda x: x[1]), reverse=True)

    for x, _ in genre:
        next = False
        for key, _ in playlist:
            print(key.split()[0])
            print(x)
            if key.split()[0] == x:
                answer.append(int(key.split()[1]))
                if next:
                    break
                else:
                    next = True

    return answer