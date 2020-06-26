from collections import defaultdict
class clerks:
    def __init__(self):
        self.clerks_queus = defaultdict(list)
    def _get_other_client(self):
        for clerk in self.clerks_queus.keys():
            if self.clerks_queus[clerk] != []:
                return clerk

    def add_client_to_quese(self,clerkName,clientName):
        self.clerks_queus[clerkName].append(clientName)

    def remove_client_from_queuse(self,clerkName):
        if self.clerks_queus[clerkName] != []:
            final_clerk = clerkName
        else:
            final_clerk = self._get_other_client()
            #print(f"final {}")

        print(self.clerks_queus[final_clerk][0])
        self.clerks_queus[final_clerk].pop(0)


cmd=input("please enter an order")
quese = clerks()
while cmd != "1":
    cmd = cmd.split()
    if "wait" in cmd:
        quese.add_client_to_quese(clerkName=cmd[1],clientName=cmd[2])
    elif "next" in cmd:
        quese.remove_client_from_queuse(clerkName=cmd[1])
    cmd = input('please enter an order')








