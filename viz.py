from matplotlib import pyplot as plt

def generate_frame(battlefield, fname):
    colors = {"1":lambda x: (1,0,0,x),"2":lambda x: (0,0,1,x)}
    plt.cla()
    plt.clf()
    plt.ylim([0,battlefield.shape()[0]-1])
    plt.xlim([0,battlefield.shape()[1]-1])
    plt.axes().set_xticks(range(battlefield.shape()[1]))
    plt.axes().set_yticks(range(battlefield.shape()[0]))
    plt.grid(True,which='both',axis='both')
    for x in range(battlefield.shape()[0]):
        for y in range(battlefield.shape()[1]):
            t = battlefield.get_tile(x,y)
            if t.has_unit():
                plt.scatter([y],[x],c=[colors[str(t.unit().get_allegiance())](float(t.unit().get_health())/t.unit().get_health_max())])
            elif not t.is_passable():

                plt.scatter([y],[x],c='k')
    plt.title(fname)
    plt.savefig("img/"+fname)

