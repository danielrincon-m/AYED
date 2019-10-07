from sys import stdin


class Team:
    def __init__(self, teamNumber):
        self.miembros = []
        self.teamNumber = teamNumber

    def addMember(self, member):
        self.miembros.append(member)

    def removeMember(self):
        member = self.miembros[0]
        del self.miembros[0]
        return member

    def isEmpty(self):
        return True if len(self.miembros) == 0 else False


class Queue:
    def __init__(self):
        self.queue = []
        self.teams = []

    def addElement(self, x, team):
        for i in range(len(self.teams)):
            if self.teams[i] == team:
                self.queue[i].addMember(x)
                return
        newTeam = Team(team)
        newTeam.addMember(x)
        self.queue.append(newTeam)
        self.teams.append(team)

    def removeElement(self):
        member = self.queue[0].removeMember()
        if self.queue[0].isEmpty():
            del(self.queue[0])
            del(self.teams[0])
        return member



def main():
    nTeams = int(stdin.readline().strip())
    case = 1
    while nTeams != 0:
        print('Scenario #' + str(case))
        case += 1
        teamDict = {}
        queue = Queue()
        for i in range(nTeams):
            team = [int(x) for x in stdin.readline().strip().split()]
            for j in range(1, len(team)):
                teamDict[team[j]] = i
        instruction = stdin.readline().strip()
        while instruction != 'STOP':
            if instruction == 'DEQUEUE':
                print(queue.removeElement())
            else:
                instruction, x = [x for x in instruction.split()]
                x = int(x)
                queue.addElement(x, teamDict[x])
            instruction = stdin.readline().strip()
        nTeams = int(stdin.readline().strip())
        print()


main()
