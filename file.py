import operator
class File:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._content = []

    def read(self):
        self._content = []
        with open(self._file_path) as content:
            for line in content:
                self._content.append(line.strip())

    def write(self, addition: str):
        self._content.append(addition)
        f = open(self._file_path, "a")
        f.write(f"{addition}\n")
        f.close()


class News(File):
    def __init__(self, file_path: str):
        super().__init__(file_path)

    def get_news(self, line_number: int):
        ticker, news, affect = self._content[line_number].split(";")
        return (ticker, news, affect)

class Leaderboard(File):
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._content = []
        self._scores = {}
    
    def __str__(self):
        leaderboard = ""
        placement = 1
        for username in self._scores:
            leaderboard += f"place: {placement}, username: {username}, score: {self._scores[username]}\n"
            placement += 1
        return leaderboard
    
    def initialization(self):
        for line in self._content:
            username, scores = line.split()
            self.add(username, float(scores))

    def sort_leaderboard(self, leave_last: bool):
        if leave_last:
            self._scores = dict(sorted(self._scores.items(), key=operator.itemgetter(1), reverse=True))
        else:
            self._scores = dict(sorted(self._scores.items(), key=operator.itemgetter(1), reverse=True)[:-1])

    def add_to_file(self):
        f = open(self._file_path, "w")
        f = open(self._file_path, "a")
        for username in self._scores.keys():
            f.write(f"{username} {self._scores[username]}\n")
        f.close()
        
    def add(self, username: str, score: int):
        try:
            if self._scores[username] < score:
                self._scores[username] = score
        except:
            self._scores[username] = score
        if len(self._scores) > 10:
            self.sort_leaderboard(False)
        else:
            self.sort_leaderboard(True)


    