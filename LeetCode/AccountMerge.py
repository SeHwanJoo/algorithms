class Tree:
    def __init__(self):
        self.root = range(1000*10)
    def find(self, x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
    def union(self, x, y):
        self.root[self.find(y)] = self.find(x)

class Solution(object):
    def accountsMerge(self, accounts):
        tree = Tree()
#       key: email, value: name
        email_to_name = {}
#       key: email, value: id(email)
        email_to_id = {}
        id = 0
        for account in accounts:
            for email in account[1:]:
                email_to_name[email] = account[0]
                if email not in email_to_id:
                    email_to_id[email] = id
                    id += 1
                tree.union(email_to_id[account[1]], email_to_id[email])

        ans = {}
        for email, id in email_to_id.items():
            ans[id] = []
        for email in email_to_name:
            ans[tree.find(email_to_id[email])].append(email)
        for key, value in ans.items():
            if not value:
                del ans[key]

        return [[email_to_name[v[0]]] + sorted(v) for v in ans.values()]